from pydantic import BaseModel, Field

class EstabelecimentoBase(BaseModel):
    nome: str = Field(..., max_length=100)
    endereco: str = Field(..., max_length=200)
    instagram: str | None = None
    telefone: str = Field(..., max_length=11)
    logo_base64: str | None = None