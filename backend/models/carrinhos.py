from sqlalchemy import Column, Integer, String, Float
from bd.connection import Base

class Carrinho(Base):
    __tablename__ = "carrinhos"
    produto_id = Column(Integer, primary_key=True, nullable=False)
    cod_pdv = Column(String(20), nullable=False)
    categoria = Column(String(30), nullable=False)
    nome = Column(String(80), nullable=False)
    preco_custo = Column(Float, nullable=False)
    preco_venda = Column(Float, nullable=False)
    medida = Column(String(2), nullable=False)
    estoque = Column(Integer, nullable=False)
    estoque_min = Column(Integer, nullable=False)
    sit_estoque = Column(String(50), nullable=False)
    descricao = Column(String(300), nullable=False)
    ficha_tecnica = Column(String(300), nullable=True)
    status_venda = Column(String(20), nullable=False)
    imagem_url = Column(String, nullable=True)
    quantidade = Column(Integer, default=1, nullable=False)
