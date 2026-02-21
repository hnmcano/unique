from pydantic import BaseModel, Field, EmailStr

class Usuarios(BaseModel):
    nome: str = Field(..., min_length= 3, max_length=50)
    email: EmailStr
    senha_hash: str
