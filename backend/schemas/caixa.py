from pydantic import BaseModel, Field

class Caixa(BaseModel):
    valor: float = Field(..., ge=0, description="Valor do caixa")
    