from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from .produtos import Produto
from uuid import UUID


class ItensPedidosMesa(BaseModel):
    produto_id: UUID
    quantidade: int = Field(..., gt=0)
    valor_unitario: float

    model_config = {
        "from_attributes": True
    }
class CriacaoPedidoMesa(BaseModel):
    status: str
    itens: Optional[List[ItensPedidosMesa]]

    model_config = {
        "from_attributes": True
    }

class AberturaMesa(BaseModel):
    numero: int = Field(..., gt=0)
    pedido: CriacaoPedidoMesa

    model_config = {
        "from_attributes": True
    }


class AdicionarItensMesa(BaseModel):
    mesa_id: UUID
    produto_id: UUID
    quantidade: int
    valor_unitario: float

    model_config = {
        "from_attributes": True
    }



class ItensPedidosMesaResponse(BaseModel):
    produto_id: UUID
    quantidade: int = Field(..., ge=0)
    valor_unitario: float
    valor_total: float
    produto: Produto

    model_config = {
        "from_attributes": True
    }

class CriacaoPedidosResponse(BaseModel):
    id_pedido_mesa: UUID
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
    id_mesa: UUID
    numero: int = Field(..., gt=0)
    pedido: CriacaoPedidosResponse

    model_config = {
        "from_attributes": True
    }

