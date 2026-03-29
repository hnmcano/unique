import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy import Column, String, text, DateTime, ForeignKey, Boolean
from database.connection import Base
from datetime import datetime

class Usuarios(Base):
    __tablename__ = 'usuarios'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4,server_default=text("gen_random_uuid()"), nullable=False)
    estabelecimento_id = Column(UUID(as_uuid=True), ForeignKey('estabelecimentos.id'), nullable=False, index=True)
    nome = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)
    senha_hash = Column(String(200), nullable=False)
    ativo = Column(Boolean, default=True)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())
    atualizado_em = Column(DateTime(timezone=True), onupdate=func.now())

>>>>>>> 182d746 (Versão atual da infra com backend da VM)
    estabelecimento = relationship("Estabelecimento", back_populates="usuarios")