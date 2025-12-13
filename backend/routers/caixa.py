from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from bd.connection import get_db
from schemas.caixa import Caixa as CaixaSchema
from models.caixa import Caixa as CaixaModel

router = APIRouter()

@router.post("/open_box")
def open_box(caixa: CaixaSchema, db: Session = Depends(get_db)):
    db_caixa = CaixaModel(**caixa.dict())
    db.add(db_caixa)
    db.commit()
    db.refresh(db_caixa)
    return db_caixa
