from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


class ItensPedidosMesa(BaseModel):
    produto_id: int = Field(..., gt=0)
    quantidade: int = Field(..., gt=0)
    valor_unitario: float

class CriacaoPedidoMesa(BaseModel):
    status: str
    itens: Optional[List[ItensPedidosMesa]]
    
class AberturaMesa(BaseModel):
    numero: int = Field(..., gt=0)
    pedido: CriacaoPedidoMesa
    
class ItensPedidosMesaResponse(BaseModel):
    produto_id: int = Field(..., ge=0)
    quantidade: int = Field(..., ge=0)
    valor_unitario: float

class CriacaoPedidosResponse(BaseModel):
    id: int
    status: str
    data_criacao: datetime
    data_atualizacao: datetime | None
    valor_total: float | None
    quantidade_itens: int | None
    itens: Optional[List[ItensPedidosMesaResponse]]

class MesasResponse(BaseModel):
    id: int = Field(..., gt=0)
    numero: int = Field(..., gt=0)
    pedido: CriacaoPedidosResponse


class AtualizarItensMesa(BaseModel):
    id: int = Field(..., gt=0)
    numero: int = Field(..., gt=0)
    pedido: CriacaoPedidoMesa