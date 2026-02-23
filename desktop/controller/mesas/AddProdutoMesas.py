
from windows.form_orders.add_produtos_ui import Ui_MainWindow as addProdutosMesa
from core.app_context import app_context as APPContext
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt

import requests
import json
import os
from config.config import settings


class AdicionarProdutoMesa(QMainWindow, addProdutosMesa):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.data = data

        columns = ["nome", "preco", ""]

        self.buscar_produtos(data, columns)

        produtos = APPContext.api_client.get("/mesas/add-produto")

        self.atualizar_tabela(produtos, data)

    def filtrar_produtos(self, text):
        for row in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(row, 1)
            if text.lower() in item.text().lower():
                self.tableWidget.showRow(row)
            else:
                self.tableWidget.hideRow(row)

    def adicionar_produto(self, row, data):
        try:
            produto = self.tableWidget.item(row, 0).data(Qt.UserRole)
            mesa_id = data["id_mesa"]
            data_json = {
                    "mesa_id": f"{mesa_id}",
                    "produto_id": f"{produto["id"]}",
                    "quantidade": 1,
                    "valor_unitario": f"{produto['preco_venda']}"
            }
            
            response = APPContext.api_client.put("/mesas/adicionar-produto", data_json)

            QMessageBox.information(self, "Sucesso", "Produto adicionado com sucesso!")

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao adicionar produto: {str(e)}")


    def buscar_produtos(self, data, columns=None):
        
        self.FilterProducts.setPlaceholderText("Digite para filtrar produtos...")

        self.FilterProducts.textChanged.connect(self.filtrar_produtos)

        quantidade_columns = len(columns)
        self.tableWidget.setColumnCount(quantidade_columns)
        self.tableWidget.setHorizontalHeaderLabels(columns)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Interactive)
        self.tableWidget.setSortingEnabled(True)
        header.setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableWidget.setSelectionMode(QTableWidget.SingleSelection)

        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)    

    def atualizar_tabela(self, produtos=None, data=None):

        if isinstance(produtos, str):
            produtos = json.loads(produtos)

        self.tableWidget.setRowCount(len(produtos))
        
        for i, prod in enumerate(produtos):
            
            item_nome = QTableWidgetItem(prod["nome"])
            item_nome.setData(Qt.UserRole, prod)
            item_nome.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            self.tableWidget.setItem(i, 0, item_nome)

            item_preco = QTableWidgetItem(str(prod["preco_venda"]))
            item_preco.setTextAlignment(Qt.AlignCenter)
            self.tableWidget.setItem(i, 1, item_preco)

            btn_adicionar = QPushButton("+")
            self.tableWidget.setCellWidget(i, 2, btn_adicionar)

            btn_adicionar.clicked.connect(lambda _, row=i: self.adicionar_produto(row, data=data))
