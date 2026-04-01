
from windows.form_delivery.add_produtos_ui import Ui_MainWindow as addProdutosPedido
from core.app_context import app_context as APPContext
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt

import requests
import json
import os
from config.config import settings


class AdicionarProdutoPedido(QMainWindow, addProdutosPedido):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.data = data

        columns = ["nome", "preco", ""]

        self.buscar_produtos(data, columns)

        produtos = APPContext.api_client.get("/pedidos/desktop/add-produto")

        self.atualizar_tabela(produtos, data)

    def filtrar_produtos(self, text):
        for row in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(row, 0)
            if text.lower() in item.text().lower():
                self.tableWidget.showRow(row)
            else:
                self.tableWidget.hideRow(row)

    def adicionar_produto(self, row, data):
        print("Adicionar produto na linha:", row)
        print("Data recebida:", data)
        try:
            produto = self.tableWidget.item(row, 0).data(Qt.UserRole)
            pedido_id = data["id_pedido"]
            data_json = {
                    "pedido_id": f"{pedido_id}",
                    "produto_id": f"{produto["id"]}",
                    "quantidade": 1,
                    "valor_unitario": f"{produto['preco_venda']}"
            }
            
            response = APPContext.api_client.put("/pedidos/desktop/adicionar-produto", data_json)

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
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
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
            btn_adicionar.setStyleSheet("""
                                        QPushButton {
                                            background-color: green; 
                                            border: none; 
                                            color: white; 
                                            font-size: 20px; 
                                            max-width: 30px; 
                                            height: 30px;
                                            border-radius: 5px;
                                        }
                                        QPushButton:hover {
                                            background-color: darkgreen;
                                        }
                                        """)
