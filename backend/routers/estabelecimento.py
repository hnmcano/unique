from models.estabelecimento import Estabelecimento as EstabelecimentoModel
from models.estabelecimento import HorariosFuncionamento
from models.caixa import Caixa as CaixaModel
from models.produtos import Produto as ProductModel
from models.usuarios import Usuarios as UsuariosModel
from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from service.websocketservice import notificar_todos
from sqlalchemy.orm import Session
from database.connection import get_db
from sqlalchemy import join
from datetime import datetime, time, timedelta
from time import sleep
from typing import List
import pandas as pd
import base64
from service.depencias import get_current_user
from core.dependencies.tenant import get_estabelecimento
from fastapi import HTTPException, Header
from schemas.estabelecimento import EstabelecimentoBase as Estabelecimentoschema
from schemas.estabelecimento import EstabelecimentoSchemaAtualizar as EstabelecimentoSchemaAtualizar
from schemas.estabelecimento import AtualizacaoHorarios, HorariosFuncionamentoResponse
from schemas.estabelecimento import EstabelecimentoResponse
from auth.security import autenticar_usuario, gerar_hash
from service.websocketservice import estabelecimento_esta_online

from uuid import UUID

router = APIRouter()

def dicionario_dias_semana(dia_semana):
    dicionario = {
        "segunda-feira": 0,
        "terca-feira": 1,
        "quarta-feira": 2,
        "quinta-feira": 3,
        "sexta-feira": 4,
        "sabado": 5,
        "domingo":6,
    }

    return dicionario.get(dia_semana.lower())

def dentro_do_horario(horarios):
    agora = datetime.now() - timedelta(hours=3)
    dia_semana = agora.weekday()
    hora_atual = agora.time() 

    for h in horarios:
        if h.dia_semana == dia_semana:
            if h.hora_abertura <= hora_atual <= h.hora_fechamento:
                return True

    return False

@router.get("/carregar-dados")
async def carregar_dados(
    db: Session = Depends(get_db),
    x_tenant_estabelecimento: EstabelecimentoModel = Depends(get_estabelecimento)
):

    online_ws = estabelecimento_esta_online(x_tenant_estabelecimento.id)

    caixa_existente = db.query(CaixaModel).filter(
        CaixaModel.estabelecimento_id == x_tenant_estabelecimento.id,
        CaixaModel.status == "ABERTO"
    ).first()

    horarios = db.query(HorariosFuncionamento).filter(
        HorariosFuncionamento.estabelecimento_id == x_tenant_estabelecimento.id
    ).all()

    horario_ok = dentro_do_horario(horarios)

    print(horario_ok)

    online = False

    if online_ws == True and caixa_existente and horario_ok:
        online = True

    estabelecimento = {
        "nome": x_tenant_estabelecimento.nome,
        "nome_fantasia": x_tenant_estabelecimento.nome_fantasia,
        "telefone": x_tenant_estabelecimento.telefone,
        "logo_img": x_tenant_estabelecimento.logo_img,
        "endereco": x_tenant_estabelecimento.endereco,
        "rede_social": x_tenant_estabelecimento.rede_social,
        "descricao": x_tenant_estabelecimento.descricao,
        "cor_layout": x_tenant_estabelecimento.cor_layout,
        "online": online,
        "horarios": jsonable_encoder(horarios)
    }

    return estabelecimento

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
        db_estabelecimento.descricao = estabelecimento.descricao
        db_estabelecimento.cor_layout = estabelecimento.cor_layout
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

@router.post("/horarios", response_model=List[HorariosFuncionamentoResponse])
async def horarios_estabelecimento(dados: AtualizacaoHorarios, db: Session = Depends(get_db), user_current: dict = Depends(get_current_user)):
    dia_da_semana = dicionario_dias_semana(dados.dia_semana)
    horario_abertura = datetime.strptime(dados.horario_inicio, "%H:%M")
    horario_fechamento = datetime.strptime(dados.horario_final, "%H:%M")
    horarios_ativo = db.query(HorariosFuncionamento).filter(HorariosFuncionamento.estabelecimento_id == user_current["estabelecimento_id"], HorariosFuncionamento.dia_semana == dia_da_semana).first()

    if horarios_ativo:
        raise HTTPException(status_code=400, detail="Horario já foi estabelecido!")

    horarios_funcionamento = HorariosFuncionamento(
        estabelecimento_id=user_current["estabelecimento_id"],
        dia_semana=dia_da_semana,
        hora_abertura=horario_abertura.time(),
        hora_fechamento=horario_fechamento.time()
    )
    
    db.add(horarios_funcionamento)
    db.commit()

    horarios = db.query(HorariosFuncionamento).filter(HorariosFuncionamento.estabelecimento_id == user_current["estabelecimento_id"])
    estabelecimento_id = UUID(user_current["estabelecimento_id"])

    print(estabelecimento_id)
    print(type(estabelecimento_id))

    horarios_funcionamento = horarios.order_by(HorariosFuncionamento.dia_semana.asc()).all()

    await notificar_todos(estabelecimento_id,{
        "tipo": "horario_criado",
        "dados": jsonable_encoder(horarios_funcionamento)
    })

    return horarios_funcionamento

@router.delete("/horarios-delete/{id_horario}")
async def deletar_horario(id_horario: UUID, db: Session = Depends(get_db), user_current: dict = Depends(get_current_user)):
    horario_definido = db.query(HorariosFuncionamento).filter(HorariosFuncionamento.estabelecimento_id == user_current["estabelecimento_id"], HorariosFuncionamento.id_horarios_func == id_horario).first()

    if not horario_definido:
        raise HTTPException(status_code=403, detail="horario ainda não foi definido!")

    db.delete(horario_definido)
    db.commit()
    
@router.get("/horarios", response_model=List[HorariosFuncionamentoResponse])
async def gerar_horarios(db: Session = Depends(get_db), user_current: dict = Depends(get_current_user)):
    horarios = db.query(HorariosFuncionamento).filter(HorariosFuncionamento.estabelecimento_id == user_current["estabelecimento_id"]).all()

    if not horarios:
        return []

    return horarios
>>>>>>> 182d746 (Versão atual da infra com backend da VM)
