from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from windows.form_delivery.delivery_ui import Ui_MainWindow as delivery
from .DadosPedido import DadosPedido
from services.websocket import WebSocketService, PedidoStore
from PySide6.QtNetwork import *
from PySide6.QtMultimedia import *
from ..produtos.Produtos import FloatQtTableWidget, NumericQtTableWidget
from core.app_context import app_context as APPContext

import requests
from datetime import datetime
import os
from config.config import settings

class Pedidos(QMainWindow, delivery):
    def __init__(self, pedido_store, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.layout_tabela()
        self.tableWidget.cellDoubleClicked.connect(self.abrir_dados_pedido)

        self.pedido_store = pedido_store
        pedidos = self.pedido_store.listar()

        menor_data = None
        maior_data = None

        if pedidos:
            menor_data = min(p["data_criacao"] for p in pedidos)
            maior_data = max(p["data_criacao"] for p in pedidos)

        print(menor_data, maior_data)
        
        if maior_data:
            pedidos_novos = APPContext.api_client.get(
                f"/pedidos/desktop/tabela?after={maior_data}"
            )
        else:
            pedidos_novos = APPContext.api_client.get(
                "/pedidos/desktop/tabela"
            )

        if menor_data:
            pedidos_anteriores = APPContext.api_client.get(
                f"/pedidos/desktop/tabela?before={menor_data}"
            )
        else:
            pedidos_anteriores = []

        for pedidos in pedidos_novos + pedidos_anteriores:
            self.pedido_store.adicionar(pedidos)

        pedidos = self.pedido_store.listar()
        self.atualizar_tabela(pedidos)

    def layout_tabela(self):

        self.FilterPedidos.setPlaceholderText("Pesquisar pedidos realizados.....")

        columns = [ "nome_cliente", "telefone", "data_pedido", "hora_pedido", "status", "valor_total"]

        quantidade_columns = len(columns)

        self.FilterPedidos.textChanged.connect(self.filtrar_produtos)
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

        for index, pedido in enumerate(data):
            
            item_nome = QTableWidgetItem(str(pedido["cliente"]["nome"]))
            item_nome.setData(Qt.UserRole + 1, pedido)
            item_nome.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            self.tableWidget.setItem(index, 0, item_nome)

            item_telefone = QTableWidgetItem(str(pedido["cliente"]["telefone"]))
            item_telefone.setTextAlignment(Qt.AlignCenter)
            self.tableWidget.setItem(index, 1, item_telefone)

            item_data_pedido = QTableWidgetItem(datetime.fromisoformat(pedido["data_criacao"]).strftime("%d/%m/%Y"))
            item_data_pedido.setTextAlignment(Qt.AlignCenter)
            self.tableWidget.setItem(index, 2, item_data_pedido)

            item_hora_pedido = QTableWidgetItem(datetime.fromisoformat(pedido["data_criacao"]).strftime("%H:%M:%S"))
            item_hora_pedido.setTextAlignment(Qt.AlignCenter)
            self.tableWidget.setItem(index, 3, item_hora_pedido)

            item_status = QTableWidgetItem(str(pedido["status"]))
            item_status.setTextAlignment(Qt.AlignCenter)
            self.tableWidget.setItem(index, 4, item_status)

            item_valor = FloatQtTableWidget(str(pedido["valor_total"]))
            item_valor.setData(Qt.UserRole, float(pedido["valor_total"]))
            item_valor.setTextAlignment(Qt.AlignCenter)
            self.tableWidget.setItem(index, 5, item_valor)

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
