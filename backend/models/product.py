from sqlalchemy import Column, Integer, String, Float, ForeignKey
from typing import List
from sqlalchemy.orm import declarative_base, relationship, Mapped

Base = declarative_base()

# Iserção da tabela de categorias no banco de dados
class Category(Base):

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

    categoria_object = relationship("Category", back_populates="produtos")

    def __repr__(self):
        return f"Product(id={self.id}, name={self.nome})"


# Acesso a View produtos_com_categorias, onde no sqlite3 é feito um join entre as duas tabelas
class Produtos_com_categorias(Base):

    __tablename__ = "produtos_com_categorias"

    produto_id: int = Column("produto_id", Integer, primary_key=True, nullable=False)
    codigo_pdv: str = Column("cod_pdv", String(20), nullable=False)
    nome_produto: str = Column("nome_produto", String(80), nullable=False)
    preco_custo: float = Column("preco_custo", Float, nullable=False)
    preco_venda: float = Column("preco_venda", Float, nullable=False)
    medida: str = Column("medida", String(2), nullable=False)
    estoque: int = Column("estoque", Integer, nullable=False)
    estoque_min: int = Column("estoque_min", Integer, nullable=False)
    sit_estoque: str = Column("sit_estoque", String(50), default="Regular", nullable=False)
    descricao: str = Column("descricao", String(300), nullable=True)
    ficha_tecnica: str = Column("ficha_tecnica", String(300), nullable=True)
    status_venda: str = Column("status_venda", String(20), nullable=False)
    imagem_url: str = Column("imagem_url", String(300), nullable=True)

    categoria_id: int = Column("categoria_id", Integer, nullable=False)
    nome_categoria: str = Column("nome_categoria", String(30), nullable=False)

