from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from back_end.bd.connection import get_db
from back_end.schemas.users import User as UserSchema
from back_end.models.users import User as UserModel


router = APIRouter()

@router.post("/users")
def create_user(user: UserSchema, db: Session = Depends(get_db)):
    db_user = UserModel(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user