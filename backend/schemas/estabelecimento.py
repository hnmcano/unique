from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from uuid import UUID

class EstabelecimentoBase(BaseModel):
    nome: str = Field(..., min_length= 3, max_length=50)
    nome_fantasia: str = Field(..., min_length= 3, max_length=50)
    documento: str = Field(..., min_length=14, max_length=14)
    telefone: str = Field(..., min_length=11, max_length=11)
    email: EmailStr
    senha: str

    model_config = {
        "from_attributes": True
    }

class EstabelecimentoSchemaAtualizar(BaseModel):
    id: UUID
    nome: str = Field(..., min_length= 3, max_length=50)
    nome_fantasia: str = Field(..., min_length= 3, max_length=50)
    documento: str = Field(..., min_length=14, max_length=14)
    telefone: str = Field(..., min_length=11, max_length=11)
    email: EmailStr
    logo_img: str | None
    endereco: str | None
    rede_social: str | None
    plano: str
    limite_usuarios: int
    ativo: bool
    data_expiracao: str
    subdominio: str
    criado_em: str
    atualizado_em: str

    model_config = {
        "from_attributes": True
    }

class EstabelecimentoResponse(BaseModel):
    id: UUID
    nome: str = Field(..., min_length= 3, max_length=50)
    nome_fantasia: str = Field(..., min_length= 3, max_length=50)
    documento: str = Field(..., min_length=14, max_length=14)
    telefone: str = Field(..., min_length=11, max_length=11)
    email: EmailStr
    logo_img: str | None
    endereco: str | None
    rede_social: str | None
    plano: str
    limite_usuarios: int
    ativo: bool
    data_expiracao: datetime | None
    subdominio: str | None
    criado_em: datetime | None
    atualizado_em: datetime | None

    model_config = {
        "from_attributes": True
    }