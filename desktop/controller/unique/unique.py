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
from config.config import settings

from core.app_context import app_context as APPContext
import os

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

        caminho = os.path.abspath("Sound/notificacao.wav")

        self.notificacao.setSource(QUrl.fromLocalFile(caminho))
        self.notificacao.setVolume(0.8)

    def play(self):
        self.notificacao.play()

# classe principal da aplicação
class Uniq(QMainWindow, uniq):

    def __init__(self):
        # inicializa a classe pai
        super().__init__()
        # instancia a interface do uniq
        self.setupUi(self)
        center_window(self)
        self.valid_caixa()

        data = self.dados_cliente()
        self.IdUsuario.setText(f"ID USUARIO: {data['id']}")
        self.BemVindo.setText(f"Seja bem vindo, {data['nome']}")
        
        self.sound = SoundService()
        self.pedido_store = PedidoStore()
        self.websocket = APPContext.websocket_client
        self.websocket = APPContext.websocket_client
        self.websocket.status.connect(self.atualizar_status)

        # sincroniza estado atual
        self.atualizar_status(self.websocket.status_atual)
        self.websocket.mensagem_recebida.connect(self.on_evento_recebido)


        self.btn_venda.clicked.connect(
            lambda: self.StackedWidgetVendas.setCurrentWidget(self.WidgetVendas)
        )
        self.btn_relatorios.clicked.connect(
            lambda: self.StackedWidgetVendas.setCurrentWidget(self.WidgetRelatorios)
        )

       # Inicializa as janelas como None
        self.caixa_window = None
        self.mesas_window = None
        self.clientes_window = None
        self.produtos_window = None
        self.delivery_window = None
        self.painel_config_window = None
        self.estabelecimento_window = None
        
        # Ao clicar nos botões, abre as respectivas janelas

        self.btn_clientes.clicked.connect(self.abrir_clientes)
        self.btn_mesas.clicked.connect(self.abrir_mesas)
        self.btn_produtos.clicked.connect(self.abrir_produtos)
        self.btn_delivery.clicked.connect(self.abrir_delivery)
        self.btn_caixa.clicked.connect(self.abrir_caixa)
        self.btn_estabelecimento.clicked.connect(self.abrir_estabelecimento)
        self.btn_config.clicked.connect(self.painel_config)

    
    # Funções para abrir a janela filhas de mesas, clientes e produtos
    def abrir_caixa(self):
        if self.caixa_window is None:
            self.caixa_window = Caixa(parent=self)

        self.caixa_window.showNormal()
        self.caixa_window.raise_()
        self.caixa_window.activateWindow()

    # considerando que a janela Uniq é a janela pai, que ao fechada, fecha as janelas filhas
    def abrir_mesas(self):
        if self.mesas_window is None:
            self.mesas_window = Mesas(parent=self)

        self.mesas_window.showNormal()
        self.mesas_window.raise_()
        self.mesas_window.activateWindow()

    def abrir_clientes(self):
        if self.clientes_window is None:
            self.clientes_window = Clientes(parent=self)
        
        self.clientes_window.showNormal()
        self.clientes_window.raise_()
        self.clientes_window.activateWindow()

    def abrir_produtos(self):
        if self.produtos_window is None:
            self.produtos_window = Produtos(parent=self)
        
        self.produtos_window.showNormal()
        self.produtos_window.raise_()
        self.produtos_window.activateWindow()

    def abrir_delivery(self):
        if self.delivery_window is None:
            self.delivery_window = Pedidos(pedido_store=self.pedido_store, parent=self)

        self.delivery_window.showNormal()
        self.delivery_window.raise_()
        self.delivery_window.activateWindow()

    def painel_config(self):
        if self.painel_config_window is None:
            self.painel_config_window = PainelConfig(parent=self)

        self.painel_config_window.showNormal()
        self.painel_config_window.raise_()
        self.painel_config_window.activateWindow()

    def abrir_estabelecimento(self):
        if self.estabelecimento_window is None:
            self.estabelecimento_window = Estabelecimento(parent=self)
        
        self.estabelecimento_window.showNormal()
        self.estabelecimento_window.raise_()
        self.estabelecimento_window.activateWindow()

    def valid_caixa(self):
        try:
            response = APPContext.api_client.get("caixa/valid_box")
            tempo_aberto = response.get("detail")
            QMessageBox.information(self, "Caixa Aberto", f"Seu caixa esta aberto há {tempo_aberto}")
        except:
            QMessageBox.information(self, "Caixa Fechado", "Seu caixa esta fechado, por favor abra-o")

    def dados_cliente(self):
        try:
            response = APPContext.api_client.get("/usuarios/dados")
            return response
        except:
            QMessageBox.information(self, "Dados Incorretos", "Não localizamos o usuario na base de dados!")

    def on_evento_recebido(self, evento):
        if evento["tipo"] == "delivery_acionado":
            self.sound.play()
            print("Delivery acionado")
            pedido = evento["dados"]
            self.pedido_store.adicionar(pedido)

    def atualizar_status(self, status):
        print("Atualizando status:", status)
        if status == "conectado":
            self.labelStatus.setText("Status: 🟢Conectado")
        else:
            self.labelStatus.setText("Status: 🔴Desconectado")
