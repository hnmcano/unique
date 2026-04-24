from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from .produtos import Produto
from uuid import UUID


class ImpressoraInput(BaseModel):
    impressora: str
    padrao: bool
    tamanho: str

    model_config = {
        "from_attributes": True
    }

class ImpressoraResponse(BaseModel):
    estabelecimento_id: UUID
    impressora_id: UUID
    data_adicao: datetime | None = None
    impressora: str
    padrao: bool
    tamanho: str | None = None

    model_config = {
        "from_attributes": True
    }