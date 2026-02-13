from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from telas.form_delivery.delivery_ui import Ui_MainWindow as delivery
from .DadosPedido import DadosPedido
from services.websocket import WebSocketService
from PySide6.QtNetwork import *
from PySide6.QtMultimedia import *

import requests
from datetime import datetime

APIURLDESENV = "http://localhost:8000"


class Pedidos(QMainWindow, delivery):
    mensagem_recebida = Signal(dict)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.FilterPedidos.setPlaceholderText("Pesquisar pedidos realizados.....")

        columns = ["id_pedido", "nome_cliente", "telefone", "data_pedido", "hora_pedido", "status", "valor_total"]

        quantidade_columns = len(columns)

        self.tableWidget.setColumnCount(quantidade_columns)
        self.tableWidget.setHorizontalHeaderLabels(columns)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Interactive)
        self.tableWidget.setShortcutEnabled(True)
        header.setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableWidget.setSelectionMode(QTableWidget.SingleSelection)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.tableWidget.cellClicked.connect(self.abrir_dados)


    def atualizar_tabela(self, pedidos):
        print(pedidos)



    def abrir_dados(self, row, column):
        self.dados_pedidos = DadosPedido(row=row, column=column, parent=self)
        self.dados_pedidos.show()
