from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from bd.connection import get_db
from models.caixa import Caixa as CaixaModel
from fastapi.encoders import jsonable_encoder
from schemas.mesas import MesasResponse, AberturaMesa, AdicionarItensMesa
from models.mesas import Mesas as MesaModel, PedidosMesa as PedidosMesaModel, PedidoItens as PedidoItensModel
from models.produtos import Produto as ProdutoModel
from service.websocketservice import clientes_conectados, notificar_todos
from models.caixa import Caixa
import time
import json

router = APIRouter()

@router.post(
    "/abrir-mesa",
    status_code=status.HTTP_201_CREATED,
    response_model=MesasResponse
)
def abrir_mesa(mesa: AberturaMesa, db: Session = Depends(get_db)):

    caixa = db.query(CaixaModel).filter(CaixaModel.status == "ABERTO").first()
    if not caixa:
        raise HTTPException(
            status_code=400,
            detail="Nenhum caixa aberto para realizar a venda"
        )

    mesa_existente = db.query(MesaModel).filter(
        MesaModel.numero == mesa.numero
    ).first()

    if mesa_existente:
        pedido_aberto = db.query(PedidosMesaModel).filter(
            PedidosMesaModel.mesa_id == mesa_existente.id,
            PedidosMesaModel.status == "ABERTO"
        ).first()

        if pedido_aberto:
            return {
                "id": mesa_existente.id,
                "numero": mesa_existente.numero,
                "caixa_id": mesa_existente.caixa_id,
                "pedido": pedido_aberto
            }

    # cria mesa
    db_mesa = MesaModel(
        numero=mesa.numero,
        caixa_id=caixa.id
    )
    db.add(db_mesa)
    db.commit()
    db.refresh(db_mesa)

    # cria pedido vazio
    db_pedido = PedidosMesaModel(
        mesa_id=db_mesa.id,
        status="ABERTO",
        valor_total=0,
        quantidade_itens=0
    )

    db.add(db_pedido)
    db.commit()
    db.refresh(db_pedido)

    return {
        "id": db_mesa.id,
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
    db: Session = Depends(get_db)
):

    mesa_existente = db.query(MesaModel).filter(
        MesaModel.id == mesa.mesa_id
    ).first()

    if not mesa_existente:
        raise HTTPException(status_code=404, detail="Mesa nao encontrada")

    pedido_aberto = db.query(PedidosMesaModel).filter(
        PedidosMesaModel.mesa_id == mesa_existente.id,
        PedidosMesaModel.status == "ABERTO"
    ).first()

    if not pedido_aberto:
        raise HTTPException(status_code=404, detail="Pedido nao encontrado")

    item_existente = db.query(PedidoItensModel).filter(PedidoItensModel.produto_id == mesa.Itens[0].produto_id).first()

    if item_existente:
        item_existente.quantidade += mesa.Itens[0].quantidade
        db.commit()
        db.refresh(item_existente)

        mesa_response = MesasResponse.model_validate( {
            "id": mesa_existente.id,    
            "numero": mesa_existente.numero,
            "pedido": pedido_aberto
        })

        await notificar_todos({
            "tipo": "produto_em_mesa",
            "dados": jsonable_encoder(mesa_response)
        })

        return {
            "id": mesa_existente.id,
            "numero": mesa_existente.numero,
            "caixa_id": mesa_existente.caixa_id,
            "pedido": pedido_aberto
        }

    # pega o item enviado no request
    item_request = mesa.Itens[0]

    item = PedidoItensModel(
        produto_id=item_request.produto_id,
        quantidade=item_request.quantidade,
        valor_unitario=item_request.valor_unitario,
    )
    
    pedido_aberto.itens.append(item)

    # atualiza totais
    pedido_aberto.quantidade_itens += item.quantidade
    pedido_aberto.valor_total += item.quantidade * item.valor_unitario

    db.commit()
    db.refresh(pedido_aberto)


    mesa_response = MesasResponse.model_validate( {  
        "id": mesa_existente.id,    
        "numero": mesa_existente.numero,
        "pedido": pedido_aberto
    })

    await notificar_todos({
        "tipo": "produto_em_mesa",
        "dados": jsonable_encoder(mesa_response)
    })

    return {
        "id": mesa_existente.id,
        "numero": mesa_existente.numero,
        "caixa_id": mesa_existente.caixa_id,
        "pedido": pedido_aberto
    }

@router.put(
    "/finalizar-pedido-mesa/{mesa_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def fechar_mesa(mesa_id: int, db: Session = Depends(get_db)):

    mesa_existente = db.query(MesaModel).filter(
        MesaModel.id == mesa_id
    ).first()

    if not mesa_existente:
        raise HTTPException(status_code=404, detail="Mesa nao encontrada")

    pedido_aberto = db.query(PedidosMesaModel).filter(
        PedidosMesaModel.mesa_id == mesa_existente.id,
        PedidosMesaModel.status == "ABERTO"
    ).first()

    if not pedido_aberto:
        raise HTTPException(status_code=404, detail="Pedido nao encontrado")

    pedido_aberto.status = "FECHADO"
    db.commit()

@router.delete("/excluir-pedido-mesa/{mesa_id}", status_code=status.HTTP_204_NO_CONTENT)
async def excluir_pedido_mesa(mesa_id: int, db: Session = Depends(get_db)):

    mesa_existente = db.query(MesaModel).filter(
        MesaModel.id == mesa_id
    ).first()

    if not mesa_existente:
        raise HTTPException(status_code=404, detail="Mesa nao encontrada")

    pedido_aberto = db.query(PedidosMesaModel).filter(
        PedidosMesaModel.mesa_id == mesa_existente.id,
        PedidosMesaModel.status == "ABERTO"
    ).first()

    if not pedido_aberto:
        raise HTTPException(status_code=404, detail="Pedido nao encontrado")

    db.delete(pedido_aberto)
    db.commit()

@router.delete("/excluir-mesa/{mesa_id}", status_code=status.HTTP_204_NO_CONTENT)
async def excluir_mesa(mesa_id: int, db: Session = Depends(get_db)):

    mesa_existente = db.query(MesaModel).filter(
        MesaModel.id == mesa_id
    ).first()

    if not mesa_existente:
        raise HTTPException(status_code=404, detail="Mesa nao encontrada")
    

    db.delete(mesa_existente)
    db.commit()

    raise HTTPException(status_code=200, detail="Mesa excluida com sucesso")

@router.get("/em-atendimento", status_code=status.HTTP_200_OK)
async def mesas_em_atendimento(db: Session = Depends(get_db)):
    pedidos_abertos = db.query(PedidosMesaModel).filter(PedidosMesaModel.status == "ABERTO").all()

    if not pedidos_abertos:
        raise HTTPException(status_code=404, detail="Nenhum pedido em atendimento")

    mesas_em_atendimento = []

    for pedido in pedidos_abertos:
        mesa = db.query(MesaModel).filter(MesaModel.id == pedido.mesa_id).first()
        mesas_em_atendimento.append(mesa.numero)

    return mesas_em_atendimento