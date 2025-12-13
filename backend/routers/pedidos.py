from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from decimal import Decimal
from typing import Tuple
import requests

# --- Importações (Assuma que estão nos seus respectivos arquivos) ---
from schemas.pedidos import NovoPedidoSchema, PedidoResponse
from models.pedidos import Pedido, Cliente, EnderecoPedido, ItemPedido, PedidoDesktopView
from bd.connection import get_db

router = APIRouter()

# --- Funções Auxiliares (Simplificadas para o Exemplo) ---

def get_or_create_cliente(cliente_data, db: Session) -> Tuple[int, Cliente]:
    """
    Simula a busca do cliente por e-mail/telefone ou a criação de um novo.
    Retorna o ID do cliente e o objeto Cliente.
    """
    # 1. Tenta encontrar o cliente pelo email (ou telefone)
    cliente_db = db.query(Cliente).filter(Cliente.email == cliente_data.email).first()
    
    if not cliente_db:
        # 2. Se não existir, cria o novo cliente no DB
        cliente_db = Cliente(
            nome=cliente_data.nome,
            email=cliente_data.email,
            telefone=cliente_data.telefone
        )
        db.add(cliente_db)
        db.flush() # Garante que o cliente_id seja gerado antes de usar

    return cliente_db.id, cliente_db

# --- ROTA PRINCIPAL ---

#  Usa o schema de resposta completo para serializar o pedido final em response_model=PedidoResponse
@router.post("/react", status_code=status.HTTP_201_CREATED, response_model=PedidoResponse)
async def criar_novo_pedido(novo_pedido_data: NovoPedidoSchema,db: Session = Depends(get_db)):
    """
    Processa e salva um novo pedido, incluindo endereço histórico e itens.
    """
    
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

        print(f"Valor total calculado: {valor_total_calculado}")
        print(f"Valor total do pedido: {novo_pedido_data.valor_total}")

        print(valor_total_calculado - novo_pedido_data.valor_total)

        if abs(valor_total_calculado - novo_pedido_data.valor_total) > Decimal('0.01'):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="Valor total do pedido inconsistente."
            )

        # 3. CRIAÇÃO DO OBJETO PEDIDO PRINCIPAL
        
        db_pedido = Pedido(
            cliente_id=cliente_id,
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
        print(f"Erro inesperado ao criar pedido: {e}")
        # Retorna um erro genérico 500
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro interno do servidor. Não foi possível finalizar o pedido."
        )
    

@router.get("/delivery/desktop")
async def read_pedidos(db: Session = Depends(get_db)):
    return db.query(PedidoDesktopView).all()

