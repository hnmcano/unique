from schemas.produtos import Categoria as CategoriaSchema
from models.produtos import Categoria as CategoryModel
from models.produtos import Produto as ProductModel

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from bd.connection import get_db
from sqlalchemy import join
from time import sleep
import pandas as pd
import base64

router = APIRouter()

# Rotas para inserir categorias ao banco de dados, com a validação do Pydantic, baseado no envio do desktop
@router.post("/category")
async def get_category(categoria: CategoriaSchema, db: Session = Depends(get_db)):
    db_category = db.query(CategoryModel).filter(CategoryModel.nome == categoria.nome).first()

    if db_category:
        raise HTTPException(status_code=400, detail="Categoria ja cadastrada")
    
    db_category = CategoryModel(**categoria.dict())

    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

# Rota para listar todas as categorias no dropdown estabelecido no desktop na aba produtos
@router.get("/dropdown/categories")
async def read_categories(db: Session = Depends(get_db)):
    return db.query(CategoryModel).all()

# Rota para excluir categoria pelo id com base no dropdown estabelecido no desktop
@router.delete("/category/{category_id}")
async def delete_category(category_id: str, db: Session = Depends(get_db)):
    db_category = db.query(CategoryModel).filter(CategoryModel.nome == category_id).first()
    if db_category:
        db.delete(db_category)
        db.commit()
        return {"message": "Categoria excluída com sucesso"}
    return {"message": "Categoria não encontrada"}

# Rota para filtrar categoria pelo id e retornar ao front-end com react
@router.get("/category/filter/{category_id}")
async def filter_category(category_id: str, db: Session = Depends(get_db)):
    return db.query(ProductModel).filter(ProductModel.categoria == category_id).all()

