from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Numeric, ForeignKey, text, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database.connection import Base
from datetime import datetime
import uuid
from sqlalchemy.dialects.postgresql import UUID

class Pedido(Base):
    __tablename__ = 'pedidos'

    id_pedido = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4,server_default=text("gen_random_uuid()"), nullable=False, index=True)

    estabelecimento_id = Column(UUID(as_uuid=True), ForeignKey('estabelecimentos.id'), nullable=False, index=True)

    cliente_id = Column(UUID(as_uuid=True), ForeignKey('clientes.id'), nullable=False)
    caixa_id = Column(UUID(as_uuid=True), ForeignKey('caixa.id'), nullable=False)

    data_criacao = Column(DateTime(timezone=True), default=datetime.now)
    data_atualizacao = Column(DateTime(timezone=True), onupdate=func.now())
    status = Column(String(50), default="PENDENTE", nullable=False)
    metodo_pagamento = Column(String(50), nullable=False)
    opcoes_pagamento = Column(String(50), nullable=False)
    valor_total = Column(Float, nullable=False)
    observacoes = Column(Text, nullable=True)

    cliente = relationship("Clientes", back_populates="pedidos")
    endereco_entrega = relationship("EnderecoPedido", back_populates="pedido", cascade="all, delete-orphan", uselist=False)
    itens = relationship("ItemPedido", back_populates="pedido", cascade="all, delete-orphan", order_by="ItemPedido.id_itens_pedido")
    caixa = relationship("Caixa", back_populates="pedido")
    estabelecimento = relationship("Estabelecimento", back_populates="pedido")

    def __repr__(self):
        return f"Pedido(id_pedido={self.id_pedido}, cliente_id={self.cliente_id}, data_criacao={self.data_criacao}, data_atualizacao={self.data_atualizacao})"
    
class EnderecoPedido(Base):
    __tablename__ = 'enderecos_pedidos'

    id_endereco_pedido = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=text("gen_random_uuid()"), nullable=False, index=True)
    estabelecimento_id = Column(UUID(as_uuid=True), ForeignKey('estabelecimentos.id'), nullable=False, index=True)
    pedido_id = Column(UUID(as_uuid=True), ForeignKey('pedidos.id_pedido'), unique=True, nullable=False)

    cep = Column(String(8), nullable=False)
    endereco = Column(String(200), nullable=False)
    numero = Column(String(100), nullable=False)
    bairro = Column(String(100), nullable=False)
    cidade = Column(String(100), nullable=False)
    estado = Column(String(2), nullable=False)
    complemento = Column(String(200), nullable=False)
    referencia = Column(String(200), nullable=True)

    taxa_entrega = Column(Numeric(10, 2), nullable=False)

    pedido = relationship("Pedido", back_populates="endereco_entrega")

    def __repr__(self):
        return f"EnderecoPedido(id_endereco_pedido={self.id_endereco_pedido}, cep={self.cep}, endereco={self.endereco}, bairro={self.bairro}, cidade={self.cidade}, complemento={self.complemento}, referencia={self.referencia})"
    
class ItemPedido(Base):
    __tablename__ = 'itens_pedidos'

    id_itens_pedido = Column(UUID(as_uuid=True), primary_key=True,default=uuid.uuid4,server_default=text("gen_random_uuid()"), nullable=False, index=True)
    estabelecimento_id = Column(UUID(as_uuid=True), ForeignKey('estabelecimentos.id'), nullable=False, index=True)
    pedido_id = Column(UUID(as_uuid=True), ForeignKey('pedidos.id_pedido'), nullable=False, index=True)
    produto_id = Column(UUID(as_uuid=True), ForeignKey('produtos.id_produto'), nullable=False, index=True)
    quantidade = Column(Integer, nullable=False)
    valor_unitario = Column(Float, nullable=False)
    valor_total = Column(Float, nullable=True)

    pedido = relationship("Pedido", back_populates="itens")
    produtos = relationship("Produto", back_populates="itens_pedidos", uselist=False)

    def __repr__(self):
        return f"ItemPedido(id_itens_pedido={self.id_itens_pedido}, pedido_id={self.pedido_id},quantidade={self.quantidade}, valor_unitario={self.valor_unitario})"
>>>>>>> 182d746 (Versão atual da infra com backend da VM)
