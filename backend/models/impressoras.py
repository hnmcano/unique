from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text, text, Boolean
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func
from database.connection import Base
import uuid
from sqlalchemy.dialects.postgresql import UUID

class Impressoras(Base):
    __tablename__ = "impressoras"

    impressora_id = Column(UUID(as_uuid=True), default=uuid.uuid4, server_default=text("gen_random_uuid()"), primary_key=True, nullable=False)
    estabelecimento_id = Column(UUID(as_uuid=True), ForeignKey('estabelecimentos.id'), nullable=False, index=True)
    data_adicao = Column(DateTime(timezone=True), server_default=func.now())
    impressora = Column(String(100))
    padrao = Column(Boolean, default=False)
    tamanho = Column(String(100))
