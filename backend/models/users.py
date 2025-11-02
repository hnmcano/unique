from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Iserção da tabela de usuários no banco de dados
class User(Base):
    __tablename__ = "users"
    
    cliente = Column(String(100), nullable=False)
    telefone = Column(String(11), primary_key=True, nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    cep = Column(String(8), nullable=False)
    endereco = Column(String(200), nullable=False)
    bairro = Column(String(100), nullable=False)
    cidade = Column(String(100), nullable=False)
    complemento = Column(String(200), nullable=False)
    referencia = Column(String(200), nullable=True)
