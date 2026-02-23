from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload
from database.connection import get_db
from models.caixa import Caixa as CaixaModel
from fastapi.encoders import jsonable_encoder
from schemas.mesas import MesasResponse, AberturaMesa, AdicionarItensMesa
from models.mesas import Mesas as MesaModel, PedidosMesa as PedidosMesaModel, PedidoItens as PedidoItensModel
from models.produtos import Categoria as CategoryModel
from models.produtos import Produto as ProdutoModel
from service.websocketservice import clientes_conectados, notificar_todos
from service.depencias import get_current_user
from models.caixa import Caixa
from uuid import UUID
import time
import json

router = APIRouter()

@router.post(
    "/abrir-mesa",
    status_code=status.HTTP_200_OK,
    response_model=MesasResponse
)
def abrir_mesa(
        mesa: AberturaMesa, 
        db: Session = Depends(get_db),
        user_current: dict = Depends(get_current_user)
    ):

    caixa = db.query(CaixaModel).filter(CaixaModel.status == "ABERTO", CaixaModel.estabelecimento_id == user_current["estabelecimento_id"]).first()
    if not caixa:
        raise HTTPException(
            status_code=400,
            detail="Nenhum caixa aberto para realizar a venda"
        )

    mesa_existente = db.query(MesaModel).filter(
        MesaModel.numero == mesa.numero,
        MesaModel.estabelecimento_id == user_current["estabelecimento_id"]
    ).first()

    if mesa_existente:
        pedido_aberto = db.query(PedidosMesaModel).filter(
            PedidosMesaModel.mesa_id == mesa_existente.id_mesa,
            PedidosMesaModel.status == "ABERTO",
            PedidosMesaModel.estabelecimento_id == user_current["estabelecimento_id"]
        ).first()

        if pedido_aberto:
            return {
                "id_mesa": mesa_existente.id_mesa,
                "numero": mesa_existente.numero,
                "caixa_id": mesa_existente.caixa_id,
                "pedido": pedido_aberto
            }

    # cria mesa
    db_mesa = MesaModel(
        numero=mesa.numero,
        caixa_id=caixa.id,
        estabelecimento_id=user_current["estabelecimento_id"]
    )
    db.add(db_mesa)
    db.commit()
    db.refresh(db_mesa)

    # cria pedido vazio
    db_pedido = PedidosMesaModel(
        mesa_id=db_mesa.id_mesa,
        status="ABERTO",
        valor_total=0,
        quantidade_itens=0,
        estabelecimento_id=user_current["estabelecimento_id"]
    )

    db.add(db_pedido)
    db.commit()
    db.refresh(db_pedido)

    return {
        "id_mesa": db_mesa.id_mesa,
        "numero": db_mesa.numero,
        "caixa_id": db_mesa.caixa_id,
        "pedido": db_pedido
    }

@router.put(
    "/adicionar-produto",
    status_code=status.HTTP_201_CREATED,
    response_model=MesasResponse
)
async def adicionar_produto(
    mesa: AdicionarItensMesa,
    db: Session = Depends(get_db),
    user_current: dict = Depends(get_current_user)
):

    mesa_existente = db.query(MesaModel).filter(
        MesaModel.id_mesa == mesa.mesa_id,
        MesaModel.estabelecimento_id == user_current["estabelecimento_id"]
    ).first()

    if not mesa_existente:
        raise HTTPException(status_code=404, detail="Mesa nao encontrada")

    pedido_aberto = db.query(PedidosMesaModel).filter(
        PedidosMesaModel.mesa_id == mesa_existente.id_mesa,
        PedidosMesaModel.status == "ABERTO",
        PedidosMesaModel.estabelecimento_id == user_current["estabelecimento_id"]
    ).with_for_update().first()

    if not pedido_aberto:
        raise HTTPException(status_code=404, detail="Pedido nao encontrado")

    item_existente = db.query(PedidoItensModel).filter(PedidoItensModel.pedido_id == pedido_aberto.id_pedido_mesa, PedidoItensModel.produto_id == mesa.produto_id,
        PedidoItensModel.estabelecimento_id == user_current["estabelecimento_id"]).with_for_update().first()
    produto_existente = db.query(ProdutoModel).filter(ProdutoModel.id_produto == mesa.produto_id,
        ProdutoModel.estabelecimento_id == user_current["estabelecimento_id"]).with_for_update().first()

    estabelecimento_id = user_current["estabelecimento_id"]

    if produto_existente.estoque <= 0:
        raise HTTPException(status_code=400, detail="Estoque insuficiente")

    if item_existente:
        item_existente.quantidade += mesa.quantidade
        item_existente.valor_total = item_existente.quantidade * mesa.valor_unitario
        pedido_aberto.quantidade_itens = pedido_aberto.quantidade_itens
        pedido_aberto.valor_total += mesa.quantidade * item_existente.valor_unitario
        produto_existente.estoque -= 1

        mesa_response = MesasResponse.model_validate( {
            "id_mesa": mesa_existente.id_mesa,    
            "numero": mesa_existente.numero,
            "pedido": pedido_aberto
        })

        db.commit()

        await notificar_todos(estabelecimento_id,{
            "tipo": "produto_em_mesa",
            "dados": jsonable_encoder(mesa_response)
        })

        return {
            "id_mesa": mesa_existente.id_mesa,
            "numero": mesa_existente.numero,
            "caixa_id": mesa_existente.caixa_id,
            "pedido": pedido_aberto
        }


    # pega o item enviado no request
    item = PedidoItensModel(
        produto_id=mesa.produto_id,
        quantidade=mesa.quantidade,
        valor_unitario=mesa.valor_unitario,
        valor_total=mesa.quantidade * mesa.valor_unitario,
        estabelecimento_id=user_current["estabelecimento_id"]
    )
    
    pedido_aberto.itens.append(item)

    # atualiza totais
    pedido_aberto.quantidade_itens += 1
    pedido_aberto.valor_total += item.valor_total
    produto_existente.estoque -= item.quantidade

    db.commit()
    db.refresh(pedido_aberto)

    mesa_response = MesasResponse.model_validate( {  
        "id_mesa": mesa_existente.id_mesa,    
        "numero": mesa_existente.numero,
        "pedido": pedido_aberto
    })

    await notificar_todos(estabelecimento_id, {
        "tipo": "produto_em_mesa",
        "dados": jsonable_encoder(mesa_response)
    })

    return {
        "id_mesa": mesa_existente.id_mesa,
        "numero": mesa_existente.numero,
        "caixa_id": mesa_existente.caixa_id,
        "pedido": pedido_aberto
    }

@router.put(
    "/finalizar-pedido-mesa/{mesa_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def fechar_mesa(
    mesa_id: int, 
    db: Session = Depends(get_db),
    user_current: dict = Depends(get_current_user)
):

    mesa_existente = db.query(MesaModel).filter(
        MesaModel.id_mesa == mesa_id,
        MesaModel.estabelecimento_id == user_current["estabelecimento_id"]
    ).first()

    if not mesa_existente:
        raise HTTPException(status_code=404, detail="Mesa nao encontrada")

    pedido_aberto = db.query(PedidosMesaModel).filter(
        PedidosMesaModel.mesa_id == mesa_existente.id_mesa,
        PedidosMesaModel.status == "ABERTO",
        PedidosMesaModel.estabelecimento_id == user_current["estabelecimento_id"]
    ).first()

    if not pedido_aberto:
        raise HTTPException(status_code=404, detail="Pedido nao encontrado")

    pedido_aberto.status = "FECHADO"
    db.commit()

@router.delete(
        "/excluir-pedido-mesa/{mesa_id}", 
        status_code=status.HTTP_204_NO_CONTENT
    )
async def excluir_pedido_mesa(
    mesa_id: int, 
    db: Session = Depends(get_db),
    user_current: dict = Depends(get_current_user)
):

    mesa_existente = db.query(MesaModel).filter(
        MesaModel.id_mesa == mesa_id,
        MesaModel.estabelecimento_id == user_current["estabelecimento_id"]
    ).first()

    if not mesa_existente:
        raise HTTPException(status_code=404, detail="Mesa nao encontrada")

    pedido_aberto = db.query(PedidosMesaModel).filter(
        PedidosMesaModel.mesa_id == mesa_existente.id_mesa,
        PedidosMesaModel.status == "ABERTO",
        PedidosMesaModel.estabelecimento_id == user_current["estabelecimento_id"]
    ).first()

    if not pedido_aberto:
        raise HTTPException(status_code=404, detail="Pedido nao encontrado")

    db.delete(pedido_aberto)
    db.commit()

@router.delete(
        "/excluir-mesa/{mesa_id}", 
        status_code=status.HTTP_204_NO_CONTENT
    )
async def excluir_mesa(
    mesa_id: UUID, 
    db: Session = Depends(get_db),
    user_current: dict = Depends(get_current_user)
):

    mesa_existente = db.query(MesaModel).filter(
        MesaModel.id_mesa == mesa_id,
        MesaModel.estabelecimento_id == user_current["estabelecimento_id"]
    ).first()

    if not mesa_existente:
        raise HTTPException(status_code=404, detail="Mesa nao encontrada")
    
    pedido_aberto = (
        db.query(PedidosMesaModel)
        .options(joinedload(PedidosMesaModel.itens))
        .filter(
            PedidosMesaModel.mesa_id == mesa_id,
            PedidosMesaModel.status == "ABERTO",
            PedidosMesaModel.estabelecimento_id == user_current["estabelecimento_id"]
        )
        .first()
    )

    if not pedido_aberto:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")

    # Devolve estoque
    for item in pedido_aberto.itens:
        produto = db.get(ProdutoModel, item.produto_id)
        produto.estoque += item.quantidade

        if produto.estoque > 0:
            produto.status_venda = "Ativo"

    # Agora deleta pedido e mesa
    db.delete(pedido_aberto)
    db.delete(mesa_existente)

    # UM ÚNICO COMMIT
    db.commit()

    raise HTTPException(status_code=200, detail="Mesa excluida com sucesso")

@router.get(
        "/em-atendimento", 
        status_code=status.HTTP_200_OK
    )
async def mesas_em_atendimento(
    db: Session = Depends(get_db),
    user_current: dict = Depends(get_current_user)
):
    pedidos_abertos = db.query(PedidosMesaModel).filter(PedidosMesaModel.status == "ABERTO",
        PedidosMesaModel.estabelecimento_id == user_current["estabelecimento_id"]).all()
    
    mesas_em_atendimento = []

    for pedido in pedidos_abertos:
        mesa = db.query(MesaModel).filter(MesaModel.id_mesa == pedido.mesa_id, MesaModel.estabelecimento_id == user_current["estabelecimento_id"]).first()
        mesas_em_atendimento.append(mesa.numero)

    return mesas_em_atendimento

@router.delete(
        "/excluir-item/{mesa_id}/{pedido_id}/{item_id}", 
        status_code=status.HTTP_200_OK
)
async def excluir_item_pedido_mesa(
    mesa_id: UUID, 
    pedido_id: UUID, 
    item_id: UUID, 
    db: Session = Depends(get_db),
    user_current: dict = Depends(get_current_user)
):  
    mesa = db.query(MesaModel).filter(MesaModel.id_mesa == mesa_id, MesaModel.estabelecimento_id == user_current["estabelecimento_id"]).first()
    pedido = db.query(
        PedidosMesaModel
    ).filter(PedidosMesaModel.mesa_id == mesa_id, 
                PedidosMesaModel.id_pedido_mesa == pedido_id, 
                PedidosMesaModel.estabelecimento_id == user_current["estabelecimento_id"]
            ).with_for_update().first()

    if mesa and pedido:
        item_existente = db.query(PedidoItensModel).filter(PedidoItensModel.pedido_id == pedido_id, PedidoItensModel.produto_id == item_id, PedidoItensModel.estabelecimento_id == user_current["estabelecimento_id"]).with_for_update().first()

        if not item_existente:
            raise HTTPException(status_code=404, detail="Item nao encontrado")

        pedido.quantidade_itens -= 1
        pedido.valor_total -= item_existente.quantidade * item_existente.valor_unitario

        pedido_aberto = (
            db.query(PedidosMesaModel)
            .options(
                joinedload(PedidosMesaModel.itens)
            )
            .filter(
                PedidosMesaModel.mesa_id == mesa_id,
                PedidosMesaModel.status == "ABERTO",
                PedidosMesaModel.estabelecimento_id == user_current["estabelecimento_id"]
            )
            .first()
        )

        if not pedido_aberto:
            raise HTTPException(status_code=404, detail="Pedido nao encontrado")

        produto = db.query(ProdutoModel).filter(ProdutoModel.id_produto == item_existente.produto_id, ProdutoModel.estabelecimento_id == user_current["estabelecimento_id"]).first()
        produto.estoque += item_existente.quantidade

        db.delete(item_existente)
        db.commit()

        if produto.estoque > 0:
            produto.status_venda = "Ativo"
        
        db.commit()

        estabelecimento_id = user_current["estabelecimento_id"]

        mesa_response = MesasResponse.model_validate( {  
            "id_mesa": mesa.id_mesa,    
            "numero": mesa.numero,
            "pedido": pedido
        })

        await notificar_todos(estabelecimento_id, {
            "tipo": "produto_em_mesa",
            "dados": jsonable_encoder(mesa_response)
        })

    else:
        raise HTTPException(status_code=404, detail="Mesa ou pedido não encontrados.")
    
@router.put("/aumentar-item/{mesa_id}/{pedido_id}/{item_id}", status_code=status.HTTP_200_OK, response_model=MesasResponse)
async def adicionar_quantidade(mesa_id: UUID, pedido_id: UUID, item_id: UUID, bd: Session = Depends(get_db), user_current: dict = Depends(get_current_user)):
    mesa_existente = bd.query(MesaModel).filter(MesaModel.id_mesa == mesa_id, MesaModel.estabelecimento_id == user_current["estabelecimento_id"]).first()
    pedido_existente = bd.query(
        PedidosMesaModel
        ).filter(
            PedidosMesaModel.id_pedido_mesa == pedido_id, 
            PedidosMesaModel.mesa_id == mesa_existente.id_mesa, 
            PedidosMesaModel.status == "ABERTO",
            PedidosMesaModel.estabelecimento_id == user_current["estabelecimento_id"]
        ).first()

    item_existente = bd.query(PedidoItensModel).filter(PedidoItensModel.pedido_id == pedido_existente.id_pedido_mesa, PedidoItensModel.produto_id == item_id, PedidoItensModel.estabelecimento_id == user_current["estabelecimento_id"]).first()
    if not item_existente:
        raise HTTPException(status_code=404, detail="Item nao encontrado")
    
    produto_existente = bd.query(ProdutoModel).filter(ProdutoModel.id_produto == item_existente.produto_id, ProdutoModel.estabelecimento_id == user_current["estabelecimento_id"]).with_for_update().first()
    if not produto_existente:
        raise HTTPException(status_code=404, detail="Produto nao encontrado")
    
    if produto_existente.estoque <= 0:
        raise HTTPException(status_code=409, detail="Estoque insuficiente")
 
    item_existente.quantidade += 1
    item_existente.valor_total += item_existente.valor_unitario
    pedido_existente.valor_total += item_existente.valor_unitario
    produto_existente.estoque += -1

    if produto_existente.estoque == 0:
        produto_existente.status_venda = "Pausado"

    bd.commit()

    estabelecimento_id = user_current["estabelecimento_id"]

    mesa_response = MesasResponse.model_validate( {  
        "id_mesa": mesa_existente.id_mesa,    
        "numero": mesa_existente.numero,
        "pedido": pedido_existente
    })

    await notificar_todos(estabelecimento_id, {
        "tipo": "produto_em_mesa",
        "dados": jsonable_encoder(mesa_response)
    })

    return mesa_response

@router.put("/diminuir-item/{mesa_id}/{pedido_id}/{item_id}", status_code=status.HTTP_200_OK, response_model=MesasResponse)
async def remover_quantidade(mesa_id: UUID, pedido_id: UUID, item_id: UUID, bd: Session = Depends(get_db), user_current: dict = Depends(get_current_user)):
    mesa_existente = bd.query(MesaModel).filter(MesaModel.id_mesa == mesa_id, MesaModel.estabelecimento_id == user_current["estabelecimento_id"]).first()
    pedido_existente = bd.query(
        PedidosMesaModel
        ).filter(
            PedidosMesaModel.id_pedido_mesa == pedido_id, 
            PedidosMesaModel.mesa_id == mesa_existente.id_mesa, 
            PedidosMesaModel.status == "ABERTO",
            PedidosMesaModel.estabelecimento_id == user_current["estabelecimento_id"]
        ).first()

    item_existente = bd.query(PedidoItensModel).filter(PedidoItensModel.pedido_id == pedido_existente.id_pedido_mesa, PedidoItensModel.produto_id == item_id, PedidoItensModel.estabelecimento_id == user_current["estabelecimento_id"]).first()
    if not item_existente:
        raise HTTPException(status_code=404, detail="Item nao encontrado")
    
    produto_existente = bd.query(ProdutoModel).filter(ProdutoModel.id_produto == item_existente.produto_id, ProdutoModel.estabelecimento_id == user_current["estabelecimento_id"]).with_for_update().first()

    if not produto_existente:
        raise HTTPException(status_code=404, detail="Produto nao encontrado")

    estabelecimento_id = user_current["estabelecimento_id"]

    if item_existente.quantidade == 1:
        mesa_response = MesasResponse.model_validate( {  
            "id_mesa": mesa_existente.id_mesa,    
            "numero": mesa_existente.numero,
            "pedido": pedido_existente
        })

        await notificar_todos(estabelecimento_id, {
            "tipo": "produto_em_mesa",
            "dados": jsonable_encoder(mesa_response)
        })

        return mesa_response

    item_existente.quantidade += -1
    item_existente.valor_total += -item_existente.valor_unitario
    pedido_existente.valor_total += -item_existente.valor_unitario
    produto_existente.estoque += 1

    if produto_existente.estoque > 0:
        produto_existente.status_venda = "Ativo"

    bd.commit()

    mesa_response = MesasResponse.model_validate( {  
        "id_mesa": mesa_existente.id_mesa,    
        "numero": mesa_existente.numero,
        "pedido": pedido_existente
    })

    await notificar_todos(estabelecimento_id, {
        "tipo": "produto_em_mesa",
        "dados": jsonable_encoder(mesa_response)
    })

    return mesa_response


@router.get("/add-produto", status_code=status.HTTP_200_OK)
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
