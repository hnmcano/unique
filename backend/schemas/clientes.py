<<<<<<< HEAD
from pydantic import  BaseModel, Field, EmailStr

# Modelo padrão para usuários
class Clientes(BaseModel):
    cliente: str = Field(..., min_length= 3, max_length=50)
    telefone: str = Field(..., min_length=11, max_length=11)
    email: EmailStr
    cep: str = Field(..., min_length=8, max_length=8)
    endereco: str
    bairro: str
    cidade: str
    complemento: str
=======
from pydantic import  BaseModel, Field, EmailStr
from uuid import UUID

# Modelo padrão para usuários
class Clientes(BaseModel):
    cliente: UUID
    telefone: str = Field(..., min_length=11, max_length=11)
    email: EmailStr
    cep: str = Field(..., min_length=8, max_length=8)
    endereco: str
    bairro: str
    cidade: str
    complemento: str
>>>>>>> 182d746 (Versão atual da infra com backend da VM)
    referencia: str | None = None