from pydantic import BaseModel, Field

class Product(BaseModel):
    cod_sistema: int = Field(..., gt=0)
    cod_pdv: str = Field(..., min_length=5, max_length=20)
    categoria: str = Field(..., min_length=3, max_length=30)
    nome: str = Field(..., min_length= 3, max_length=50)
    preco_custo: float = Field(..., gt=0)
    peco_venda: float = Field(..., gt=0)
    medida: str = Field(..., min_length=1, max_length=2)
    estoque: int = Field(..., ge=0)
    estoque_min: int = Field(..., ge=0)
    sit_estoque: str = Field(..., min_length=3, max_length=20)
    descricao: str = Field(..., min_length= 10, max_length=300)
    ficha_tecnica: str | None = None
    status_venda: str = Field(..., min_length=3, max_length=20)
    imagem_url: str | None = None
