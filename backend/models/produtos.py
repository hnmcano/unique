from sqlalchemy import Column, Integer, String, Float, ForeignKey, text, UniqueConstraint
from typing import List
from sqlalchemy.orm import relationship, Mapped
from database.connection import Base
import uuid
from sqlalchemy.dialects.postgresql import UUID

# Iserção da tabela de categorias no banco de dados
class Categoria(Base):

    __tablename__ = "categorias"

    id_categoria = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4,server_default=text("gen_random_uuid()"), nullable=False)
    estabelecimento_id = Column(UUID(as_uuid=True), ForeignKey("estabelecimentos.id"), nullable=False, index=True)
    nome = Column(String(30), nullable=False)

    __table_args__ = (
        UniqueConstraint('estabelecimento_id', 'nome', name='uix_categoria_nome_estabelecimento'),
    )

    produtos: Mapped[List["Produto"]] = relationship("Produto", back_populates="categoria_object")

    def __repr__(self):
        return f"Category(id={self.id}, name={self.nome})"
    
# Iserção da tabela de produtos no banco de dados
class Produto(Base):
    __tablename__ = "produtos"
    
    id_produto = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=text("gen_random_uuid()"), nullable=False)
    estabelecimento_id = Column(UUID(as_uuid=True), ForeignKey("estabelecimentos.id"), nullable=False, index=True)
    categoria_id = Column(UUID(as_uuid=True), ForeignKey("categorias.id_categoria"), nullable=False)
    cod_pdv = Column(String(20), nullable=False)
    __table_args__ = (
        UniqueConstraint('estabelecimento_id', 'cod_pdv', name='uix_cod_pdv_estabelecimento'),
    )
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
    imagem_name = Column(String(300), nullable=True)
    imagem = Column(String, nullable=True)
    dias_vendas = Column(Integer, nullable=True)

    categoria_object = relationship("Categoria", back_populates="produtos")
    tamanhos_object = relationship("Tamanhos", back_populates="produto", cascade="all, delete-orphan")
    itens_mesa = relationship("PedidoItens", back_populates="produto")
    itens_pedidos = relationship("ItemPedido", back_populates="produtos")


    def __repr__(self):
        return f"Product(id={self.id}, name={self.nome})"

class Tamanhos(Base):
    __tablename__ = "aux_tamanhos"

    tamanho_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=text("gen_random_uuid()"), nullable=False)
    produto_id = Column(UUID(as_uuid=True), ForeignKey("produtos.id_produto"), nullable=False)
    estabelecimento_id = Column(UUID(as_uuid=True), ForeignKey("estabelecimentos.id"), nullable=False, index=True)
    tamanho = Column(String(300), nullable=True)
    valor = Column(Float, nullable=True)

    __table_args__ = (
        UniqueConstraint('produto_id', 'tamanho', name='uix_tamanho_produto'),
    )

    produto = relationship("Produto", back_populates="tamanhos_object")
