from fastapi import APIRouter, Depends, HTTPException
from database.connection import get_db
import pandas as pd
from sqlalchemy.orm import Session
from models.estabelecimento import Estabelecimento as EstabelecimentoModel
from schemas.estabelecimento import EstabelecimentoBase as Estabelecimentoschema

router = APIRouter()

@router.post("/desktop/add")
async def info_data_estabelecimento(dados_estabelecimento: Estabelecimentoschema, db: Session = Depends(get_db)):
    bd_estabelecimento = EstabelecimentoModel(**dados_estabelecimento.dict())
    db.add(bd_estabelecimento)
    db.commit()
    db.refresh(bd_estabelecimento)
    return bd_estabelecimento
