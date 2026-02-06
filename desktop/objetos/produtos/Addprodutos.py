from PySide6.QtWidgets import QMainWindow
from telas.form_products.add_produtos_ui import Ui_MainWindow as addprodutos
from .AddCategoria import AddCategoria

from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QGuiApplication
from PySide6.QtNetwork import QNetworkAccessManager

from scripts.produtos import preencher_dropdown_categoria, salvar_dados_produtos, inserir_imagem, exibir_confirmacao_exclusao

def center_window(self):

    screen = QGuiApplication.primaryScreen()
    screen_geometry = screen.availableGeometry()
    window_geometry = self.frameGeometry()

    window_geometry.moveCenter(screen_geometry.center())
    self.move(window_geometry.topLeft())


class AddProdutos(QMainWindow, addprodutos):
    janela_fechada = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        center_window(self)

        # Esconde o botão do windows de fechar(X) a janela
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)# type: ignore

        # Gerenciador de rede para requisições HTTP
        self.network_manager = QNetworkAccessManager(self)
    
        preencher_dropdown_categoria(self)
        # Ao clicar no botão selecionar imagem, Aciona a função de inserir imagem localizada em scripts/aux_func.py
        self.selecionar_imagem.clicked.connect(lambda: inserir_imagem(self))
        # Ao clicar no botão salvar, Aciona a função de salvar dados produtos localizada em scripts/aux_func.py
        self.add_produto.clicked.connect(lambda: salvar_dados_produtos(self))
        # Ao clicar no botão adicionar categoria, Aciona a função de abrir a janela de categorias localizada em scripts/aux_func.py
        self.add_categoria.clicked.connect(self.abrir_categoria)
        # Ao clicar no botão cancelar, Aciona a função de confirmação de exclusão localizada em scripts/aux_func.py
        self.cancelar.clicked.connect(lambda: exibir_confirmacao_exclusao(self))

    def abrir_categoria(self):
        self.categoria_window = AddCategoria(parent=self)# type: ignore
        self.categoria_window.show()# type: ignore
