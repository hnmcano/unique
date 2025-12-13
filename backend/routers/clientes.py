from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from bd.connection import get_db
from schemas.clientes import Clientes as ClientesSchema
from models.clientes import Clientes as ClientesModel

router = APIRouter()

# Rotas para inserir usuários ao banco de dados, com a validação do Pydantic
@router.post("/users")
def create_user(user: ClientesSchema, db: Session = Depends(get_db)):
    db_user = ClientesModel(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user