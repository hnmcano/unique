from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Numeric, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from bd.connection import Base
from datetime import datetime

class Pedido(Base):
    __tablename__ = 'pedidos'

    id = Column(Integer, primary_key=True, index=True)

    cliente_id = Column(Integer, ForeignKey('clientes.id'), nullable=False)
    caixa_id = Column(Integer, ForeignKey('caixa.id'), nullable=False)

    data_criacao = Column(DateTime(timezone=True), default=datetime.now)
    data_atualizacao = Column(DateTime(timezone=True), onupdate=func.now())
    status = Column(String(50), default="PENDENTE", nullable=False)
    metodo_pagamento = Column(String(50), nullable=False)
    valor_total = Column(Numeric(10, 2), nullable=False)
    observacoes = Column(Text, nullable=True)

    cliente = relationship("Clientes", back_populates="pedidos", uselist=False)
    endereco_entrega = relationship("EnderecoPedido", back_populates="pedido", cascade="all, delete-orphan")
    itens = relationship("ItemPedido", back_populates="pedido", cascade="all, delete-orphan")
    caixa = relationship("Caixa", back_populates="pedido")

    def __repr__(self):
        return f"Pedido(id={self.id}, cliente_id={self.cliente_id}, data_criacao={self.data_criacao}, data_atualizacao={self.data_atualizacao})"
    

class EnderecoPedido(Base):
    __tablename__ = 'enderecos_pedidos'

    id = Column(Integer, primary_key=True, index=True)
    pedido_id = Column(Integer, ForeignKey('pedidos.id'), unique=True, nullable=False)

    cep = Column(String(8), nullable=False)
    endereco = Column(String(200), nullable=False)
    numero = Column(Integer, nullable=False)
    bairro = Column(String(100), nullable=False)
    cidade = Column(String(100), nullable=False)
    estado = Column(String(2), nullable=False)
    complemento = Column(String(200), nullable=False)
    referencia = Column(String(200), nullable=True)

    taxa_entrega = Column(Numeric(10, 2), nullable=False)

    pedido = relationship("Pedido", back_populates="endereco_entrega")

    def __repr__(self):
        return f"EnderecoPedido(id={self.id}, cep={self.cep}, endereco={self.endereco}, bairro={self.bairro}, cidade={self.cidade}, complemento={self.complemento}, referencia={self.referencia})"
    
class ItemPedido(Base):
    __tablename__ = 'itens_pedidos'

    id = Column(Integer, primary_key=True, index=True)
    pedido_id = Column(Integer, ForeignKey('pedidos.id'), nullable=False)
    produto_id = Column(Integer, nullable=False)
    quantidade = Column(Integer, nullable=False)
    valor_unitario = Column(Numeric(10, 2), nullable=False)

    pedido = relationship("Pedido", back_populates="itens")

    def __repr__(self):
        return f"ItemPedido(id={self.id}, pedido_id={self.pedido_id},quantidade={self.quantidade}, valor_unitario={self.valor_unitario})"
