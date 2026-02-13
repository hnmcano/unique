from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from .produtos import Produto


class ItensPedidosMesa(BaseModel):
    produto_id: int = Field(..., gt=0)
    quantidade: int = Field(..., gt=0)
    valor_unitario: float

    class Config:
        from_atributes = True

class CriacaoPedidoMesa(BaseModel):
    status: str
    itens: Optional[List[ItensPedidosMesa]]

    class Config:
        from_atributes = True

class AberturaMesa(BaseModel):
    numero: int = Field(..., gt=0)
    pedido: CriacaoPedidoMesa

    class Config:
        from_atributes = True




class AdicionarItensMesa(BaseModel):
    mesa_id: int
    produto_id: int
    quantidade: int
    valor_unitario: float

    class Config:
        from_atributes = True






















class ItensPedidosMesaResponse(BaseModel):
    produto_id: int = Field(..., ge=0)
    quantidade: int = Field(..., ge=0)
    valor_unitario: float
    valor_total: float
    produto: Produto

    model_config = {
        "from_attributes": True
    }

class CriacaoPedidosResponse(BaseModel):
    id: int
    status: str
    data_criacao: datetime
    data_atualizacao: datetime | None
    valor_total: float | None
    quantidade_itens: int | None
    itens: Optional[List[ItensPedidosMesaResponse]]

    model_config = {
        "from_attributes": True
    }
class MesasResponse(BaseModel):
    id: int = Field(..., gt=0)
    numero: int = Field(..., gt=0)
    pedido: CriacaoPedidosResponse

    model_config = {
        "from_attributes": True
    }
