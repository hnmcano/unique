from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from bd.connection import get_db
from schemas.caixa import Caixa as CaixaSchema
from models.caixa import Caixa as CaixaModel
from models.pedidos import Pedido as PedidoModel
from datetime import datetime
from zoneinfo import ZoneInfo


router = APIRouter()

fuso_brasil = ZoneInfo("America/Sao_Paulo")


@router.get("/valid_box")
def valid_box(db: Session = Depends(get_db)):
    Caixa_aberto = db.query(CaixaModel).filter(CaixaModel.status == "ABERTO").first()

    if not Caixa_aberto:
        raise HTTPException(status_code=400, detail="Nenhum caixa aberto no momento")
    

    data_abertura_br = Caixa_aberto.data_abertura.astimezone(fuso_brasil)
    agora_brasil = datetime.now(fuso_brasil)
    diferenca = agora_brasil - data_abertura_br

    horas, resto = divmod(int(diferenca.total_seconds()), 3600)
    minutos, segundos = divmod(resto, 60)

    tempo_aberto = f"{horas:02d}:{minutos:02d}:{segundos:02d}"

    raise HTTPException(
        status_code=409,
        detail=f"{tempo_aberto}",
    )


@router.post("/open_box")
def open_box(caixa: CaixaSchema, db: Session = Depends(get_db)):

    if db.query(CaixaModel).filter(CaixaModel.status == "ABERTO").first():
        raise HTTPException(status_code=400, detail="Ja existe um caixa aberto")

    db_caixa = CaixaModel(**caixa.dict())
    db.add(db_caixa)
    db.commit()
    db.refresh(db_caixa)
    return db_caixa


@router.get("/close_box")
def close_box(db: Session = Depends(get_db)):
    caixa_aberto = db.query(CaixaModel).filter(CaixaModel.status == "ABERTO").first()
    produtos_pendentes = db.query(PedidoModel).filter(PedidoModel.status == "PENDENTE" and PedidoModel.caixa_id == caixa_aberto.id).first() 

    if caixa_aberto and not produtos_pendentes:
        caixa_aberto.status = "FECHADO"
        db.commit()
        return {"message": "Caixa fechado com sucesso"}
    else:
        raise HTTPException(status_code=400, detail="Existem pedidos pendentes no caixa, finalize-os antes de fechar o caixa")
    

@router.get("/react/get_caixa")
def get_caixa(db: Session = Depends(get_db)):
    caixa_aberto = db.query(CaixaModel).filter(CaixaModel.status == "ABERTO").first()

    if not caixa_aberto:
        return {
            "status": "Fechado",
            "messagem" : "Estamos Fechados no momento, volte mais tarde"
            }

    return {"message": "Caixa aberto"}