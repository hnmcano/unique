from models.estabelecimento import Estabelecimento as EstabelecimentoModel
from models.produtos import Produto as ProductModel
from models.usuarios import Usuarios as UsuariosModel

from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from service.websocketservice import notificar_todos
from sqlalchemy.orm import Session
from database.connection import get_db
from sqlalchemy import join
from time import sleep
import pandas as pd
import base64
from service.depencias import get_current_user
from core.dependencies.tenant import get_estabelecimento
from fastapi import HTTPException, Header

from schemas.estabelecimento import EstabelecimentoBase as Estabelecimentoschema
from schemas.estabelecimento import EstabelecimentoSchemaAtualizar as EstabelecimentoSchemaAtualizar
from schemas.estabelecimento import EstabelecimentoResponse

from auth.security import autenticar_usuario, gerar_hash


from uuid import UUID


router = APIRouter()

@router.get("/carregar-dados", response_model=EstabelecimentoResponse)
async def carregar_dados( db: Session = Depends(get_db), x_tenant_estabelecimento: EstabelecimentoModel = Depends(get_estabelecimento)):
    return x_tenant_estabelecimento


@router.put("/atualizar-infos", response_model=EstabelecimentoResponse)
async def atualizar_estabelecimento(estabelecimento: EstabelecimentoSchemaAtualizar, db: Session = Depends(get_db), user_current: dict = Depends(get_current_user)):
    db_estabelecimento = db.query(EstabelecimentoModel).filter(EstabelecimentoModel.id == user_current["estabelecimento_id"]).first()

    if db_estabelecimento:
        db_estabelecimento.nome = estabelecimento.nome
        db_estabelecimento.nome_fantasia = estabelecimento.nome_fantasia
        db_estabelecimento.telefone = estabelecimento.telefone
        db_estabelecimento.email = estabelecimento.email
        db_estabelecimento.logo_img = estabelecimento.logo_img
        db_estabelecimento.endereco = estabelecimento.endereco
        db_estabelecimento.plano = estabelecimento.plano
        db_estabelecimento.limite_usuarios = estabelecimento.limite_usuarios
        db_estabelecimento.rede_social = estabelecimento.rede_social
        db_estabelecimento.subdominio = estabelecimento.subdominio
        db.commit()
        db.flush()
    
    estabelecimento_id=user_current["estabelecimento_id"]

    estabelecimento_serializado = EstabelecimentoResponse.model_validate(db_estabelecimento)

    await notificar_todos(estabelecimento_id,{
        "tipo": "Atualizar_estabelecimento",
        "dados": jsonable_encoder(estabelecimento_serializado)
    })

    return estabelecimento_serializado


@router.get("/carregar-infos", response_model=EstabelecimentoResponse)
async def get_estabelecimento( db: Session = Depends(get_db), user_current: dict = Depends(get_current_user)):
    estabelecimento = db.query(EstabelecimentoModel).filter(EstabelecimentoModel.id == user_current["estabelecimento_id"]).first()
    return estabelecimento


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

    return bd_estabelecimento