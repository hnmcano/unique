from fastapi import APIRouter, Depends
import pandas as pd
from sqlalchemy.orm import Session
from sqlalchemy import join
from time import sleep
from bd.connection import get_db
from models.produtos import Produto as ProductModel
from schemas.produtos import Produto as ProdutoSchema
from schemas.produtos import Categoria as CategoriaSchema
from models.produtos import Categoria as CategoryModel

router = APIRouter()

########################################### PRODUTOS ################################################

# Rotas para inserir produtos ao banco de dados, com a validação do Pydantic, baseado no envio do desktop
@router.post("/desktop/add")
async def get_product(product: ProdutoSchema, db: Session = Depends(get_db)):
    db_product = ProductModel(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# Rota para popular tabela de produtos disponivel no desktop na aba produtos
@router.get("/desktop/table")
async def read_products(db: Session = Depends(get_db)):
    db = db.query(ProductModel).all()

    return db

# Rota para listar todos os produtos com os nomes das categorias no front-end com react
@router.get("/react/catalago")
async def list_products(db: Session = Depends(get_db)):
    # executar a query

    produtos = db.query(ProductModel).all()
    categorias = db.query(CategoryModel).all()

    p = pd.DataFrame([p.__dict__ for p in produtos])
    c = pd.DataFrame([c.__dict__ for c in categorias])

    p = p.drop(columns=["_sa_instance_state"], errors="ignore")
    c = c.drop(columns=["_sa_instance_state"], errors="ignore")

    c = c.rename(columns={"nome": "nome_categoria"})


    data = pd.merge(p, c, left_on="categoria_id", right_on="id", how="left")
    data = data.drop(columns=["id_y"]).rename(columns={"id_x": "id"})
    data = data[data["status_venda"] == "Ativo"]

    if "nome_categoria" in data.columns:
        data = (
            data.rename(columns={"id" : "produto_id"})
            .groupby("nome_categoria")
            .apply(lambda x: x.drop(columns=["categoria_id", "nome_categoria"]).to_dict("records"))
            .reset_index(name="produtos")
        )

        data = data.to_dict("records")

        return data
    else:
        return data.to_dict("records")
    

############################################# CATEGORIAS ################################################

# Rotas para inserir categorias ao banco de dados, com a validação do Pydantic, baseado no envio do desktop
@router.post("/category")
async def get_category(categoria: CategoriaSchema, db: Session = Depends(get_db)):
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

