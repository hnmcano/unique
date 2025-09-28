from pydantic import  BaseModel, Field, EmailStr

class Clientes(BaseModel):
    cliente: str = Field(..., min_length= 3, max_length=50)
    telefone: int = Field(..., min_length=10, max_length=11)
    email: EmailStr
    cep: int = Field(..., min_length=8, max_length=8)
    endereco: str
    bairro: str
    cidade: str
    complemento: str
    referencia: str | None = None




