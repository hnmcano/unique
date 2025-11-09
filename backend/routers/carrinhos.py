from fastapi import APIRouter, Depends
import pandas as pd
from sqlalchemy.orm import Session
from sqlalchemy import update, select
from bd.connection import get_db
from typing import List, Dict
from models.carrinhos import Carrinho as CarrinhoModel
from schemas.carrinhos import Carrinho as CarrinhoSchema
from time import sleep

router = APIRouter()

@router.get("/carrinho")
async def read_products(db: Session = Depends(get_db)):
    db = db.query(CarrinhoModel).all()
    db = [p.__dict__ for p in db]
    dataframe = pd.DataFrame(db).drop(columns=["_sa_istance_state"], errors="ignore")
    
    if not dataframe.empty:
        dataframe["valor_total"] = dataframe["preco_venda"] * dataframe["quantidade"]

    dataframe = dataframe.to_dict(orient='records')

    return dataframe

@router.post("/postagem/{product_id}")
async def post_product(product_id: int, format: CarrinhoSchema, db: Session = Depends(get_db)):
    db_product = db.query(CarrinhoModel).filter(CarrinhoModel.cod_sistema == product_id).first()
    if not db_product:
        db_product = CarrinhoModel(**format.dict())
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return db_product

    db_product.quantidade = db_product.quantidade + 1
    db.commit()
    db.refresh(db_product)
    return db_product

@router.delete("/delete/{product_id}")
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

