from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from telas.form_delivery.delivery_ui import Ui_MainWindow as delivery
from .DadosPedido import DadosPedido
from services.websocket import WebSocketService, PedidoStore
from PySide6.QtNetwork import *
from PySide6.QtMultimedia import *

import requests
from datetime import datetime

APIURLDESENV = "http://localhost:8000"


class Pedidos(QMainWindow, delivery):
    def __init__(self, pedido_store, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.layout_tabela()
        self.tableWidget.cellDoubleClicked.connect(self.abrir_dados_pedido)

        self.pedido_store = pedido_store
        pedidos = self.pedido_store.listar()
        print("todos os pedidos", pedidos)
        self.atualizar_tabela(pedidos)

    def layout_tabela(self):

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

        
    def atualizar_tabela(self, data):
        self.tableWidget.setRowCount(len(data))
        
        for index, pedido in enumerate(data):
            self.tableWidget.setItem(index, 0, QTableWidgetItem(str(pedido["id"])))
            self.tableWidget.setItem(index, 1, QTableWidgetItem(str(pedido["cliente"]["nome"])))
            self.tableWidget.setItem(index, 2, QTableWidgetItem(str(pedido["cliente"]["telefone"])))
            self.tableWidget.setItem(index, 3, QTableWidgetItem(str(pedido["data_criacao"])))
            self.tableWidget.setItem(index, 5, QTableWidgetItem(str(pedido["status"])))
            self.tableWidget.setItem(index, 6, QTableWidgetItem(str(pedido["valor_total"])))

    def abrir_dados_pedido( self, row, column):
        self.dados_pedidos = DadosPedido(row=row, column=column, parent=self)
        self.dados_pedidos.show()

        
