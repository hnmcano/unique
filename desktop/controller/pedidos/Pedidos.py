from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from windows.form_delivery.delivery_ui import Ui_MainWindow as delivery
from .DadosPedido import DadosPedido
from services.websocket import WebSocketService, PedidoStore
from PySide6.QtNetwork import *
from PySide6.QtMultimedia import *
from ..produtos.Produtos import FloatQtTableWidget, NumericQtTableWidget


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

        if len(pedidos) == 0:
            response = requests.get(f"{APIURLDESENV}/pedidos/desktop/tabela")
            pedidos = response.json()

            for pedido in pedidos:
                self.pedido_store.adicionar(pedido)

        self.atualizar_tabela(pedidos)

    def layout_tabela(self):

        self.FilterPedidos.setPlaceholderText("Pesquisar pedidos realizados.....")

        columns = ["id_pedido", "nome_cliente", "telefone", "data_pedido", "hora_pedido", "status", "valor_total"]

        quantidade_columns = len(columns)

        self.FilterPedidos.textChanged.connect(self.filtrar_produtos)
        quantidade_columns = len(columns)
        self.tableWidget.setColumnCount(quantidade_columns)
        self.tableWidget.setHorizontalHeaderLabels(columns)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableWidget.setSelectionMode(QTableWidget.SingleSelection)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def atualizar_tabela(self, data):
        self.tableWidget.setRowCount(len(data))

        for index, pedido in enumerate(data):
            
            item_id = NumericQtTableWidget(str(pedido["id"]))
            item_id.setData(Qt.UserRole, int(pedido["id"]))
            item_id.setData(Qt.UserRole + 1, pedido)
            item_id.setTextAlignment(Qt.AlignCenter)
            self.tableWidget.setItem(index, 0, item_id)

            item_nome = QTableWidgetItem(str(pedido["cliente"]["nome"]))
            item_nome.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            self.tableWidget.setItem(index, 1, item_nome)

            item_telefone = QTableWidgetItem(str(pedido["cliente"]["telefone"]))
            item_telefone.setTextAlignment(Qt.AlignCenter)
            self.tableWidget.setItem(index, 2, item_telefone)

            item_data_pedido = QTableWidgetItem(datetime.fromisoformat(pedido["data_criacao"]).strftime("%d/%m/%Y"))
            item_data_pedido.setTextAlignment(Qt.AlignCenter)
            self.tableWidget.setItem(index, 3, item_data_pedido)

            item_hora_pedido = QTableWidgetItem(datetime.fromisoformat(pedido["data_criacao"]).strftime("%H:%M:%S"))
            item_hora_pedido.setTextAlignment(Qt.AlignCenter)
            self.tableWidget.setItem(index, 4, item_hora_pedido)

            item_status = QTableWidgetItem(str(pedido["status"]))
            item_status.setTextAlignment(Qt.AlignCenter)
            self.tableWidget.setItem(index, 5, item_status)

            item_valor = FloatQtTableWidget(str(pedido["valor_total"]))
            item_valor.setData(Qt.UserRole, float(pedido["valor_total"]))
            item_valor.setTextAlignment(Qt.AlignCenter)
            self.tableWidget.setItem(index, 6, item_valor)

    def abrir_dados_pedido(self, row):
        item = self.tableWidget.item(row, 0)
        pedido = item.data(Qt.UserRole + 1)
        self.dados_pedidos = DadosPedido(pedido=pedido, parent=self)
        self.dados_pedidos.show()
    
    def filtrar_produtos(self, text):
        for row in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(row, 1)
            if text.lower() in item.text().lower():
                self.tableWidget.showRow(row)
            else:
                self.tableWidget.hideRow(row)
