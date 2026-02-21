from fastapi import APIRouter, Depends, HTTPException
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

@router.post("/login")
def create_user(user: UsuariosSchema, db: Session = Depends(get_db)):
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

@router.get("/me")
def me(usuario = Depends(get_current_user)):
    return usuario