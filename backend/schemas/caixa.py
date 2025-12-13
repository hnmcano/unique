from pydantic import BaseModel, Field

class Caixa(BaseModel):
    valor: float
    