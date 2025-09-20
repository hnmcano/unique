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

    def __repr__(self):
        return f'<cliente {self.cliente}'


def inicializar_banco():
    with app.app_context():
        db.create_all()

def adicionar_novo_usuario(cliente, telefone, email):
    with app.app_context():
        novo_cliente = Clientes(cliente=cliente, telefone=telefone, email=email)
        db.session.add(novo_cliente)
        db.session.commit()

def listar_clientes():
    with app.app_context():
        return Clientes.query.all()
