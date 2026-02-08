from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from bd.connection import Base
from datetime import datetime


class Mesas(Base):
    __tablename__ = 'mesas'

    id = Column(Integer, primary_key=True, index=True)
    caixa_id = Column(Integer, ForeignKey('caixa.id'), nullable=True)
    numero = Column(Integer, nullable=False)

    pedido = relationship("PedidosMesa", back_populates="mesa", cascade="all, delete-orphan")
    caixa = relationship("Caixa", back_populates="mesa", uselist=False)


class PedidosMesa(Base):
    __tablename__ = 'pedidos_mesa'

    id: int = Column(Integer, primary_key=True, index=True)
    mesa_id: int = Column(Integer, ForeignKey('mesas.id'), nullable=False)
    status: str = Column(String(50), nullable=False)
    data_criacao: datetime = Column(DateTime(timezone=True), default=datetime.now)
    data_atualizacao: datetime = Column(DateTime(timezone=True), onupdate=func.now())
    valor_total: float = Column(Float, nullable=False)
    quantidade_itens: int = Column(Integer, nullable=False)
    
    mesa = relationship("Mesas", back_populates="pedido")
    itens = relationship("PedidoItens", back_populates="pedido", cascade="all, delete-orphan")
    

class PedidoItens(Base):
    __tablename__ = 'pedido_itens'

    id: int = Column(Integer, primary_key=True, index=True)
    pedido_id: int = Column(Integer, ForeignKey('pedidos_mesa.id'), nullable=False)
    produto_id: int = Column(Integer, ForeignKey('produtos.id'), nullable=False)
    quantidade: int = Column(Integer, nullable=False)
    valor_unitario: float = Column(Float, nullable=False)

    pedido = relationship("PedidosMesa", back_populates="itens")
    produto = relationship("Produto", back_populates="itens_mesa", uselist=False)


