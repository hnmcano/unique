from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from telas.form_delivery.delivery_ui import Ui_MainWindow as delivery
from .DadosPedido import DadosPedido

import requests
from datetime import datetime

APIURLDESENV = "http://localhost:8000"


class Pedidos(QMainWindow, delivery):
    resposta_delivery = Signal(str)

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

        try:
            response = requests.get(f"{APIURLDESENV}/pedidos/delivery/desktop")
            pedidos = response.json().get("detail")

            if response.status_code == 200:               
                self.tableWidget.setRowCount(len(pedidos))
                linha_atual = 0

                for i in pedidos:
                    self.tableWidget.setRowHeight(linha_atual, 50)

                    item_ordenavel_id = QTableWidgetItem(str(i["id"]))
                    self.tableWidget.setItem(linha_atual, 0, item_ordenavel_id)

                    item_ordenavel_nome = QTableWidgetItem(i["nome"])
                    self.tableWidget.setItem(linha_atual, 1, item_ordenavel_nome)

                    item_ordenavel_telefone = QTableWidgetItem(str(i["telefone"]))
                    self.tableWidget.setItem(linha_atual, 2, item_ordenavel_telefone)

                    item_ordenavel_data_pedido = QTableWidgetItem(i["data_pedido"])
                    self.tableWidget.setItem(linha_atual, 3, item_ordenavel_data_pedido)

                    item_ordenavel_hora_pedido = QTableWidgetItem(str(i["hora_pedido"]))
                    self.tableWidget.setItem(linha_atual, 4, item_ordenavel_hora_pedido)

                    item_ordenavel_status = QTableWidgetItem(i["status"])
                    self.tableWidget.setItem(linha_atual, 5, item_ordenavel_status)

                    item_ordenavel_valor_total = QTableWidgetItem(str(i["valor_total"]))
                    self.tableWidget.setItem(linha_atual, 6, item_ordenavel_valor_total)

                    linha_atual += 1
                
                self.tableWidget.sortItems(0, Qt.AscendingOrder)
            else:
                self.tableWidget.setRowCount(0)
                                
        except requests.RequestException as e:
            QMessageBox.critical(self, "Erro", f"Erro ao buscar pedidos: {str(e)}")

    def abrir_dados(self, row, column):
        self.dados_pedidos = DadosPedido(row=row, column=column, parent=self)
        self.dados_pedidos.show()
