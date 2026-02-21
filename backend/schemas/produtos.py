from pydantic import BaseModel, Field

# Modelo padrão para produtos
class Produto(BaseModel):
    estabelecimento_id: str
    categoria_id: int
    cod_pdv: str | None = None  
    nome: str = Field(..., min_length= 3, max_length=50)
    preco_custo: float = Field(..., ge=0)
    preco_venda: float = Field(..., gt=0)
    medida: str = Field(..., min_length=1, max_length=2)
    estoque: int = Field(..., ge=0)
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
    estabelecimento_id: str
    nome: str = Field(..., min_length=3, max_length=30)

    model_config = {
        "from_attributes": True
    }
