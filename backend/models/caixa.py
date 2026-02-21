from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text, text
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func
from database.connection import Base
import uuid
from sqlalchemy.dialects.postgresql import UUID

class Caixa(Base):
    __tablename__ = "caixa"

    id = Column(UUID(as_uuid=True), default=uuid.uuid4,server_default=text("gen_random_uuid()"), primary_key=True, nullable=False)
    estabelecimento_id = Column(UUID(as_uuid=True), ForeignKey('estabelecimentos.id'), nullable=False, index=True)
    data_abertura = Column(DateTime(timezone=True), server_default=func.now())
    status = Column(String(50), default="ABERTO" )
    valor = Column(Float, nullable=False)

    pedido = relationship("Pedido", back_populates="caixa")
    mesa = relationship("Mesas", back_populates="caixa")

    def __repr__(self):
        return f"Caixa(id={self.id}, data_abertura={self.data_abertura}, status={self.status}, valor={self.valor})"