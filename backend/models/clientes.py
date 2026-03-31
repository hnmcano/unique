from sqlalchemy import Column, Integer, String, Float, ForeignKey, text
from database.connection import Base
from sqlalchemy.orm import relationship
import uuid
from sqlalchemy.dialects.postgresql import UUID

class Clientes(Base):
    __tablename__ = 'clientes'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=text("gen_random_uuid()"), nullable=False, index=True)
    estabelecimento_id = Column(UUID(as_uuid=True), ForeignKey('estabelecimentos.id'), nullable=False, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    telefone = Column(String(11), nullable=False)
    cpf = Column(String(30))

    pedidos = relationship("Pedido", back_populates="cliente")

    def __repr__(self):
        return f"Cliente(id={self.id}, nome={self.nome}, email={self.email}, telefone={self.telefone})"
