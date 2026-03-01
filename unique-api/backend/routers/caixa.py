from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.connection import get_db
from schemas.caixa import Caixa as CaixaSchema
from models.caixa import Caixa as CaixaModel
from models.pedidos import Pedido as PedidoModel
from service.depencias import get_current_user
from datetime import datetime
from zoneinfo import ZoneInfo


router = APIRouter()

fuso_brasil = ZoneInfo("America/Sao_Paulo")

@router.get("/valid_box")
def valid_box(db: Session = Depends(get_db), user_current: dict = Depends(get_current_user)):
    Caixa_aberto = db.query(CaixaModel).filter(CaixaModel.status == "ABERTO", CaixaModel.estabelecimento_id == user_current["estabelecimento_id"]).first()

    if not Caixa_aberto:
        raise HTTPException(status_code=400, detail="Nenhum caixa aberto no momento")
    
    data_abertura_br = Caixa_aberto.data_abertura.astimezone(fuso_brasil)
    agora_brasil = datetime.now(fuso_brasil)
    diferenca = agora_brasil - data_abertura_br

    horas, resto = divmod(int(diferenca.total_seconds()), 3600)
    minutos, segundos = divmod(resto, 60)

    tempo_aberto = f"{horas:02d}:{minutos:02d}:{segundos:02d}"

    raise HTTPException(
        status_code=200,
        detail=f"{tempo_aberto}",
    )


@router.post("/open_box")
def open_box(caixa: CaixaSchema, db: Session = Depends(get_db), user_current: dict = Depends(get_current_user)):

    if db.query(CaixaModel).filter(CaixaModel.status == "ABERTO", CaixaModel.estabelecimento_id == user_current["estabelecimento_id"]).first():
        raise HTTPException(status_code=400, detail="Ja existe um caixa aberto")

    db_caixa = CaixaModel(**caixa.dict())
    db_caixa.estabelecimento_id = user_current["estabelecimento_id"]
    db.add(db_caixa)
    db.commit()
    db.refresh(db_caixa)
    return db_caixa


@router.get("/close_box")
def close_box(db: Session = Depends(get_db), user_current: dict = Depends(get_current_user)):
    caixa_aberto = db.query(CaixaModel).filter(CaixaModel.status == "ABERTO", CaixaModel.estabelecimento_id == user_current["estabelecimento_id"]).first()
    produtos_pendentes = db.query(PedidoModel).filter(PedidoModel.status == "PENDENTE" and PedidoModel.caixa_id == caixa_aberto.id, PedidoModel.estabelecimento_id == user_current["estabelecimento_id"]).first() 

    if caixa_aberto and not produtos_pendentes:
        caixa_aberto.status = "FECHADO"
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