from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func
from bd.connection import Base

class Caixa(Base):
    __tablename__ = "caixa"

    id = Column(Integer, primary_key=True, nullable=False)
    data_abertura = Column(DateTime(timezone=True), server_default=func.now())
    status = Column(String(50), default="ABERTO" )
    valor = Column(Float, nullable=False)

    pedido = relationship("Pedido", back_populates="caixa")
    mesa = relationship("Mesas", back_populates="caixa")

    def __repr__(self):
        return f"Caixa(id={self.id}, data_abertura={self.data_abertura}, status={self.status}, valor={self.valor})"