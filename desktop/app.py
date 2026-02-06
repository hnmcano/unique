from scripts.produtos import (atualizar_dados_produtos, salvar_dados_produtos, 
                              inserir_imagem, exibir_confirmacao_exclusao, 
                              adicionar_categoria, preencher_dropdown_categoria, 
                              excluir_categoria, excluir_produto_base_dados, buscar_produtos)
from scripts.estabelecimento import (enviar_dados_estabelecimento)
from scripts.clientes import (salvar_dados_clientes)
from scripts.api_externa import (buscar_cep)
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QWidget, QHeaderView, QTableWidget, QAbstractItemView

from PySide6.QtGui import QPixmap, QGuiApplication

from objetos.estabelecimento.Estabelecimento import Estabelecimento
from objetos.produtos.Produtos import Produtos
from objetos.clientes.Clientes import Clientes
from objetos.pedidos.Pedidos import Pedidos

from telas.unique_ui import Ui_Unique as uniq

from datetime import datetime, timezone
from objetos.caixa.Caixa import Caixa
from objetos.mesas.Mesas import Mesas
from PySide6.QtCore import Signal, Qt
import requests
import sys
import base64
import os

APIURLDESENV = "http://localhost:8000"

#funcao para centralizar a janelas
def center_window(self):

    screen = QGuiApplication.primaryScreen()
    screen_geometry = screen.availableGeometry()
    window_geometry = self.frameGeometry()

    window_geometry.moveCenter(screen_geometry.center())
    self.move(window_geometry.topLeft())

# classe principal da aplicação
class Uniq(QMainWindow, uniq):  
    def __init__(self):
        # inicializa a classe pai
        super().__init__()
        # instancia a interface do uniq
        self.setupUi(self)
        center_window(self)

       # Inicializa as janelas como None
        self.clientes_window = None
        self.mesas_window = None
        self.produtos_window = None

        self.valid_caixa()

        # Ao clicar nos botões, abre as respectivas janelas

        self.btn_clientes.clicked.connect(self.abrir_clientes)
        self.btn_mesas.clicked.connect(self.abrir_mesas)
        self.btn_produtos.clicked.connect(self.abrir_produtos)
        self.btn_delivery.clicked.connect(self.abrir_delivery)
        self.btn_caixa.clicked.connect(self.abrir_caixa)
        self.estabelecimento.triggered.connect(self.configuracoes_estabelecimento)

    # Funções para abrir a janela filhas de mesas, clientes e produtos
    def abrir_caixa(self):
        self.caixa_window = Caixa(parent=self)
        self.caixa_window.show()
    # considerando que a janela Uniq é a janela pai, que ao fechada, fecha as janelas filhas
    def abrir_mesas(self):
        self.mesas_window = Mesas(parent=self)
        self.mesas_window.show()

    def abrir_clientes(self):
        self.clientes_window = Clientes(parent=self)
        self.clientes_window.show()

    def abrir_produtos(self):
        self.produtos_window= Produtos(parent=self)
        self.produtos_window.show()

    def abrir_delivery(self):
        self.delivery_window = Pedidos(parent=self)
        self.delivery_window.show()

    def configuracoes_estabelecimento(self):
        self.estabelecimento_window = Estabelecimento(parent=self)
        self.estabelecimento_window.show()

    def valid_caixa(self):

        url = f"{APIURLDESENV}/caixa/valid_box"

        response = requests.get(url)

        if response.status_code == 200:
            tempo_aberto = response.json().get("detail")
            QMessageBox.information(self, "Caixa Aberto", f"Seu caixa esta aberto há {tempo_aberto}")

# funcao principal da aplicação
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Uniq()
    window.show()
    sys.exit(app.exec())