from models.produtos import Produto as ProductModel
from schemas.produtos import Produto as ProdutoSchema
from models.produtos import Categoria as CategoryModel

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from bd.connection import get_db
from sqlalchemy import join
from time import sleep
import pandas as pd
import base64

router = APIRouter()

########################################### PRODUTOS ################################################

# Rotas para inserir produtos ao banco de dados, com a validação do Pydantic, baseado no envio do desktop
@router.post("/desktop/add/product")
async def get_product(product: ProdutoSchema, db: Session = Depends(get_db)):
    db_product = ProductModel(**product.dict())

    if db_product.imagem is None:
        with open("backend/static/default_product.png", "rb") as image_file:
            image_data = image_file.read()
            encoded_image = base64.b64encode(image_data).decode("utf-8")
            db_product.imagem_name = "default.png"
            db_product.imagem = encoded_image


    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


# Rota para popular tabela de produtos disponivel no desktop na aba produtos
@router.get("/desktop/table")
async def read_products(db: Session = Depends(get_db)):
    produtos = db.query(ProductModel).all()
    categorias = db.query(CategoryModel).all()


    if not produtos:
        return []

    categorias_map = {
        c.id: c.nome for c in categorias
    }

    data = []

    for p in produtos:

        nome_categoria = categorias_map.get(p.categoria_id, "Sem categoria")

        produto = {
            "id": p.id,
            "categoria_id": p.categoria_id,
            "cod_pdv": p.cod_pdv,
            "nome": p.nome,
            "preco_custo": p.preco_custo,
            "preco_venda": p.preco_venda,
            "medida": p.medida,
            "estoque": p.estoque,
            "estoque_min": p.estoque_min,
            "descricao": p.descricao,
            "ficha_tecnica": p.ficha_tecnica,
            "status_venda": p.status_venda,
            "imagem_name": p.imagem_name,
            "imagem": p.imagem
        }

        produto["nome_categoria"] = nome_categoria
        data.append(produto)

    return data


# Rota para listar todos os produtos com os nomes das categorias no front-end com react
@router.get("/react/catalago")
async def list_products(db: Session = Depends(get_db)):

    produtos = db.query(ProductModel).all()
    categorias = db.query(CategoryModel).all()

    if not produtos:
        return []
    
    categorias_map = {
        c.id: c.nome for c in categorias
    }

    resultado = {}

    for p in produtos:
        if p.status_venda != "Ativo":
            continue

        nome_categoria = categorias_map.get(p.categoria_id, "Sem categoria")

        produto_dict = {
            "id": p.id,
            "cod_pdv": p.cod_pdv,
            "nome": p.nome,
            "preco_custo": p.preco_custo,
            "preco_venda": p.preco_venda,
            "medida": p.medida,
            "estoque": p.estoque,
            "estoque_min": p.estoque_min,
            "descricao": p.descricao,
            "ficha_tecnica": p.ficha_tecnica,
            "status_venda": p.status_venda,
            "sit_estoque": p.sit_estoque,
            "imagem_name": p.imagem_name,
            "imagem": p.imagem
        }

        if nome_categoria not in resultado:
            resultado[nome_categoria] = []

        resultado[nome_categoria].append(produto_dict)

    return [

        {
            "nome_categoria": categorias,
            "produtos": produtos
        }

        for categorias, produtos in resultado.items()
    ]

    

@router.delete("/desktop/delete-product-data-base/{product_id}")
async def delete_product(product_id: str, db: Session = Depends(get_db)):
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        raise HTTPException(status_code=200, detail="Produto excluido com sucesso")
    raise HTTPException(status_code=404, detail="Produto nao encontrado")


@router.put("/desktop/alter-product-data-base/{product_id}")
async def update_product(product_id: str, product: ProdutoSchema, db: Session = Depends(get_db)):
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()

    if not db_product:
        raise HTTPException(status_code=404, detail="Produto nao encontrado")

    for key, value in product.dict(exclude_unset=True).items():
        setattr(db_product, key, value)

    db.commit()
    db.refresh(db_product)
    return {"message": "Produto atualizado com sucesso"}


############################################# CATEGORIAS ################################################
