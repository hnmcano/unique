from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from bd.connection import get_db
from schemas.caixa import Caixa as CaixaSchema
from models.caixa import Caixa as CaixaModel
from models.pedidos import Pedido as PedidoModel
from datetime import datetime


router = APIRouter()

@router.get("/valid_box")
def valid_box(db: Session = Depends(get_db)):
    Caixa_aberto = db.query(CaixaModel).filter(CaixaModel.status == "ABERTO").first()

    if Caixa_aberto is not None:
        temporizador = Caixa_aberto.data_abertura
        diferenca = (temporizador - datetime.now()).total_seconds()
        raise HTTPException(status_code=200, detail=f"Ja existe um caixa aberto há {diferenca:.2f} segundos")
    else:
        raise HTTPException(status_code=400, detail="Nao existe um caixa aberto")


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