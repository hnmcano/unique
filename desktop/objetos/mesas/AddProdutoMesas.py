
from telas.form_orders.add_produtos_ui import Ui_MainWindow as addProdutosMesa
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt

import requests
import json

APIURLDESENV = "http://localhost:8000"


class AdicionarProdutoMesa(QMainWindow, addProdutosMesa):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        columns = ["id", "nome", "preco", ""]

        self.buscar_produtos(data, columns)

        response = requests.get(f"{APIURLDESENV}/produtos/mesa-add-product")
        response.raise_for_status()  # Levanta um erro para códigos de status HTTP ruins
        produtos = response.json()

        self.atualizar_tabela(produtos, data)

    def filtrar_produtos(self, text):
        for row in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(row, 1)
            if text.lower() in item.text().lower():
                self.tableWidget.showRow(row)
            else:
                self.tableWidget.hideRow(row)

    def adicionar_produto(self, row, data):
        produto = self.tableWidget.item(row, 0).data(Qt.UserRole)
        mesa_id = data["id"]
        response = requests.put(f"{APIURLDESENV}/mesas/adicionar-produto", 
                                 json={
                                        "mesa_id": f"{mesa_id}",
                                        "produto_id": f"{produto["id"]}",
                                        "quantidade": 1,
                                        "valor_unitario": f"{produto['preco_venda']}"
                                })

        if response.status_code == 201:
            QMessageBox.information(self, "Sucesso", "Produto adicionado com sucesso!")
        else:
            QMessageBox.critical(self, "Erro", f"Erro ao adicionar produto: {response.text}")

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

            item_id = QTableWidgetItem(str(prod["id"]))
            item_id.setData(Qt.UserRole, prod)
            item_id.setTextAlignment(Qt.AlignCenter)
            self.tableWidget.setItem(i, 0, item_id)
            
            item_nome = QTableWidgetItem(prod["nome"])
            item_nome.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            self.tableWidget.setItem(i, 1, item_nome)

            item_preco = QTableWidgetItem(str(prod["preco_venda"]))
            item_preco.setTextAlignment(Qt.AlignCenter)
            self.tableWidget.setItem(i, 2, item_preco)

            btn_adicionar = QPushButton("+")
            self.tableWidget.setCellWidget(i, 3, btn_adicionar)

            btn_adicionar.clicked.connect(lambda _, row=i: self.adicionar_produto(row, data=data))
