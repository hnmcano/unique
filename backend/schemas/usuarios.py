from pydantic import BaseModel, Field, EmailStr
from uuid import UUID

class Usuarios(BaseModel):
    email: EmailStr
    senha_hash: str

class UsuariosResponse(BaseModel):
    id: UUID
    estabelecimento_id: UUID
    nome: str
    email: EmailStr
    ativo: bool
    criado_em: str
>>>>>>> 182d746 (Versão atual da infra com backend da VM)
