from fastapi import APIRouter, Depends
import pandas as pd
from sqlalchemy.orm import Session
from sqlalchemy import update, select
from bd.connection import get_db
from typing import List, Dict
from models.carrinhos import Carrinho as CarrinhoModel
from schemas.carrinhos import Carrinho as CarrinhoSchema
from schemas.carrinhos import CarrinhoUpdate as CarrinhoUpdateSchema

router = APIRouter()

@router.get("/carrinho")
async def read_products(db: Session = Depends(get_db)):
    db = db.query(CarrinhoModel).all()
    db = [p.__dict__ for p in db]
    dataframe = pd.DataFrame(db).drop(columns=["_sa_istance_state"], errors="ignore")
    if not dataframe.empty:
        dataframe["valor_total"] = dataframe["preco_venda"] * dataframe["quantidade"]

    qtdprodutos = dataframe["cod_sistema"].count().item() if not dataframe.empty else 0
    dataframe = dataframe.to_dict(orient='records')

    return {"dataframe": dataframe, "qtdprodutos": qtdprodutos}

@router.delete("/delete/all")
async def delete_all(db: Session = Depends(get_db)):
    db.query(CarrinhoModel).delete()
    db.commit()
    return {"message": "Carrinho excluido com sucesso"}

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

        db = db.query(CarrinhoModel).all()
        db = [p.__dict__ for p in db]
        dataframe = pd.DataFrame(db).drop(columns=["_sa_istance_state"], errors="ignore")

        qtdprodutos = dataframe["cod_sistema"].count().item() if not dataframe.empty else 0

        return {"qtdprodutos": qtdprodutos}
    
    return {"message": "Produto nao encontrado"}


@router.put("/atualizar/quantidade/{product_id}/{quantidade}")
async def update_product(product_id: int, quantidade: int, db: Session = Depends(get_db)):
    db_product = db.query(CarrinhoModel).filter(CarrinhoModel.cod_sistema == product_id).first()
    if db_product:
        db_product.quantidade = quantidade
        db.commit()
        return {"message": "Produto atualizado com sucesso"}
    return {"message": "Produto nao encontrado"}

