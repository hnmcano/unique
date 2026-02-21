from pydantic import BaseModel, Field, EmailStr

class EstabelecimentoBase(BaseModel):
    nome: str = Field(..., min_length= 3, max_length=50)
    nome_fantasia: str = Field(..., min_length= 3, max_length=50)
    documento: str = Field(..., min_length=14, max_length=14)
    telefone: str = Field(..., min_length=11, max_length=11)
    email: EmailStr