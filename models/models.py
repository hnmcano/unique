# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Unique.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Clientes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente = db.Column(db.String(50), nullable=False)
    telefone = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    cep = db.Column(db.String, nullable=False)
    endereco = db.Column(db.String(50), nullable=False)
    bairro = db.Column(db.String(50), nullable=False)
    cidade = db.Column(db.String(50), nullable=False)
    complemento = db.Column(db.String(50), nullable=False)
    referencia = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<cliente {self.cliente}'

class Produtos(db.Model):
    Cod_PDV = db.Column(db.Integer, primary_key=True)
    Cod_Sistema = db.Column(db.Integer)
    Categoria = db.Column(db.String(50), nullable=False)
    Nome = db.Column(db.String(50), nullable=False)
    Preço_Custo = db.Column(db.String(50), nullable=False)
    Preço_Venda = db.Column(db.String(50), nullable=False)
    Medida = db.Column(db.String(50), nullable=False)
    Estoque = db.Column(db.Integer)
    Estoque_Min = db.Column(db.Integer)
    Sit_Estoque = db.Column(db.String(50), nullable=False)
    Ficha_Tecnica = db.Column(db.String(50))
    Status_Venda = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<produto {self.Nome}'

def inicializar_banco():
    with app.app_context():
        db.create_all()

def adicionar_novo_usuario(cliente, telefone, email,
                            cep, endereco, bairro, cidade,
                                complemento, referencia):
    with app.app_context():
        novo_cliente = Clientes(cliente=cliente, telefone=telefone, email=email, cep=cep, endereco=endereco,
        bairro=bairro, cidade=cidade, complemento=complemento, referencia=referencia)
        db.session.add(novo_cliente)
        db.session.commit()

def adicionar_novo_produto(Cod_PDV, Cod_Sistema, Categoria, Nome,
                                Preço_Custo, Preço_Venda, Medida, Estoque,
                                    Estoque_Min, Sit_Estoque,Ficha_Tecnica, Status_Venda):
    with app.app_context():
        novo_produto = Produtos(Cod_PDV=Cod_PDV, Cod_Sistema=Cod_Sistema, Categoria=Categoria, Nome=Nome,
                                    Preço_Custo=Preço_Custo, Preço_Venda=Preço_Venda, Medida=Medida,Estoque=Estoque,
                                            Estoque_Min=Estoque_Min, Sit_Estoque=Sit_Estoque,Ficha_Tecnica=Ficha_Tecnica, Status_Venda=Status_Venda)
        db.session.add(novo_produto)
        db.session.commit()

def listar_clientes():
    with app.app_context():
        return Clientes.query.all()

def listar_produtos():
    with app.app_context():
        return Produtos.query.all()
