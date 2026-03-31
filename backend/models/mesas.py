from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey, Text, text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database.connection import Base
from datetime import datetime
import uuid
from sqlalchemy.dialects.postgresql import UUID

class Mesas(Base):
    __tablename__ = 'mesas'

    id_mesa = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4,server_default=text("gen_random_uuid()"), nullable=False, index=True)
    estabelecimento_id = Column(UUID(as_uuid=True), ForeignKey('estabelecimentos.id'), nullable=False, index=True)
    caixa_id = Column(UUID(as_uuid=True), ForeignKey('caixa.id'), nullable=True, index=True)
    numero = Column(Integer, nullable=False)

    pedido = relationship("PedidosMesa", back_populates="mesa", cascade="all, delete-orphan")
    caixa = relationship("Caixa", back_populates="mesa", uselist=False)
    

class PedidosMesa(Base):
    __tablename__ = 'pedidos_mesa'

    id_pedido_mesa = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4, server_default=text("gen_random_uuid()"), nullable=False)
    estabelecimento_id = Column(UUID(as_uuid=True), ForeignKey('estabelecimentos.id'), nullable=False, index=True)
    mesa_id = Column(UUID(as_uuid=True), ForeignKey('mesas.id_mesa'),nullable=False, index=True)
    status = Column(String(50), nullable=False)
    data_criacao = Column(DateTime(timezone=True), default=datetime.now)
    data_atualizacao = Column(DateTime(timezone=True), onupdate=func.now())
    valor_total = Column(Float, nullable=False)
    quantidade_itens = Column(Integer, nullable=False)
    
    mesa = relationship("Mesas", back_populates="pedido")
    itens = relationship("PedidoItens", back_populates="pedido", cascade="all, delete-orphan", order_by="PedidoItens.ordem_criacao")
    

class PedidoItens(Base):
    __tablename__ = 'pedido_itens'

    id_itens_mesa = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4,server_default=text("gen_random_uuid()"), nullable=False)
    estabelecimento_id = Column(UUID(as_uuid=True), ForeignKey('estabelecimentos.id'), nullable=False, index=True)
    pedido_id = Column(UUID(as_uuid=True), ForeignKey('pedidos_mesa.id_pedido_mesa'), nullable=False, index=True)
    produto_id = Column(UUID(as_uuid=True), ForeignKey('produtos.id_produto'), nullable=False, index=True)
    quantidade = Column(Integer, nullable=False)
    valor_unitario = Column(Float, nullable=False)
    valor_total = Column(Float, nullable=False)
    ordem_criacao = Column(DateTime(timezone=True), default=datetime.utcnow)

    pedido = relationship("PedidosMesa", back_populates="itens")
    produto = relationship("Produto", back_populates="itens_mesa", uselist=False)

