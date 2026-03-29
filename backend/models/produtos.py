<<<<<<< HEAD
from sqlalchemy import Column, Integer, String, Float, ForeignKey, text
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
    nome = Column(String(30), unique=True, nullable=False)

    produtos: Mapped[List["Produto"]] = relationship("Produto", back_populates="categoria_object")

    def __repr__(self):
        return f"Category(id={self.id}, name={self.nome})"
    

# Iserção da tabela de produtos no banco de dados
class Produto(Base):
    __tablename__ = "produtos"
    
    id_produto = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=text("gen_random_uuid()"), nullable=False)
    estabelecimento_id = Column(UUID(as_uuid=True), ForeignKey("estabelecimentos.id"), nullable=False, index=True)
    categoria_id = Column(UUID(as_uuid=True), ForeignKey("categorias.id_categoria"), nullable=False)
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
    imagem_name = Column(String(300), nullable=True)
    imagem = Column(String, nullable=True)

    categoria_object = relationship("Categoria", back_populates="produtos")
    itens_mesa = relationship("PedidoItens", back_populates="produto")
    itens_pedidos = relationship("ItemPedido", back_populates="produtos")

    def __repr__(self):
        return f"Product(id={self.id}, name={self.nome})"

=======
from sqlalchemy import Column, Integer, String, Float, ForeignKey, text
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
    nome = Column(String(30), unique=True, nullable=False)

    produtos: Mapped[List["Produto"]] = relationship("Produto", back_populates="categoria_object", order_by="Produto.id_produto")

    def __repr__(self):
        return f"Category(id={self.id}, name={self.nome})"
    

# Iserção da tabela de produtos no banco de dados
class Produto(Base):
    __tablename__ = "produtos"
    
    id_produto = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=text("gen_random_uuid()"), nullable=False)
    estabelecimento_id = Column(UUID(as_uuid=True), ForeignKey("estabelecimentos.id"), nullable=False, index=True)
    categoria_id = Column(UUID(as_uuid=True), ForeignKey("categorias.id_categoria"), nullable=False)
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
    imagem_name = Column(String(300), nullable=True)
    imagem = Column(String, nullable=True)

    categoria_object = relationship("Categoria", back_populates="produtos")
    itens_mesa = relationship("PedidoItens", back_populates="produto")
    itens_pedidos = relationship("ItemPedido", back_populates="produtos")

    def __repr__(self):
        return f"Product(id={self.id}, name={self.nome})"

>>>>>>> 182d746 (Versão atual da infra com backend da VM)
