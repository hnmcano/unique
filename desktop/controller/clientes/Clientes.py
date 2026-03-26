from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from windows.form_clients.clientes_ui import Ui_MainWindow
from .AddClientes import AddClientes
from core.app_context import app_context as APPContext

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
        self.layout_tabela()

        self.add_clientes.clicked.connect(self.adicionar_clientes)
        response = APPContext.api_client.get("clientes/clientes-cadastrados")
        self.atualizar_tabela(response)

    def layout_tabela(self):

        columns = ["nome", "telefone", "email", "cpf"]

        quantidade_columns = len(columns)
        self.tableWidget.setColumnCount(quantidade_columns)
        self.tableWidget.setHorizontalHeaderLabels(columns)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableWidget.setSelectionMode(QTableWidget.SingleSelection)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)


    def atualizar_tabela(self, data):
        self.tableWidget.setRowCount(len(data))
        for i, item in enumerate(data):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(item["nome"]))

            item_telefone = QTableWidgetItem(
                    f"""{
                        '('+ str(item['telefone'])[0:2] + ') ' \
                        + str(item["telefone"])[2:7] + '-' \
                        + str(item["telefone"])[7:]
                    }"""
                )
            item_telefone.setTextAlignment(Qt.AlignCenter)
            self.tableWidget.setItem(i, 1, item_telefone)

            self.tableWidget.setItem(i, 2, QTableWidgetItem(item["email"]))
            
            item_cpf = QTableWidgetItem(item["cpf"])
            item_cpf.setTextAlignment(Qt.AlignCenter)
            self.tableWidget.setItem(i, 3, item_cpf)
    
    def on_evento_recebido(self, evento: dict):
        data = evento["dados"]

        if evento["tipo"] == "Atualizar_clientes":
            # Se vier um dicionário único, transformamos em lista
            if isinstance(data, dict):
                data = [data]
            self.atualizar_tabela(data)

    def adicionar_clientes(self):
        self.add_clientes_window = AddClientes(self)
        self.add_clientes_window.show()