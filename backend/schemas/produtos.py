from pydantic import BaseModel, Field
from uuid import UUID

# Modelo padrão para produtos
class Produto(BaseModel):
    categoria_id: UUID
    cod_pdv: str | None = None  
    nome: str = Field(..., min_length= 3, max_length=50)
    preco_custo: float = Field(..., ge=0)
    preco_venda: float = Field(..., gt=0)
    medida: str = Field(..., min_length=1, max_length=2)
    estoque: int
    estoque_min: int = Field(..., ge=0)
    descricao: str | None = None
    ficha_tecnica: str | None = None
    status_venda: str = Field(..., min_length=3, max_length=20)
    imagem_name: str | None = None
    imagem: str | None = None

    model_config = {
        "from_attributes": True
    }


# Modelo para categorias
class Categoria(BaseModel):
    nome: str = Field(..., min_length=3, max_length=30)

    model_config = {
        "from_attributes": True
    }


class ProdutoSchema(Produto):
    produto_id: UUID
    estabelecimento_id: UUID
    nome: str
    preco_custo: float
    preco_venda: float
    medida: str
    estoque: int
    estoque_min: int
    descricao: str | None = None
    ficha_tecnica: str | None = None
    status_venda: str
    imagem_name: str | None = None
    imagem: str | None = None

