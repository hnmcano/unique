from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtMultimedia import QSoundEffect

from controller.estabelecimento.Estabelecimento import Estabelecimento
from controller.configuracao.PainelConfig import PainelConfig
from controller.produtos.Produtos import Produtos
from controller.clientes.Clientes import Clientes
from controller.pedidos.Pedidos import Pedidos
from controller.caixa.Caixa import Caixa
from controller.mesas.Mesas import Mesas
from windows.unique_ui import Ui_Unique as uniq

from services.websocket import WebSocketService 
from services.websocket import PedidoStore


import requests
import sys
import base64
import os

APIURLDESENV = os.getenv("APIURLDESENV")

#funcao para centralizar a janelas
def center_window(self):

    screen = QGuiApplication.primaryScreen()
    screen_geometry = screen.availableGeometry()
    window_geometry = self.frameGeometry()

    window_geometry.moveCenter(screen_geometry.center())
    self.move(window_geometry.topLeft())

class SoundService:
    def __init__(self):
        self.notificacao = QSoundEffect()

        caminho = os.path.abspath("desktop/Sound/notificacao.wav")

        self.notificacao.setSource(QUrl.fromLocalFile(caminho))
        self.notificacao.setVolume(0.8)

    def play(self):
        self.notificacao.play()

# classe principal da aplicação
class Uniq(QMainWindow, uniq):
    mensagem_recebida = Signal(dict)
    def __init__(self):
        # inicializa a classe pai
        super().__init__()
        # instancia a interface do uniq
        self.setupUi(self)
        center_window(self)

        self.sound = SoundService()
        self.pedido_store = PedidoStore()


       # Inicializa as janelas como None
        self.clientes_window = None
        self.mesas_window = None
        self.produtos_window = None

        self.ws = WebSocketService()
        self.ws.mensagem_recebida.connect(self.on_evento_recebido)
        self.ws.start()
        
        self.valid_caixa()

        # Ao clicar nos botões, abre as respectivas janelas

        self.btn_clientes.clicked.connect(self.abrir_clientes)
        self.btn_mesas.clicked.connect(self.abrir_mesas)
        self.btn_produtos.clicked.connect(self.abrir_produtos)
        self.btn_delivery.clicked.connect(self.abrir_delivery)
        self.btn_caixa.clicked.connect(self.abrir_caixa)
        self.btn_config.clicked.connect(self.painel_config)

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

        self.delivery_window = Pedidos(pedido_store=self.pedido_store, parent=self)
        self.delivery_window.show()

    def painel_config(self):
        self.painel_config_window = PainelConfig( parent=self)
        self.painel_config_window.show()

    def valid_caixa(self):

        url = f"{APIURLDESENV}/caixa/valid_box"

        response = requests.get(url)

        if response.status_code == 200:
            tempo_aberto = response.json().get("detail")
            QMessageBox.information(self, "Caixa Aberto", f"Seu caixa esta aberto há {tempo_aberto}")

    def on_evento_recebido(self, evento):
        if evento["tipo"] == "delivery_acionado":
            self.sound.play()
            print("Delivery acionado")
            pedido = evento["dados"]
            self.pedido_store.adicionar(pedido)
            

# funcao principal da aplicação
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Uniq()
    window.show()
    sys.exit(app.exec())