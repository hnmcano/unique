from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional
from datetime import datetime
from decimal import Decimal

class ItemPedidoInput(BaseModel):
    produto_id: int = Field(..., description="ID do produto")
    quantidade: int = Field(..., ge=1)
    valor_unitario: Decimal = Field(..., ge=0, description="Valor unitário do produto no pedido")
    observacoes: Optional[str] = None

class ClienteInput(BaseModel):
    nome: str = Field(..., min_length=3, description="Nome do cliente")
    email: Optional[EmailStr] = None
    telefone: str = Field(..., description="Telefone do cliente")

class EntregaInput(BaseModel):
    cep: str = Field(..., description="CEP da entrega")
    endereco: str = Field(..., description="Endereço da entrega")
    numero: str = Field(..., description="Número da entrega")
    bairro: str = Field(..., description="Bairro da entrega")
    cidade: str = Field(..., description="Cidade da entrega")
    estado: str = Field(..., description="Estado da entrega")
    complemento: Optional[str] = None
    referencia: Optional[str] = None
    taxa_entrega: Decimal = Field(..., ge=0, description="Taxa de entrega")

class NovoPedidoSchema(BaseModel):

    itens: List[ItemPedidoInput] = Field(..., description="Itens do pedido")

    metodo_pagamento: str = Field(..., description="Método de pagamento")

    valor_total: Decimal = Field(..., ge=0, description="Valor total do pedido")

    cliente: ClienteInput

    entrega: EntregaInput













# 1. Detalhes de Item em um Pedido
class ItemPedidoResponse(BaseModel):
    id: int
    produto_id: int
    quantidade: int
    # O preço histórico é crucial e deve ser retornado com precisão
    preco_unitario_historico: Decimal = Field(..., decimal_places=2) 
    observacoes: Optional[str] = None
    
    class Config:
        from_attributes = True # Necessário para ler o objeto SQLAlchemy

# 2. Endereço Histórico
class EnderecoPedidoResponse(BaseModel):
    id: int
    endereco: str
    numero: Optional[str]
    complemento: Optional[str]
    bairro: str
    cep: str
    observacoes: Optional[str] = None
    taxa_entrega: Decimal = Field(..., decimal_places=2)

    class Config:
        from_attributes = True

# 3. Informações do Cliente
class ClienteResponse(BaseModel):
    id: int
    nome: str
    email: str
    telefone: str
    
    class Config:
        from_attributes = True

# --- Modelo Principal de Resposta ---

class PedidoResponse(BaseModel):
    """
    Schema de saída para um Pedido, incluindo todas as suas relações aninhadas.
    """
    id: int # ID auto-gerado
    cliente_id: int
    data_pedido: datetime # Retorna o timestamp gerado pelo DB
    status: str
    metodo_pagamento: str
    valor_total: Decimal = Field(..., decimal_places=2)
    
    # Relações Aninhadas
    # O Pydantic irá popular esses campos usando os objetos relacionados do SQLAlchemy
    cliente: ClienteResponse 
    endereco_entrega: EnderecoPedidoResponse # Relação 1:1
    itens: List[ItemPedidoResponse] # Relação 1:N

    class Config:
        # Essencial: Habilita o modo ORM para ler atributos de objetos SQLAlchemy 
        # e resolver as relações automaticamente.
        from_attributes = True