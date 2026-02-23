from pydantic import BaseModel, Field, EmailStr

class Usuarios(BaseModel):
    email: EmailStr
    senha_hash: str
