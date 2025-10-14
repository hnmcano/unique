from pydantic import  BaseModel, Field, EmailStr

# Modelo padrão para usuários
class User(BaseModel):
    cliente: str = Field(..., min_length= 3, max_length=50)
    telefone: str = Field(..., min_length=11, max_length=11)
    email: EmailStr
    cep: str = Field(..., min_length=8, max_length=8)
    endereco: str
    bairro: str
    cidade: str
    complemento: str
    referencia: str | None = None