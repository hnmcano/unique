from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import join
from decimal import Decimal
from typing import Tuple
import pandas as pd
import requests

# --- Importações (Assuma que estão nos seus respectivos arquivos) ---
from schemas.pedidos import NovoPedidoSchema, PedidoResponse
from models.pedidos import Pedido, EnderecoPedido, ItemPedido
from models.clientes import Clientes
from models.produtos import Produto as ProdutoModel
from models.caixa import Caixa as CaixaModel
from service.websocketservice import notificar_todos
from service.depencias import get_current_user
from database.connection import get_db
from datetime import datetime

router = APIRouter()

# --- Funções Auxiliares (Simplificadas para o Exemplo) ---

def get_or_create_cliente(cliente_data, db: Session, user_current: dict) -> Tuple[int, Clientes]:
    """
    Simula a busca do cliente por e-mail/telefone ou a criação de um novo.
    Retorna o ID do cliente e o objeto Cliente.
    """
    # 1. Tenta encontrar o cliente pelo email (ou telefone)
    cliente_db = db.query(Clientes).filter(Clientes.email == cliente_data.email, Clientes.estabelecimento_id == user_current["estabelecimento_id"]).first()
    
    if not cliente_db:
        # 2. Se não existir, cria o novo cliente no DB
        cliente_db = Clientes(
            nome=cliente_data.nome,
            email=cliente_data.email,
            telefone=cliente_data.telefone,
            estabelecimento_id=user_current["estabelecimento_id"]
        )
        db.add(cliente_db)
        db.flush() # Garante que o cliente_id seja gerado antes de usar

    return cliente_db.id, cliente_db

@router.delete("/react/deletar-dados-pedidos/{pedido_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_pedido(pedido_id: int, db: Session = Depends(get_db), user_current: dict = Depends(get_current_user)):
    pedido = db.query(Pedido).filter(Pedido.id_pedido == pedido_id, Pedido.estabelecimento_id == user_current["estabelecimento_id"]).first()

    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")

    db.delete(pedido)
    db.commit()

#  Usa o schema de resposta completo para serializar o pedido final em response_model=PedidoResponse
@router.post("/react", status_code=status.HTTP_201_CREATED, response_model=PedidoResponse)
async def criar_novo_pedido(novo_pedido_data: NovoPedidoSchema,db: Session = Depends(get_db), user_current: dict = Depends(get_current_user)):

    caixa = db.query(CaixaModel).filter(CaixaModel.status == "ABERTO", CaixaModel.estabelecimento_id == user_current["estabelecimento_id"]).first()

    if not caixa:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Estamos Fechados no momento, volte mais tarde"
        )
    
    try:
        # 1. OBTER/CRIAR O CLIENTE
        # Esta função garante que tenhamos o ID do cliente logado ou recém-criado
        cliente_id = get_or_create_cliente(novo_pedido_data.cliente, db, user_current)
        
        # 2. VALIDAÇÃO DE PRECISÃO (Opcional: Verifica a soma do frontend)
        # O Pydantic já garantiu que valor_total, preco_unitario e taxa_entrega são Decimais.
        valor_total_calculado = (
            sum(item.quantidade * item.valor_unitario for item in novo_pedido_data.itens) 
            + novo_pedido_data.entrega.taxa_entrega
        )

        print("valor_total_calculado", valor_total_calculado)

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
            valor_total=novo_pedido_data.valor_total,
            estabelecimento_id=user_current["estabelecimento_id"],
            # status e data_pedido usam defaults do modelo
        )

        db.add(db_pedido)
        
        # 4. FLUSH PARA OBTER O ID DO PEDIDO (Pedido.id)
        # Necessário para usar a FK nas tabelas relacionadas
        db.flush() 

        # 5. CRIAÇÃO DO ENDEREÇO HISTÓRICO (1:1)
        
        # Converte o Pydantic 'EntregaInput' para o modelo SQLAlchemy 'EnderecoPedido'
        db_endereco = EnderecoPedido(
            pedido_id=db_pedido.id_pedido,
            **novo_pedido_data.entrega.model_dump(exclude_unset=True),
            estabelecimento_id=user_current["estabelecimento_id"] # Mapeia todos os campos de entrega
        )
        db.add(db_endereco)

        # 6. CRIAÇÃO DOS ITENS DO PEDIDO (1:N)
        
        for item_data in novo_pedido_data.itens:
            db_item = ItemPedido(
                pedido_id=db_pedido.id_pedido,
                produto_id=item_data.produto_id,
                quantidade=item_data.quantidade,
                valor_unitario=item_data.valor_unitario,
                estabelecimento_id=user_current["estabelecimento_id"]
            )
            db.add(db_item)

        # 7. COMMIT FINAL DA TRANSAÇÃO
        db.commit()
        
        # 8. REFRESH e RETORNO (Obtém o Pedido final com todas as relações carregadas)
        db.refresh(db_pedido)

        pedido_serializado = PedidoResponse.model_validate(db_pedido)

        await notificar_todos(jsonable_encoder({
            "tipo": "delivery_acionado",
            "dados": pedido_serializado.model_dump()
        }))

        return pedido_serializado
    

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
            detail=str(e)
        )
    
@router.get("/desktop/tabela", status_code=status.HTTP_200_OK, response_model=list[PedidoResponse])
def listar_pedidos(db: Session = Depends(get_db), user_current: dict = Depends(get_current_user)):
    bd_pedido = (db.query(Pedido)
                 .options(joinedload(Pedido.itens).joinedload(ItemPedido.produtos),
                          joinedload(Pedido.endereco_entrega),
                          joinedload(Pedido.cliente),
                          joinedload(Pedido.caixa),
                          joinedload(Pedido.estabelecimento_id),
                    ).all()
            )

    return bd_pedido

@router.put("/aumentar-item/{pedido_id}/{item_id}", status_code=status.HTTP_200_OK, response_model=PedidoResponse)
async def adicionar_quantidade(pedido_id: int, item_id: int, bd: Session = Depends(get_db), user_current: dict = Depends(get_current_user)):
    pedido_existente = bd.query(Pedido).filter(
        Pedido.id == pedido_id,
        Pedido.status != "CANCELADO",
        Pedido.estabelecimento_id == user_current["estabelecimento_id"]
    ).with_for_update().first()

    if not pedido_existente:
        raise HTTPException(status_code=404, detail="Pedido nao encontrado")

    item_existente = bd.query(ItemPedido).filter(ItemPedido.pedido_id == pedido_existente.id_pedido, ItemPedido.id_itens_pedido == item_id, ItemPedido.estabelecimento_id == user_current["estabelecimento_id"]).with_for_update().first()
    if not item_existente:
        raise HTTPException(status_code=404, detail="Item nao encontrado")
    
    produto_existente = bd.query(ProdutoModel).filter(ProdutoModel.id_produto == item_existente.produto_id).with_for_update().first()
    if not produto_existente:
        raise HTTPException(status_code=404, detail="Produto nao encontrado")

    if produto_existente.estoque <= 0:
        raise HTTPException(status_code=400, detail="Estoque insuficiente")
    
    item_existente.quantidade += 1
    pedido_existente.valor_total += item_existente.valor_unitario
    produto_existente.estoque += -1

    if produto_existente.estoque == 0:
        produto_existente.status_venda = "Pausado"

    bd.commit()

    bd.refresh(pedido_existente)

    pedido_response = PedidoResponse.model_validate(pedido_existente)

    await notificar_todos({
        "tipo": "pedido_em_delivery",
        "dados": jsonable_encoder(pedido_response)
    })

    return PedidoResponse.model_validate(
        pedido_existente
    )