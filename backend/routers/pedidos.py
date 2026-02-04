from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import join
from decimal import Decimal
from typing import Tuple
import pandas as pd
import requests

# --- Importações (Assuma que estão nos seus respectivos arquivos) ---
from schemas.pedidos import NovoPedidoSchema, PedidoResponse
from models.pedidos import Pedido, EnderecoPedido, ItemPedido
from models.clientes import Clientes
from models.caixa import Caixa as CaixaModel
from bd.connection import get_db
from datetime import datetime

router = APIRouter()

# --- Funções Auxiliares (Simplificadas para o Exemplo) ---

def get_or_create_cliente(cliente_data, db: Session) -> Tuple[int, Clientes]:
    """
    Simula a busca do cliente por e-mail/telefone ou a criação de um novo.
    Retorna o ID do cliente e o objeto Cliente.
    """
    # 1. Tenta encontrar o cliente pelo email (ou telefone)
    cliente_db = db.query(Clientes).filter(Clientes.email == cliente_data.email).first()
    
    if not cliente_db:
        # 2. Se não existir, cria o novo cliente no DB
        cliente_db = Clientes(
            nome=cliente_data.nome,
            email=cliente_data.email,
            telefone=cliente_data.telefone
        )
        db.add(cliente_db)
        db.flush() # Garante que o cliente_id seja gerado antes de usar

    return cliente_db.id, cliente_db

@router.delete("/react/deletar-dados-pedidos/{pedido_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_pedido(pedido_id: int, db: Session = Depends(get_db)):
    pedido = db.query(Pedido).filter(Pedido.id == pedido_id).first()

    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")

    db.delete(pedido)
    db.commit()

#  Usa o schema de resposta completo para serializar o pedido final em response_model=PedidoResponse
@router.post("/react", status_code=status.HTTP_201_CREATED, response_model=PedidoResponse)
async def criar_novo_pedido(novo_pedido_data: NovoPedidoSchema,db: Session = Depends(get_db)):

    caixa = db.query(CaixaModel).filter(CaixaModel.status == "ABERTO").first()

    if not caixa:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Estamos Fechados no momento, volte mais tarde"
        )
    
    try:
        # 1. OBTER/CRIAR O CLIENTE
        # Esta função garante que tenhamos o ID do cliente logado ou recém-criado
        cliente_id, cliente_objeto = get_or_create_cliente(novo_pedido_data.cliente, db)
        
        # 2. VALIDAÇÃO DE PRECISÃO (Opcional: Verifica a soma do frontend)
        # O Pydantic já garantiu que valor_total, preco_unitario e taxa_entrega são Decimais.
        valor_total_calculado = (
            sum(item.quantidade * item.valor_unitario for item in novo_pedido_data.itens) 
            + novo_pedido_data.entrega.taxa_entrega
        )

        if abs(valor_total_calculado - novo_pedido_data.valor_total) > Decimal('0.01'):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="Valor total do pedido inconsistente."
            )

        # 3. CRIAÇÃO DO OBJETO PEDIDO PRINCIPAL
        
        db_pedido = Pedido(
            cliente_id=cliente_id,
            caixa_id=caixa.id,
            metodo_pagamento=novo_pedido_data.metodo_pagamento,
            valor_total=novo_pedido_data.valor_total
            # status e data_pedido usam defaults do modelo
        )

        db.add(db_pedido)
        
        # 4. FLUSH PARA OBTER O ID DO PEDIDO (Pedido.id)
        # Necessário para usar a FK nas tabelas relacionadas
        db.flush() 

        # 5. CRIAÇÃO DO ENDEREÇO HISTÓRICO (1:1)
        
        # Converte o Pydantic 'EntregaInput' para o modelo SQLAlchemy 'EnderecoPedido'
        db_endereco = EnderecoPedido(
            pedido_id=db_pedido.id,
            **novo_pedido_data.entrega.model_dump(exclude_unset=True) # Mapeia todos os campos de entrega
        )
        db.add(db_endereco)

        # 6. CRIAÇÃO DOS ITENS DO PEDIDO (1:N)
        
        for item_data in novo_pedido_data.itens:
            db_item = ItemPedido(
                pedido_id=db_pedido.id,
                produto_id=item_data.produto_id,
                quantidade=item_data.quantidade,
                valor_unitario=item_data.valor_unitario,
            )
            db.add(db_item)

        # 7. COMMIT FINAL DA TRANSAÇÃO
        db.commit()
        
        # 8. REFRESH e RETORNO (Obtém o Pedido final com todas as relações carregadas)
        db.refresh(db_pedido) 
        
        # Retorna o objeto SQLAlchemy, que é serializado pelo PedidoResponse
        return db_pedido 

    except HTTPException:
        # Repassa exceções HTTPException (como o erro de valor total)
        db.rollback() 
        raise
        
    except Exception as e:
        # Se ocorrer qualquer outro erro (DB, lógica, etc.), faz rollback
        db.rollback() 
        # Retorna um erro genérico 500
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro interno do servidor. Não foi possível finalizar o pedido."
        )
    

@router.get("/delivery/desktop")
async def read_pedidos(db: Session = Depends(get_db)):    
    pedidos = db.query(Pedido).all()
    clientes_pedidos = db.query(Clientes).all()

    if len(pedidos) == 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Nenhum pedido encontrado")
    else:
        p =  pd.DataFrame([p.__dict__ for p in pedidos])
        c =  pd.DataFrame([c.__dict__ for c in clientes_pedidos])

        p = p.drop(columns=["_sa_instance_state"], errors="ignore") 
        c = c.drop(columns=["_sa_instance_state"], errors="ignore")

        p["data_pedido"] = p["data_criacao"].dt.strftime("%Y-%m-%d")
        p["hora_pedido"] = p["data_criacao"].dt.strftime("%H:%M:%S")
        p["valor_total"] = p["valor_total"].astype("float").round(2)  

        p = p.drop(columns=["data_criacao"])

        data = pd.merge(p, c, left_on="cliente_id", right_on="id", how="left")
        data = data.drop(columns=["id_y"]).rename(columns={"id_x": "id"}).to_dict("records")
        
        raise HTTPException(status_code=status.HTTP_200_OK, detail=data)
        
@router.put("/desktop/atualizar/{pedido_id}", response_model=PedidoResponse)
async def update_pedido(pedido_id: int, pedido: NovoPedidoSchema, db: Session = Depends(get_db)):

    db_pedido = db.query(Pedido).filter(Pedido.id == pedido_id).first()
    if db_pedido:
        db_pedido.status = pedido.status
        db.commit()
        db.refresh(db_pedido)
        return db_pedido
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Pedido nao encontrado")

