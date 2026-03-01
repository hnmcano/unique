from models.produtos import Produto as ProductModel
from schemas.produtos import Produto as ProdutoSchema
from models.produtos import Categoria as CategoryModel
from models.estabelecimento import Estabelecimento as EstabelecimentoModel

from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from service.websocketservice import notificar_todos
from sqlalchemy.orm import Session
from database.connection import get_db
from sqlalchemy import join
from time import sleep
import pandas as pd
import base64
from service.depencias import get_current_user
from core.dependencies.tenant import get_estabelecimento
from fastapi import HTTPException, Header

router = APIRouter()

########################################### PRODUTOS ################################################

# Rotas para inserir produtos ao banco de dados, com a validação do Pydantic, baseado no envio do desktop
@router.post("/desktop/add/product")
async def adicionar_produto(product: ProdutoSchema, db: Session = Depends(get_db), user_current: dict = Depends(get_current_user)):
    db_product = ProductModel(**product.dict())
    estabelecimento_id = user_current["estabelecimento_id"]
    db_product.estabelecimento_id = estabelecimento_id

    if db_product.imagem is None:
        with open("backend/static/default_product.png", "rb") as image_file:
            image_data = image_file.read()
            encoded_image = base64.b64encode(image_data).decode("utf-8")
            db_product.imagem_name = "default.png"
            db_product.imagem = encoded_image


    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    produtos = db.query(ProductModel).filter(
        ProductModel.estabelecimento_id == estabelecimento_id
    ).all()

    categorias = db.query(CategoryModel).filter(
        CategoryModel.estabelecimento_id == estabelecimento_id
    )
    categorias_map = {
        c.id_categoria: c.nome for c in categorias
    }

    data = []

    for p in produtos:

        nome_categoria = categorias_map.get(p.categoria_id, "Sem categoria")

        produto = {
            "estabelecimento_id": p.estabelecimento_id,
            "id_produto": p.id_produto,
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


    await notificar_todos(estabelecimento_id, {
                            "tipo": "Atualizar_produtos",
                            "dados": jsonable_encoder(data)
                            })

    return data

# Rota para popular tabela de produtos disponivel no desktop na aba produtos
@router.get("/desktop/table")
async def read_products(db: Session = Depends(get_db), user_current: dict = Depends(get_current_user)):
    estabelecimento_id = user_current["estabelecimento_id"]

    produtos = db.query(ProductModel).filter(ProductModel.estabelecimento_id == estabelecimento_id).all()
    categorias = db.query(CategoryModel).filter(CategoryModel.estabelecimento_id == estabelecimento_id).all()


    if not produtos:
        return []

    categorias_map = {
        c.id_categoria: c.nome for c in categorias
    }

    data = []

    for p in produtos:

        nome_categoria = categorias_map.get(p.categoria_id, "Sem categoria")

        produto = {
            "id_produto": p.id_produto,
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

@router.get("/mesa-add-product")
async def read_products(db: Session = Depends(get_db), user_current: dict = Depends(get_current_user)):
    estabelecimento_id = user_current["estabelecimento_id"]

    produtos = db.query(ProductModel).filter(ProductModel.estabelecimento_id == estabelecimento_id).all()
    categorias = db.query(CategoryModel).filter(CategoryModel.estabelecimento_id == estabelecimento_id).all()

    if not produtos:
        return []

    categorias_map = {
        c.id_categoria: c.nome for c in categorias
    }

    data = []

    for p in produtos:
        if p.status_venda != "Ativo": 
            continue

        nome_categoria = categorias_map.get(p.categoria_id, "Sem categoria")

        produto = {
            "id": p.id_produto,
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
async def list_products(db: Session = Depends(get_db), estabelecimento: EstabelecimentoModel = Depends(get_estabelecimento)):

    produtos = db.query(ProductModel).filter(ProductModel.estabelecimento_id == estabelecimento.id).all()
    categorias = db.query(CategoryModel).filter(CategoryModel.estabelecimento_id == estabelecimento.id).all()

    if not produtos:
        return []
    
    categorias_map = {
        c.id_categoria: c.nome for c in categorias
    }

    resultado = {}

    for p in produtos:
        if p.status_venda != "Ativo":
            continue

        nome_categoria = categorias_map.get(p.categoria_id, "Sem categoria")

        produto_dict = {
            "id": p.id_produto,
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
async def delete_product(product_id: str, db: Session = Depends(get_db), user_current: dict = Depends(get_current_user)):
    estabelecimento_id = user_current["estabelecimento_id"]

    db_product = db.query(ProductModel).filter(ProductModel.id_produto == product_id, ProductModel.estabelecimento_id == estabelecimento_id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        raise HTTPException(status_code=200, detail="Produto excluido com sucesso")
    raise HTTPException(status_code=404, detail="Produto nao encontrado")

@router.put("/desktop/alter-product-data-base/{product_id}")
async def update_product(product_id: str, product: ProdutoSchema, db: Session = Depends(get_db), user_current: dict = Depends(get_current_user)):

    estabelecimento_id = user_current["estabelecimento_id"]

    db_product = db.query(ProductModel).filter(ProductModel.id_produto == product_id, ProductModel.estabelecimento_id == estabelecimento_id).first()

    if not db_product:
        raise HTTPException(status_code=404, detail="Produto nao encontrado")

    for key, value in product.dict(exclude_unset=True).items():
        setattr(db_product, key, value)

    db.commit()
    db.flush()

    produtos = db.query(ProductModel).filter(
        ProductModel.estabelecimento_id == estabelecimento_id
    ).all()

    categorias = db.query(CategoryModel).filter(
        CategoryModel.estabelecimento_id == estabelecimento_id
    )
    categorias_map = {
        c.id_categoria: c.nome for c in categorias
    }

    data = []

    for p in produtos:

        nome_categoria = categorias_map.get(p.categoria_id, "Sem categoria")

        produto = {
            "estabelecimento_id": p.estabelecimento_id,
            "id_produto": p.id_produto,
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


    await notificar_todos(estabelecimento_id, {
                            "tipo": "Atualizar_produtos",
                            "dados": jsonable_encoder(data)
                            })

    return data