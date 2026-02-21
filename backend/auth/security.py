from passlib.context import CryptContext
from database.connection import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
from models.usuarios import Usuarios

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def gerar_hash(senha):
    return pwd_context.hash(senha)

def verifica_senha(senha_digitada, senha_hash: str):
    return pwd_context.verify(senha_digitada, senha_hash)

def autenticar_usuario(email: str, senha: str, db: Session = Depends(get_db)):
    usuario = db.query(Usuarios).filter(Usuarios.email == email).first()
    if not usuario:
        return False
    
    if not verifica_senha(senha, usuario.senha_hash):
        return False
    
    if not usuario.ativo:
        return False
    
    return usuario