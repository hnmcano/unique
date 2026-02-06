from PySide6.QtWidgets import *
from telas.form_delivery.dados_pedidos_ui import Ui_MainWindow as dados_pedidos

class DadosPedido(QMainWindow, dados_pedidos):
    def __init__(self, row, column, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.row = row
        self.column = column
