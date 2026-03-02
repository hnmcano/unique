from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.connection import get_db
from schemas.clientes import Clientes as ClientesSchema
from models.clientes import Clientes as ClientesModel
from service.depencias import get_current_user

router = APIRouter()

# Rotas para inserir usuários ao banco de dados, com a validação do Pydantic
@router.post("/users")
def create_user(user: ClientesSchema, db: Session = Depends(get_db), user_current: dict = Depends(get_current_user)):
    db_user = ClientesModel(**user.dict())
    db_user.estabelecimento_id = user_current["estabelecimento_id"]
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db), user_current: dict = Depends(get_current_user)):
    db_user = db.query(ClientesModel).filter(ClientesModel.id == user_id, ClientesModel.estabelecimento_id == user_current["estabelecimento_id"]).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return {"message": "Usuário excluido com sucesso"}
    return {"message": "Usuário nao encontrado"}