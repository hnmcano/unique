import uuid
from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.sql import func
from sqlalchemy.orm import Session, relationship
from sqlalchemy import Column, Integer, String, Boolean, DateTime, text
from database.connection import Base


class Estabelecimento(Base):
    __tablename__ = 'estabelecimentos'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=text("gen_random_uuid()"), index=True)

    nome = Column(String(200), nullable=False)
    nome_fantasia = Column(String(200))

    documento = Column(String(20), unique=True, index=True)

    telefone = Column(String(20))
    email = Column(String(200))

    logo_img = Column(String)
    endereco = Column(String(300))
    rede_social = Column(String(300))

    plano = Column(String(50), default="basico")
    limite_usuarios = Column(Integer, default=1)

    ativo = Column(Boolean, default=True)
    data_expiracao = Column(DateTime(timezone=True))

    subdominio = Column(String(100), unique=True, index=True)

    criado_em = Column(DateTime(timezone=True), server_default=func.now())
    atualizado_em = Column(DateTime(timezone=True), onupdate=func.now())

    usuarios = relationship("Usuarios", back_populates="estabelecimento")
    pedido = relationship("Pedido", back_populates="estabelecimento")
