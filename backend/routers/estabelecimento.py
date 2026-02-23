from fastapi import APIRouter, Depends, HTTPException
from database.connection import get_db
import pandas as pd
from sqlalchemy.orm import Session
from models.estabelecimento import Estabelecimento as EstabelecimentoModel
from schemas.estabelecimento import EstabelecimentoBase as Estabelecimentoschema
from models.usuarios import Usuarios as UsuariosModel
from auth.security import gerar_hash


router = APIRouter()

@router.post("/info_estabelecimento")
async def info_data_estabelecimento(dados_estabelecimento: Estabelecimentoschema, db: Session = Depends(get_db)):
    bd_estabelecimento = EstabelecimentoModel(
            nome=dados_estabelecimento.nome,
            nome_fantasia=dados_estabelecimento.nome_fantasia,
            documento=dados_estabelecimento.documento,
            telefone=dados_estabelecimento.telefone,
            email=dados_estabelecimento.email
    )

    db.add(bd_estabelecimento)
    db.flush()

    senha_hash = gerar_hash(dados_estabelecimento.senha)

    bd_usuario = UsuariosModel(
        estabelecimento_id=bd_estabelecimento.id,
        nome="Admin",
        email=bd_estabelecimento.email,
        senha_hash=senha_hash,
    )

    db.add(bd_usuario)

    db.commit()
