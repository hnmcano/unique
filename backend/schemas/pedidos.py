from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional
from datetime import datetime
from decimal import Decimal
from .produtos import Produto
from uuid import UUID

class ItemPedidoInput(BaseModel):
    produto_id: UUID
    quantidade: int 
    valor_unitario: float 

    model_config = {
        "from_attributes": True
    }

class ClienteInput(BaseModel):
    nome: str
    email: EmailStr | None
    telefone: str
    cpf: str | None

    model_config = {
        "from_attributes": True
    }

class EntregaInput(BaseModel):
    cep: str 
    endereco: str
    numero: str 
    bairro: str 
    cidade: str
    estado: str 
    complemento: str | None
    referencia: str | None
    taxa_entrega: float

    model_config = {
        "from_attributes": True
    }

class AlteracaoItemPedido(BaseModel):
    pedido_id: UUID
    id_itens_pedido: UUID
    produto_id: UUID
    quantidade: int

    model_config = {
        "from_attributes": True
    }

class DeletarItem(BaseModel):
    id_pedido: UUID
    id_itens_pedido: UUID

    model_config = {
        "from_attributes": True
    }

class AtualizarStatus(BaseModel):
    pedido_id: UUID
    status_antigo: str
    status_novo: str
    
class AdicionarProdutosPedido(BaseModel):
    pedido_id: UUID
    produto_id: UUID
    quantidade: int
    valor_unitario: float

    model_config = {
        "from_attributes": True
    }

class NovoPedidoSchema(BaseModel):

    itens: List[ItemPedidoInput] 

    metodo_pagamento: str

    opcoes_pagamento: str

    valor_total: float
    
    observacoes: str | None

    cliente: ClienteInput

    entrega: EntregaInput

    model_config = {
        "from_attributes": True
    }

# 1. Detalhes de Item em um Pedido
class ItemPedidoResponse(BaseModel):
    id_itens_pedido: UUID
    produto_id: UUID
    quantidade: int
    # O preço histórico é crucial e deve ser retornado com precisão
    valor_unitario: Decimal = Field(..., decimal_places=2) 
    observacoes: Optional[str] = None
    produtos: Produto

    model_config = {
        "from_attributes": True
    }

# 2. Endereço Histórico
class EnderecoPedidoResponse(BaseModel):
    id_endereco_pedido: UUID
    endereco: str
    numero: str
    complemento: Optional[str]
    bairro: str
    cep: str
    observacoes: Optional[str] = None
    taxa_entrega: Decimal = Field(..., decimal_places=2)

    model_config = {
        "from_attributes": True
    }

# 3. Informações do Cliente
class ClienteResponse(BaseModel):
    id: UUID
    nome: str
    email: str
    telefone: str
    
    model_config = {
        "from_attributes": True
    }

# --- Modelo Principal de Resposta ---
class PedidoResponse(BaseModel):
    """
    Schema de saída para um Pedido, incluindo todas as suas relações aninhadas.
    """
    id_pedido: UUID # ID auto-gerado
    cliente_id: UUID
    data_criacao: datetime  # Retorna o timestamp gerado pelo DB
    status: str
    metodo_pagamento: str
    opcoes_pagamento: str
    valor_total: float
    
    # Relações Aninhadas
    # O Pydantic irá popular esses campos usando os objetos relacionados do SQLAlchemy
    cliente: ClienteResponse 
    endereco_entrega: EnderecoPedidoResponse # Relação 1:1
    itens: List[ItemPedidoResponse] # Relação 1:N
    

    model_config = {
        "from_attributes": True
    }

