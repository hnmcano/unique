from PySide6.QtWidgets import QMainWindow 
from PySide6.QtGui import QGuiApplication

from telas.form_products.produtos_ui import Ui_MainWindow as produtos

from .DadosProdutos import DadosProduto
from .AddCategoria import AddCategoria
from .Addprodutos import AddProdutos

from scripts.produtos import buscar_produtos

from PySide6.QtCore import Qt

def center_window(self):

    screen = QGuiApplication.primaryScreen()
    screen_geometry = screen.availableGeometry()
    window_geometry = self.frameGeometry()

    window_geometry.moveCenter(screen_geometry.center())
    self.move(window_geometry.topLeft())


class Produtos(QMainWindow, produtos):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        center_window(self)

        columns = ["ID","CODIGO PDV", "CATEGORIA", "NOME", "PREÇO DE CUSTO", "PREÇO DE VENDA","ESTOQUE MIN", "ESTOQUE", "MEDIDA", "STATUS"]
        # Esconde o botão do windows de fechar(X) a janela
        self.tableWidget.cellClicked.connect(self.abrir_dados_produto)
        buscar_produtos(self, columns)

        # Ao clicar no botão adicionar produto, abre a janela de adicionar produtos
        self.add_products.clicked.connect(self.abrir_add_produto)
        self.add_categoria.clicked.connect(self.abrir_categoria)

    def abrir_add_produto(self):
        self.add_produto_window = AddProdutos(parent=self)# type: ignore
        self.add_produto_window.show()# type: ignore

    def abrir_dados_produto(self, row, column):
        item = self.tableWidget.item(row, 0)
        produto = item.data(Qt.UserRole)
        self.dados_produto_window = DadosProduto(produto=produto, parent=self)
        self.dados_produto_window.show()

    def abrir_categoria(self):
        self.categoria_window = AddCategoria(parent=self)
        self.categoria_window.show()

    def filtrar_produtos(self, text):
        for row in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(row, 3)
            if text.lower() in item.text().lower():
                self.tableWidget.showRow(row)
            else:
                self.tableWidget.hideRow(row)
