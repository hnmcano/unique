from fastapi import APIRouter, Depends, HTTPException, status, Query, WebSocket, WebSocketDisconnect
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import join
from decimal import Decimal
from typing import Tuple
from uuid import UUID
import pandas as pd
import requests

# --- Importações (Assuma que estão nos seus respectivos arquivos) ---
from schemas.pedidos import NovoPedidoSchema, PedidoResponse, AlteracaoItemPedido, DeletarItem, AdicionarProdutosPedido, AtualizarStatus
from models.pedidos import Pedido, EnderecoPedido, ItemPedido
from models.clientes import Clientes
from models.produtos import Produto as ProdutoModel
from models.produtos import Categoria as CategoryModel
from models.estabelecimento import Estabelecimento as EstabelecimentoModel
from models.caixa import Caixa as CaixaModel

from core.dependencies.tenant import get_estabelecimento
from service.websocketservice import notificar_todos, estabelecimento_esta_online
from service.websocketservice import notificar_pedido
from service.depencias import get_current_user
from database.connection import get_db
from datetime import datetime

router = APIRouter()

# --- Funções Auxiliares (Simplificadas para o Exemplo) ---
def get_or_create_cliente(cliente_data, db: Session, estabelecimento: dict) -> Tuple[int, Clientes]:
    """
    Simula a busca do cliente por e-mail/telefone ou a criação de um novo.
    Retorna o ID do cliente e o objeto Cliente.
    """
    # 1. Tenta encontrar o cliente pelo email (ou telefone)
    cliente_db = db.query(Clientes).filter(Clientes.nome == cliente_data.nome, Clientes.estabelecimento_id == estabelecimento.id).first()
    
    if not cliente_db:
        # 2. Se não existir, cria o novo cliente no DB
        cliente_db = Clientes(
            nome=cliente_data.nome,
            email=cliente_data.email,
            telefone=cliente_data.telefone,
            estabelecimento_id=estabelecimento.id,
            cpf=cliente_data.cpf
        )
        db.add(cliente_db)
        db.flush() # Garante que o cliente_id seja gerado antes de usar

    return cliente_db.id, cliente_db

#  Usa o schema de resposta completo para serializar o pedido final em response_model=PedidoResponse
@router.post("/react", status_code=status.HTTP_200_OK, response_model=PedidoResponse)
async def criar_novo_pedido(novo_pedido_data: NovoPedidoSchema,db: Session = Depends(get_db), estabelecimento: EstabelecimentoModel = Depends(get_estabelecimento)):

    caixa = db.query(CaixaModel).filter(CaixaModel.status == "ABERTO", CaixaModel.estabelecimento_id == estabelecimento.id).first()

    status_estabelecimento = estabelecimento_esta_online(estabelecimento.id)

    if status_estabelecimento == False or not caixa:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Estamos Fechados no momento, volte mais tarde!"
        )
    
    try:
        # 1. OBTER/CRIAR O CLIENTE
        # Esta função garante que tenhamos o ID do cliente logado ou recém-criado
        id, cliente_id = get_or_create_cliente(novo_pedido_data.cliente, db, estabelecimento)
        
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
            cliente_id=id,
            caixa_id=caixa.id,
            metodo_pagamento=novo_pedido_data.metodo_pagamento,
            opcoes_pagamento=novo_pedido_data.opcoes_pagamento,
            valor_total=novo_pedido_data.valor_total,
            estabelecimento_id=estabelecimento.id,
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
            estabelecimento_id=estabelecimento.id # Mapeia todos os campos de entrega
        )
        db.add(db_endereco)

        # 6. CRIAÇÃO DOS ITENS DO PEDIDO (1:N)
        
        for item_data in novo_pedido_data.itens:
            db_item = ItemPedido(
                pedido_id=db_pedido.id_pedido,
                produto_id=item_data.produto_id,
                quantidade=item_data.quantidade,
                valor_unitario=item_data.valor_unitario,
                estabelecimento_id=estabelecimento.id
            )
            db.add(db_item)     

        for item_data in novo_pedido_data.itens:
            produto = db.get(ProdutoModel, item_data.produto_id)

            if not produto:
                continue

            produto.estoque -= item_data.quantidade

            if produto.estoque <= 0:
                produto.status_venda = "Pausado"

        caixa.valor_final += db_pedido.valor_total

        db.commit()
        db.refresh(db_pedido)
        db.refresh(caixa)

        pedido_serializado = PedidoResponse.model_validate(db_pedido)
        estabelecimento_id=estabelecimento.id

        await notificar_todos(estabelecimento_id, {
            "tipo": "delivery_acionado",
            "dados": jsonable_encoder(pedido_serializado)
        })

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
def listar_pedidos( after: datetime | None = Query(None), before: datetime | None = Query(None), db: Session = Depends(get_db), user_current: dict = Depends(get_current_user)):

    caixa_aberto = db.query(CaixaModel).filter(CaixaModel.status == "ABERTO", CaixaModel.estabelecimento_id == user_current["estabelecimento_id"]).first()

    if not caixa_aberto:
        return []

    query = (db.query(Pedido)
                 .options(joinedload(Pedido.itens).joinedload(ItemPedido.produtos),
                          joinedload(Pedido.endereco_entrega),
                          joinedload(Pedido.cliente),
                          joinedload(Pedido.caixa),
                          joinedload(Pedido.estabelecimento),
                    )
                    .filter(Pedido.caixa_id == caixa_aberto.id)
            )

    if after:
        query = query.filter(Pedido.data_criacao > after )

    if before:
        query = query.filter(Pedido.data_criacao < before)

    pedido = query.order_by(Pedido.data_criacao.asc()).all()

    return pedido

@router.put("/desktop/atualizar-quantidade",status_code=status.HTTP_200_OK, response_model=PedidoResponse)
async def atualizar_quantidade(novaquantidade: AlteracaoItemPedido , db: Session = Depends(get_db), user_current: dict = Depends(get_current_user)):

    item = db.query(ItemPedido).filter(ItemPedido.estabelecimento_id == user_current["estabelecimento_id"],
                                                ItemPedido.pedido_id == novaquantidade.pedido_id,
                                                ItemPedido.id_itens_pedido == novaquantidade.id_itens_pedido,
                                                ItemPedido.produto_id == novaquantidade.produto_id).with_for_update().first()

    if not item:
        raise HTTPException(
                status_code=400, 
                detail="Item não existe no pedido"
            )

    if novaquantidade.quantidade <= 0:
        raise HTTPExeception(
            status_code=400,
            detail="Quantidade Invalida"
        )


    produto = (db.query(ProdutoModel)
        .filter(
            ProdutoModel.id_produto == item.produto_id,
            ProdutoModel.estabelecimento_id == user_current["estabelecimento_id"]
        )
        .with_for_update()
        .first()
    )

    pedido = (
        db.query(Pedido)
        .filter(
            Pedido.id_pedido == novaquantidade.pedido_id,
            Pedido.estabelecimento_id == user_current["estabelecimento_id"]
        )
        .with_for_update()
        .first()
    )

    diferenca = novaquantidade.quantidade - item.quantidade

    caixa_aberto = (
        db.query(CaixaModel)
        .filter(
            CaixaModel.id == pedido.caixa_id,
            CaixaModel.estabelecimento_id == user_current["estabelecimento_id"]
        )
        .with_for_update()
        .first()
    )

    # validar estoque
    if diferenca > 0 and produto.estoque < diferenca:
        raise HTTPException(
            status_code=400,
            detail="Estoque insuficiente"
        )

    # atualizar estoque
    produto.estoque -= diferenca

    # atualizar item
    item.quantidade = novaquantidade.quantidade

    # atualizar total do pedido
    pedido.valor_total += diferenca * item.valor_unitario
    caixa_aberto.valor_final += diferenca * item.valor_unitario

    if produto.estoque == 0:
        produto.status_venda = "Pausado"

    if produto.estoque > 0:
        produto.status_venda = "Ativo"

    db.commit()
    db.refresh(pedido)

    pedido_schema = PedidoResponse.model_validate(pedido)

    estabelecimento_id= pedido.estabelecimento_id

    await notificar_todos(estabelecimento_id, {
        "tipo": "pedido_em_delivery_atualizado",
        "dados": jsonable_encoder(pedido_schema)
    })


    await notificar_pedido(pedido.id_pedido, {
        "tipo": "pedido_status",
        "dados": jsonable_encoder(pedido_schema)
    })

    return pedido_schema

@router.delete("/desktop/deletar-dados-pedidos/{pedido_id}", status_code=status.HTTP_200_OK)
async def delete_pedido(pedido_id: UUID, db: Session = Depends(get_db), user_current: dict = Depends(get_current_user)):

    
    pedido = db.query(Pedido).filter(Pedido.id_pedido == pedido_id, Pedido.estabelecimento_id == user_current["estabelecimento_id"]).first()
    caixa_aberto = db.query(CaixaModel).filter(CaixaModel.id == pedido.caixa_id, CaixaModel.estabelecimento_id == user_current["estabelecimento_id"]).first()

    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")

    for item in pedido.itens:
        produto = db.get(ProdutoModel, item.produto_id)
        produto.estoque += item.quantidade

        if produto.estoque > 0:
            produto.status_venda = "Ativo"

    caixa_aberto.valor_final -= pedido.valor_total

    db.delete(pedido)
    db.commit()

@router.delete("/desktop/deletar-item-pedido", status_code=status.HTTP_200_OK, response_model=PedidoResponse)
async def delete_item_pedido(itemDeletar: DeletarItem , db: Session = Depends(get_db), user_current: dict = Depends(get_current_user)):

    item = db.query(ItemPedido).filter(ItemPedido.estabelecimento_id == user_current["estabelecimento_id"], 
                                        ItemPedido.id_itens_pedido == itemDeletar.id_itens_pedido,
                                        ItemPedido.pedido_id == itemDeletar.id_pedido).with_for_update().first()

    if not item:
        raise HTTPException(status_code=404, detail="Item não encontrado!")

    pedido = db.query(Pedido).filter(Pedido.estabelecimento_id == user_current["estabelecimento_id"],
                                    Pedido.id_pedido == itemDeletar.id_pedido).with_for_update().first()

    produto = db.get(ProdutoModel, item.produto_id)
    produto.estoque += item.quantidade  
    item.valor_total += -(item.quantidade * item.valor_unitario)

    if produto.estoque > 0:
        produto.status_venda = "Ativo"

    caixa_aberto = db.query(CaixaModel).filter(CaixaModel.estabelecimento_id == user_current["estabelecimento_id"],
                                    CaixaModel.id == pedido.caixa_id).with_for_update().first()


    caixa_aberto.valor_final -= item.valor_total

    db.delete(item)
    db.commit()
    db.flush()

    pedido = db.query(Pedido).filter(Pedido.estabelecimento_id == user_current["estabelecimento_id"],
                                        Pedido.id_pedido == itemDeletar.id_pedido).with_for_update().first()

    estabelecimento_id = pedido.estabelecimento_id

    pedido_schema = PedidoResponse.model_validate(pedido)

    await notificar_todos(estabelecimento_id, {
        "tipo": "pedido_em_delivery_atualizado",
        "dados": jsonable_encoder(pedido_schema)
    })

    await notificar_pedido(pedido.id_pedido, {
        "tipo": "pedido_status",
        "dados": jsonable_encoder(pedido_schema)
    })

    return pedido_schema

@router.get("/desktop/add-produto", status_code=status.HTTP_200_OK)
async def read_products(db: Session = Depends(get_db), user_current: dict = Depends(get_current_user)):
    estabelecimento_id = user_current["estabelecimento_id"]

    produtos = db.query(ProdutoModel).filter(ProdutoModel.estabelecimento_id == estabelecimento_id).all()
    categorias = db.query(CategoryModel).filter(CategoryModel.estabelecimento_id == estabelecimento_id).all()

    if not produtos:
        return []

    categorias_map = {
        c.id_categoria: c.nome for c in categorias
    }

    data = []

    for p in produtos:

        nome_categoria = categorias_map.get(p.categoria_id, "Sem categoria")

        produto = {
            "id": p.id_produto,
            "categoria_id": p.categoria_id,
            "cod_pdv": p.cod_pdv,
            "nome": p.nome,
            "preco_custo": p.preco_custo,
            "preco_venda": p.preco_venda,
            "medida": p.medida,
            "estoque": p.estoque,
            "estoque_min": p.estoque_min,
            "descricao": p.descricao,
            "ficha_tecnica": p.ficha_tecnica,
            "status_venda": p.status_venda,
            "imagem_name": p.imagem_name,
            "imagem": p.imagem
        }

        produto["nome_categoria"] = nome_categoria
        data.append(produto)

    filter = []
    
    for p in data:
        if p["status_venda"] == "Ativo":
            filter.append(p)

    return filter

@router.put("/desktop/adicionar-produto", status_code=status.HTTP_201_CREATED, response_model=PedidoResponse)
async def adicionar_produto(pedido_add: AdicionarProdutosPedido, db: Session = Depends(get_db), user_current: dict = Depends(get_current_user)):

    pedido = db.query(Pedido).filter(
        Pedido.id_pedido == pedido_add.pedido_id,
        Pedido.estabelecimento_id == user_current["estabelecimento_id"]
    ).first()

    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido nao encontrado")

    item_existente = db.query(ItemPedido).filter(
        ItemPedido.pedido_id == pedido_add.pedido_id,
        ItemPedido.produto_id == pedido_add.produto_id,
        ItemPedido.estabelecimento_id == user_current["estabelecimento_id"]
    ).with_for_update().first()

    produto_existente = db.query(ProdutoModel).filter(ProdutoModel.id_produto == pedido_add.produto_id,
        ProdutoModel.estabelecimento_id == user_current["estabelecimento_id"]).with_for_update().first()

    estabelecimento_id = produto_existente.estabelecimento_id

    if produto_existente.estoque <= 0:
        raise HTTPException(status_code=400, detail="Estoque insuficiente")

    if item_existente:
        item_existente.quantidade += pedido_add.quantidade
        item_existente.valor_total = item_existente.quantidade * pedido_add.valor_unitario
        pedido.valor_total += pedido_add.quantidade * item_existente.valor_unitario
        produto_existente.estoque -= 1

        pedido_response = PedidoResponse.model_validate(pedido)

        db.commit()

        await notificar_todos(estabelecimento_id,{
            "tipo": "pedido_em_delivery",
            "dados": jsonable_encoder(pedido_response)
        })

        return pedido_response


    # pega o item enviado no request
    item = ItemPedido(
        produto_id=pedido_add.produto_id,
        quantidade=pedido_add.quantidade,
        valor_unitario=pedido_add.valor_unitario,
        valor_total=pedido_add.quantidade * pedido_add.valor_unitario,
        estabelecimento_id=user_current["estabelecimento_id"]
    )
    
    pedido.itens.append(item)

    caixa_aberto = db.query(CaixaModel).filter(CaixaModel.estabelecimento_id == user_current["estabelecimento_id"],
                                    CaixaModel.id == pedido.caixa_id).with_for_update().first()

    # atualiza totais
    pedido.valor_total += item.valor_total
    produto_existente.estoque -= item.quantidade
    caixa_aberto.valor_final += item.valor_total

    db.commit()
    db.refresh(pedido)

    pedido_response = PedidoResponse.model_validate(pedido)

    await notificar_todos(estabelecimento_id, {
        "tipo": "pedido_em_delivery_atualizado",
        "dados": jsonable_encoder(pedido_response)
    })

    await notificar_pedido(pedido.id_pedido, {
        "tipo": "pedido_status",
        "dados": jsonable_encoder(pedido_response)
    })

    return pedido_response

@router.put("/desktop/atualizar-status", response_model=PedidoResponse)
async def atualizar_status(data_atualizacao: AtualizarStatus, db: Session = Depends(get_db), user_current: dict = Depends(get_current_user)):

    pedido = db.query(Pedido).filter(
                                        Pedido.id_pedido == data_atualizacao.pedido_id, 
                                        Pedido.estabelecimento_id == user_current["estabelecimento_id"], 
                                        Pedido.status == data_atualizacao.status_antigo
                                    ).with_for_update().first()

    if not pedido:
        raise HTTPException(status_code=400, detail="Pedido nao encontrado")

    pedido.status = data_atualizacao.status_novo

    db.add(pedido)
    db.commit()
    db.flush()

    pedido = db.query(Pedido).filter(
                                    Pedido.id_pedido == data_atualizacao.pedido_id, 
                                    Pedido.estabelecimento_id == user_current["estabelecimento_id"]
                                ).first()


    pedido_response = PedidoResponse.model_validate(pedido)

    estabelecimento_id = pedido.estabelecimento_id

    await notificar_todos(estabelecimento_id, {
        "tipo": "pedido_em_delivery_atualizado",
        "dados": jsonable_encoder(pedido_response)
    })

    await notificar_pedido(pedido.id_pedido, {
        "tipo": "pedido_status",
        "dados": jsonable_encoder(pedido_response)
    })

    return pedido_response
