from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from windows.form_clients.clientes_ui import Ui_MainWindow
from .AddClientes import AddClientes

def center_window(self):

    screen = QGuiApplication.primaryScreen()
    screen_geometry = screen.availableGeometry()
    window_geometry = self.frameGeometry()

    window_geometry.moveCenter(screen_geometry.center())
    self.move(window_geometry.topLeft())

class Clientes(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        center_window(self)

        self.add_clientes.clicked.connect(self.adicionar_clientes)

    def layout_tabela(self):

        columns = ["nome", "telefone", "email", "cpf"]

        # self.tableWidget.setColumnCount(len(columns))
        # self.tableWidget.setHorizontalHeaderLabels(columns)
        # header = self.tableWidget.horizontalHeader()
        # header.setSectionResizeMode(QHeaderView.Stretch)

    # def atualizar_tabela(self, data):

    
    # def on_evento_recebido(self, evento: dict):
    #     data = evento["dados"]

    #     if evento["tipo"] == "Atualizar_clientes":
    #         # Se vier um dicionário único, transformamos em lista
    #         if isinstance(data, dict):
    #             data = [data]

    #         self.atualizar_tabela(data)

    def adicionar_clientes(self):
        self.add_clientes_window = AddClientes(self)
        self.add_clientes_window.show()