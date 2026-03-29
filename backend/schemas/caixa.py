<<<<<<< HEAD
from pydantic import BaseModel, Field

class Caixa(BaseModel):
    valor: float = Field(..., ge=0, description="Valor do caixa")
    
=======
from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime

class Caixa(BaseModel):
    valor_inicial: float = Field(..., ge=0, description="Valor do caixa")

    model_config = {
        "from_attributes": True
    }

    
class CaixaResponse(BaseModel):
    id: UUID
    estabelecimento_id: UUID
    data_abertura: datetime
    status: str
    valor_inicial: float
    valor_final: float
    data_fechamento: datetime | None = None


    model_config = {
        "from_attributes": True
    }

>>>>>>> 182d746 (Versão atual da infra com backend da VM)
