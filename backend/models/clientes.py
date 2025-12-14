from sqlalchemy import Column, Integer, String, Float
from bd.connection import Base
from sqlalchemy.orm import relationship


class Clientes(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    telefone = Column(String(11), nullable=False)

    pedidos = relationship("Pedido", back_populates="cliente")

    def __repr__(self):
        return f"Cliente(id={self.id}, nome={self.nome}, email={self.email}, telefone={self.telefone})"
    
