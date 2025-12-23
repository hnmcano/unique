from fastapi import APIRouter, Depends, HTTPException
from bd.connection import get_db
from sqlalchemy.orm import Session
from models.estabelecimento import Estabelecimento as EstabelecimentoModel
from schemas.estabelecimento import EstabelecimentoBase as Estabelecimentoschema


router = APIRouter()

@router.post("/desktop/add")
def info_data_estabelecimento(dados_estabelecimento: Estabelecimentoschema, db: Session = Depends(get_db)):
    db_estabelecimento = EstabelecimentoModel(**dados_estabelecimento.dict())

    db_estabelecimento_valid = db.query(EstabelecimentoModel).filter(EstabelecimentoModel.nome == dados_estabelecimento.nome).first()

    if db_estabelecimento_valid:
        raise HTTPException(status_code=400, detail="Estabelecimento já cadastrado")

    db.add(db_estabelecimento)
    db.commit()
    db.refresh(db_estabelecimento)
    return db_estabelecimento


@router.put("/desktop/update/{estabelecimento_nome}")
def update_estabelecimento(estabelecimento_nome: str, dados_estabelecimento: Estabelecimentoschema, db: Session = Depends(get_db)):
    db_estabelecimento = db.query(EstabelecimentoModel).filter(EstabelecimentoModel.nome == estabelecimento_nome).first()

    for key, value in dados_estabelecimento.dict().items():
        setattr(db_estabelecimento, key, value)

    db.commit()
    db.refresh(db_estabelecimento)
    return db_estabelecimento

@router.get("/react/catalago")
def get_estabelecimento( db: Session = Depends(get_db)):
    db_estabelecimento = db.query(EstabelecimentoModel).all()
    if not db_estabelecimento:
        raise HTTPException(status_code=404, detail="Estabelecimento não encontrado")
    
    return db_estabelecimento