from fastapi import APIRouter, Depends
import pandas as pd
from sqlalchemy.orm import Session
from bd.connection import get_db
from typing import List, Dict
from models.products import Product as ProductModel
from schemas.products import Product as ProductSchema
from schemas.products import Category as CategorySchema
from models.products import Category as CategoryModel

router = APIRouter()

# Rotas para inserir produtos ao banco de dados, com a validação do Pydantic
@router.post("/products")
async def get_product(product: ProductSchema, db: Session = Depends(get_db)):
    db_product = ProductModel(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# Rota para popular tabela de produtos
@router.get("/desktop/table")
async def read_products(db: Session = Depends(get_db)):
    return db.query(ProductModel).all()

@router.get("/react/produtos")
async def list_products(db: Session = Depends(get_db)):
    base = db.query(ProductModel).all()
    base_dict = [p.__dict__ for p in base]
    dataframe = pd.DataFrame(base_dict).drop(columns=["_sa_istance_state"], errors="ignore")

    if 'categoria' in dataframe.columns:
        agrupado_df = dataframe.groupby('categoria').apply(lambda x: x.drop(columns="categoria").to_dict(orient='records')).reset_index(name="produtos")
        resultados_json = agrupado_df.to_dict(orient='records')

        return resultados_json
    else:
        return dataframe.to_dict(orient='records')

# Rotas para inserir categorias ao banco de dados, com a validação do Pydantic
@router.post("/category")
async def get_category(categoria: CategorySchema, db: Session = Depends(get_db)):
    db_category = CategoryModel(**categoria.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


# Rota para listar todas as categorias no dropdown
@router.get("/dropdown/categories")
async def read_categories(db: Session = Depends(get_db)):
    return db.query(CategoryModel).all()

# Rota para excluir categorias
@router.delete("/category/{category_id}")
async def delete_category(category_id: str, db: Session = Depends(get_db)):
    db_category = db.query(CategoryModel).filter(CategoryModel.categoria == category_id).first()
    if db_category:
        db.delete(db_category)
        db.commit()
        return {"message": "Categoria excluída com sucesso"}
    return {"message": "Categoria não encontrada"}


