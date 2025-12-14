from sqlalchemy import Column, Integer, String, Float, ForeignKey
from typing import List
from sqlalchemy.orm import relationship, Mapped
from bd.connection import Base

# Iserção da tabela de categorias no banco de dados
class Categoria(Base):

    __tablename__ = "categorias"

    id: int = Column(Integer, primary_key=True, nullable=False)
    nome: str = Column(String(30), unique=True, nullable=False)

    produtos: Mapped[List["Produto"]] = relationship("Produto", back_populates="categoria_object")

    def __repr__(self):
        return f"Category(id={self.id}, name={self.nome})"
    

# Iserção da tabela de produtos no banco de dados
class Produto(Base):
    __tablename__ = "produtos"
    
    id: int = Column(Integer, primary_key=True, nullable=False)
    categoria_id = Column(Integer, ForeignKey("categorias.id"), nullable=False)
    cod_pdv = Column(String(20), unique=True, nullable=False)
    nome = Column(String(80), nullable=False)
    preco_custo = Column(Float, nullable=False)
    preco_venda = Column(Float, nullable=False)
    medida = Column(String(2), nullable=False)
    estoque = Column(Integer, nullable=False)
    estoque_min = Column(Integer, nullable=False)
    sit_estoque = Column(String(50), default="Regular", nullable=False)
    descricao = Column(String(300), nullable=True)
    ficha_tecnica = Column(String(300), nullable=True)
    status_venda = Column(String(20), nullable=False)
    imagem_url = Column(String(300), nullable=True)

    categoria_object = relationship("Categoria", back_populates="produtos")

    def __repr__(self):
        return f"Product(id={self.id}, name={self.nome})"

