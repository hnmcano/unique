from fastapi import APIRouter, Depends, HTTPException
from bd.connection import get_db
import pandas as pd
from sqlalchemy.orm import Session
from models.estabelecimento import Estabelecimento as EstabelecimentoModel
from schemas.estabelecimento import EstabelecimentoBase as Estabelecimentoschema

router = APIRouter()

@router.post("/desktop/add")
async def info_data_estabelecimento(dados_estabelecimento: Estabelecimentoschema, db: Session = Depends(get_db)):
    db_estabelecimento = EstabelecimentoModel(**dados_estabelecimento.dict())

    db_estabelecimento_valid = db.query(EstabelecimentoModel).filter(EstabelecimentoModel.nome == dados_estabelecimento.nome).first()

    if db_estabelecimento_valid:
        raise HTTPException(status_code=400, detail="Estabelecimento já cadastrado")

    db.add(db_estabelecimento)
    db.commit()
    db.refresh(db_estabelecimento)
    return db_estabelecimento


@router.put("/desktop/update/{estabelecimento_nome}")
async def update_estabelecimento(estabelecimento_nome: str, dados_estabelecimento: Estabelecimentoschema, db: Session = Depends(get_db)):
    db_estabelecimento = db.query(EstabelecimentoModel).filter(EstabelecimentoModel.nome == estabelecimento_nome).first()

    for key, value in dados_estabelecimento.dict().items():
        setattr(db_estabelecimento, key, value)

    db.commit()
    db.refresh(db_estabelecimento)
    return db_estabelecimento

@router.get("/react/catalago")
async def get_estabelecimento(db: Session = Depends(get_db)):

    db_estabelecimento = db.query(EstabelecimentoModel).all()
    dados_estabelecimento = pd.DataFrame([db_estabelecimento.__dict__])
    dados_estabelecimento = dados_estabelecimento.drop(columns=["_sa_instance_state"], errors="ignore")
    dados_estabelecimento = dados_estabelecimento.to_dict("records")

    print(dados_estabelecimento)

    if not db_estabelecimento:
        raise HTTPException(status_code=404, detail="Estabelecimento não encontrado")
    
    return dados_estabelecimento