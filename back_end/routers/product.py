from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from bd.connection import get_db
from models.products import Product as ProductModel
from schemas.products import Product as ProductSchema
from schemas.products import Category as CategorySchema
from models.products import Category as CategoryModel

router = APIRouter()

# Rotas para inserir produtos ao banco de dados, com a validação do Pydantic
@router.post("/products")
def get_product(product: ProductSchema, db: Session = Depends(get_db)):
    db_product = ProductModel(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# Rota para popular tabela de produtos
@router.get("/table")
async def read_products(db: Session = Depends(get_db)):
    return db.query(ProductModel).all()


# Rotas para inserir categorias ao banco de dados, com a validação do Pydantic
@router.post("/category")
def get_category(categoria: CategorySchema, db: Session = Depends(get_db)):
    db_category = CategoryModel(**categoria.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


# Rota para listar todas as categorias no dropdown
@router.get("/dropdown/categories")
def read_categories(db: Session = Depends(get_db)):
    return db.query(CategoryModel).all()

# Rota para excluir categorias
@router.delete("/category/{category_id}")
def delete_category(category_id: str, db: Session = Depends(get_db)):
    db_category = db.query(CategoryModel).filter(CategoryModel.categoria == category_id).first()
    if db_category:
        db.delete(db_category)
        db.commit()
        return {"message": "Categoria excluída com sucesso"}
    return {"message": "Categoria não encontrada"}

