from fastapi import APIRouter, Depends, HTTPException
from bd.connection import get_db
from sqlalchemy.orm import Session
from models.estabelecimento import Estabelecimento as EstabelecimentoModel
from schemas.estabelecimento import EstabelecimentoBase as Estabelecimentoschema


router = APIRouter()

@router.post("/desktop/add/estabelecimento")
def info_data_estabelecimento(dados_estabelecimento: Estabelecimentoschema, db: Session = Depends(get_db)):
    db_estabelecimento = EstabelecimentoModel(**dados_estabelecimento.dict())

    db.add(db_estabelecimento)
    db.commit()
    db.refresh(db_estabelecimento)
    return db_estabelecimento
