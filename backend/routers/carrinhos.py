from fastapi import APIRouter, Depends
import pandas as pd
from sqlalchemy.orm import Session
from sqlalchemy import update, select
from bd.connection import get_db
from typing import List, Dict
from models.carrinhos import Carrinho as CarrinhoModel
from schemas.carrinhos import Carrinho as CarrinhoSchema

router = APIRouter()

@router.get("/carrinho")
async def read_products(db: Session = Depends(get_db)):
    return db.query(CarrinhoModel).all()


@router.post("/postagem/{product_id}")
async def post_product(product: CarrinhoSchema, db: Session = Depends(get_db)):
    productexist = db.execute(
        CarrinhoModel).filter(
            CarrinhoModel.cod_sistema == product.cod_sistema).scalar_one_or_none()
    
    if productexist:
        return {"message": "Produto ja cadastrado"}
    
    else:
        db_product = CarrinhoModel(**product.dict())
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return db_product

@router.delete("/carrinho/{product_id}")
async def delete_product(product_id: str, db: Session = Depends(get_db)):
    db_carrinho = db.query(CarrinhoModel).filter(CarrinhoModel.cod_sistema == product_id).first()
    if db_carrinho:
        db.delete(db_carrinho)
        db.commit()
        return {"message": "Produto excluído com sucesso"}
    return {"message": "Produto nao encontrado"}


@router.put("/carrinho")
async def update_product(product: CarrinhoSchema, db: Session = Depends(get_db)):
    db_product = db.query(CarrinhoModel).filter(CarrinhoModel.cod_sistema == product.cod_sistema).first()
    if db_product:
        db_product.preco = product.preco
        db_product.quantidade = product.quantidade
        db.commit()
        return {"message": "Produto atualizado com sucesso"}
    return {"message": "Produto nao encontrado"}

