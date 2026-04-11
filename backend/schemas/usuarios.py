from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from uuid import UUID

class Usuarios(BaseModel):
    email: EmailStr
    senha_hash: str

    model_config = {
        "from_attributes": True
    }


class UsuariosResponse(BaseModel):
    id: UUID
    estabelecimento_id: UUID
    nome: str
    email: EmailStr
    ativo: bool
    criado_em: datetime

    model_config = {
        "from_attributes": True
    }


