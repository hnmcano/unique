from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtNetwork import QNetworkAccessManager
from telas.form_clients.clientes_ui import Ui_MainWindow as clientes
from scripts.clientes import salvar_dados_clientes
from scripts.produtos import exibir_confirmacao_exclusao
from scripts.api_externa import buscar_cep

class Clientes(QMainWindow, clientes):
    janela_fechada = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)# type: ignore

        # Ao clicar no botão buscar CEP, Aciona a função de buscar CEP localizada em scripts/aux_func.py
        self.btn_viacep.clicked.connect(lambda: buscar_cep(self))
        # Gerenciador de rede para requisições HTTP
        self.network_manager = QNetworkAccessManager(self)
        # Ao clicar no botão salvar, Aciona a função de salvar dados clientes localizada em scripts/aux_func.py
        self.cad_clientes.clicked.connect(lambda: salvar_dados_clientes(self))
        # Ao clicar no botão cancelar, Aciona a função de confirmação de exclusão localizada em scripts/aux_func.py
        self.cancelar.clicked.connect(lambda: exibir_confirmacao_exclusao(self))
