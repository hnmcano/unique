from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import func, case
from database.connection import get_db
from schemas.caixa import Caixa as CaixaSchema
from schemas.caixa import CaixaResponse
from models.caixa import Caixa as CaixaModel
from models.pedidos import Pedido as PedidoModel
from service.depencias import get_current_user
from datetime import datetime
from zoneinfo import ZoneInfo
from uuid import UUID

router = APIRouter()

@router.get("/valid_box", status_code=status.HTTP_200_OK, response_model=CaixaResponse)
def valid_box(db: Session = Depends(get_db), user_current: dict = Depends(get_current_user)):
    Caixa_aberto = db.query(CaixaModel).filter(CaixaModel.status == "ABERTO", CaixaModel.estabelecimento_id == user_current["estabelecimento_id"]).first()

    if not Caixa_aberto:
        raise HTTPException(status_code=400, detail="Nenhum caixa aberto no momento")

    db_caixa = CaixaResponse.model_validate(Caixa_aberto)

    return db_caixa

@router.post("/open_box", response_model=CaixaResponse)
def open_box(caixa: CaixaSchema, db: Session = Depends(get_db), user_current: dict = Depends(get_current_user)):

    db_caixa = db.query(CaixaModel).filter(CaixaModel.status == "ABERTO", CaixaModel.estabelecimento_id == user_current["estabelecimento_id"]).first()

    if db_caixa:
        raise HTTPException(status_code=400, detail="Ja existe um caixa aberto")

    abrir_caixa = CaixaModel(
        valor_inicial=caixa.valor_inicial,
        estabelecimento_id = user_current["estabelecimento_id"]
    )

    db.add(abrir_caixa)
    db.commit()
    db.refresh(abrir_caixa)

    db_caixa = db.query(CaixaModel).filter(CaixaModel.status == "ABERTO", CaixaModel.estabelecimento_id == user_current["estabelecimento_id"]).first()

    caixa = CaixaResponse.model_validate(db_caixa)

    return caixa

@router.get("/close_box")
def close_box(db: Session = Depends(get_db), user_current: dict = Depends(get_current_user)):
    caixa_aberto = db.query(CaixaModel).filter(CaixaModel.status == "ABERTO", CaixaModel.estabelecimento_id == user_current["estabelecimento_id"]).first()
    pedidos_pendentes = db.query(PedidoModel).filter(
        PedidoModel.status != "FINALIZADO", 
        PedidoModel.caixa_id == caixa_aberto.id, 
        PedidoModel.estabelecimento_id == user_current["estabelecimento_id"]
    ).first() 

    print(caixa_aberto)
    print(pedidos_pendentes)

    if caixa_aberto and not pedidos_pendentes:
        caixa_aberto.status = "FECHADO"
        caixa_aberto.data_fechamento = datetime.utcnow()
        db.commit()
        raise HTTPException(status_code=200, detail="Caixa fechado com sucesso")
    else:
        raise HTTPException(status_code=400, detail="Existem pedidos pendentes no caixa, finalize-os antes de fechar o caixa")
    
@router.get("/react/get_caixa")
def get_caixa(db: Session = Depends(get_db), user_current: dict = Depends(get_current_user)):
    caixa_aberto = db.query(CaixaModel).filter(CaixaModel.status == "ABERTO", CaixaModel.estabelecimento_id == user_current["estabelecimento_id"]).first()

    if not caixa_aberto:
        return {
            "status": "Fechado",
            "messagem" : "Estamos Fechados no momento, volte mais tarde"
            }

    return {"message": "Caixa aberto"}

@router.delete("/desktop/delete-caixa/{id_caixa}")
def deletando_caixa(id_caixa: UUID, db: Session = Depends(get_db), user_current: dict = Depends(get_current_user)):
    caixa_aberto = db.query(CaixaModel).filter(CaixaModel.status == "FECHADO", CaixaModel.estabelecimento_id == user_current["estabelecimento_id"], CaixaModel.id == id_caixa).first()

    db.delete(caixa_aberto)
    db.commit()

@router.get("/desktop/carregar-tabela")
def carregamento_caixa(db: Session = Depends(get_db), user_current: dict = Depends(get_current_user)):
    opcao_pagamento_ajustada = case(
        (
            PedidoModel.metodo_pagamento == "dinheiro",
            "DINHEIRO"
        ),
            else_=PedidoModel.opcoes_pagamento
    )


    result = (
        db.query(
            CaixaModel.id.label("caixa_id"),
            CaixaModel.data_abertura,
            PedidoModel.metodo_pagamento,
            opcao_pagamento_ajustada.label("opcoes_pagamento"),
            func.sum(PedidoModel.valor_total).label("total")
        )
        .join(PedidoModel, PedidoModel.caixa_id == CaixaModel.id)
        .group_by(
            CaixaModel.id,
            CaixaModel.data_abertura,
            PedidoModel.metodo_pagamento,
            opcao_pagamento_ajustada
        )
        .filter(CaixaModel.status == "ABERTO")
        .all()
    )

    if not result:
        return []

    return [
        {
            "id_caixa": i.caixa_id,
            "data_abertura": i.data_abertura,
            "forma_pagamento": i.metodo_pagamento,
            "bandeira": i.opcoes_pagamento,
            "total": float(i.total)
        }
        for i in result
    ]
>>>>>>> 182d746 (Versão atual da infra com backend da VM)
