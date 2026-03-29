<<<<<<< HEAD
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.connection import get_db
from schemas.usuarios import Usuarios as UsuariosSchema
from models.usuarios import Usuarios as UsuariosModel
from auth.security import autenticar_usuario
from jose import jwt
from datetime import datetime, timedelta
from core.config import settings
import os
from service.depencias import get_current_user

router = APIRouter()

def create_acess_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.ACESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

@router.post("/login", status_code=status.HTTP_200_OK)
def Login_user(user: UsuariosSchema, db: Session = Depends(get_db)):
    usuario = autenticar_usuario(user.email, user.senha_hash, db)

    if not usuario:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    token = create_acess_token(
        data= {
            "sub": str(usuario.id),
            "estabelecimento_id": str(usuario.estabelecimento_id)
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer",
    }

=======
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.connection import get_db
from schemas.usuarios import Usuarios as UsuariosSchema
from models.usuarios import Usuarios as UsuariosModel
from schemas.usuarios import UsuariosResponse
from auth.security import autenticar_usuario
from service.depencias import get_current_user
from jose import jwt
from datetime import datetime, timedelta
from core.config import settings
import os
from service.depencias import get_current_user

router = APIRouter()

def create_acess_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.ACESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

@router.post("/login", status_code=status.HTTP_200_OK)
def Login_user(user: UsuariosSchema, db: Session = Depends(get_db)):
    usuario = autenticar_usuario(user.email, user.senha_hash, db)

    if not usuario:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    token = create_acess_token(
        data= {
            "sub": str(usuario.id),
            "estabelecimento_id": str(usuario.estabelecimento_id)
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer",
    }

@router.get("/dados", status_code=status.HTTP_200_OK)
def dados_usuario(db: Session = Depends(get_db), user_current: dict = Depends(get_current_user)):
    usuario_existente = db.query(UsuariosModel).filter(UsuariosModel.estabelecimento_id == user_current["estabelecimento_id"], UsuariosModel.ativo == True).first()
    
    if not usuario_existente:
        raise HTTPException(status_code=400, detail="Usuario não cadastrado na base de dados!")

    return {
        "id": usuario_existente.id,
        "nome": usuario_existente.nome,
        "email": usuario_existente.email,
        "status": usuario_existente.ativo,
        "criado_em": usuario_existente.criado_em
    }
>>>>>>> 182d746 (Versão atual da infra com backend da VM)
