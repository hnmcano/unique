from pydantic import BaseModel, Field

class Carrinho(BaseModel):
    cod_sistema: int = Field(..., gt=0)
    cod_pdv: str | None = None
    categoria: str = Field(..., min_length=3, max_length=30)
    nome: str = Field(..., min_length= 3, max_length=50)
    preco_custo: float = Field(..., gt=0)
    preco_venda: float = Field(..., gt=0)
    medida: str = Field(..., min_length=1, max_length=2)
    estoque: int = Field(..., ge=0)
    estoque_min: int = Field(..., ge=0)
    sit_estoque: str = Field(..., min_length=0, max_length=50)
    descricao: str | None = None
    ficha_tecnica: str | None = None
    status_venda: str = Field(..., min_length=3, max_length=20)
    imagem_url: str | None = None
    quantidade: int = Field(..., ge=1)

class CarrinhoUpdate(Carrinho):
    id: int = Field(..., gt=0)
    quantidade: int = Field(..., ge=1)