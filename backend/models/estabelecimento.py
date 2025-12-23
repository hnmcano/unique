from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String, Text
from bd.connection import Base


class Estabelecimento(Base):
    __tablename__ = 'estabelecimento'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    endereco = Column(String(200), nullable=False)
    instagram = Column(String(100), nullable=True)
    telefone = Column(String(15), nullable=False)
    logo_base64 = Column(Text, nullable=True)
