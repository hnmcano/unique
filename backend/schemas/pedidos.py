from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional
from datetime import datetime
from decimal import Decimal

class ItemPedidoInput(BaseModel):
    produto_id: int
    quantidade: int 
    valor_unitario: float 

class ClienteInput(BaseModel):
    nome: str
    email: EmailStr | None
    telefone: str 

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

class NovoPedidoSchema(BaseModel):

    itens: List[ItemPedidoInput] 

    metodo_pagamento: str

    valor_total: float
    
    observacoes: str | None

    cliente: ClienteInput

    entrega: EntregaInput







# 1. Detalhes de Item em um Pedido
class ItemPedidoResponse(BaseModel):
    id: int
    produto_id: int
    quantidade: int
    # O preço histórico é crucial e deve ser retornado com precisão
    valor_unitario: Decimal = Field(..., decimal_places=2) 
    observacoes: Optional[str] = None
    
    class Config:
        from_attributes = True # Necessário para ler o objeto SQLAlchemy

# 2. Endereço Histórico
class EnderecoPedidoResponse(BaseModel):
    id: int
    endereco: str
    numero: int
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