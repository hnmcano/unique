
from telas.form_orders.add_produtos_ui import Ui_MainWindow as addProdutosMesa
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt

import requests

APIURLDESENV = "http://localhost:8000"

def buscar_produtos(parent, columns=None):
    
    parent.FilterProducts.setPlaceholderText("Digite para filtrar produtos...")

    parent.FilterProducts.textChanged.connect(parent.filtrar_produtos)

    quantidade_columns = len(columns)
    parent.tableWidget.setColumnCount(quantidade_columns)
    parent.tableWidget.setHorizontalHeaderLabels(columns)
    header = parent.tableWidget.horizontalHeader()
    header.setSectionResizeMode(QHeaderView.Interactive)
    parent.tableWidget.setSortingEnabled(True)
    header.setSectionResizeMode(QHeaderView.Stretch)
    parent.tableWidget.verticalHeader().setVisible(False)
    parent.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
    parent.tableWidget.setSelectionMode(QTableWidget.SingleSelection)

    parent.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)    


    try:
        response = requests.get(f"{APIURLDESENV}/produtos/desktop/table")
        response.raise_for_status()  # Levanta um erro para códigos de status HTTP ruins
        products = response.json()

        parent.tableWidget.setRowCount(len(products))
        linha_atual = 0

            
        for i in products:
            parent.tableWidget.setRowHeight(linha_atual, 50)

            item_ordenavel_id = QTableWidgetItem(str(i["id"]))
            item_ordenavel_id.setData(Qt.UserRole, i)
            parent.tableWidget.setItem(linha_atual, 0, item_ordenavel_id)

            item_ordenavel_nome = QTableWidgetItem(i["nome"])
            parent.tableWidget.setItem(linha_atual, 1, item_ordenavel_nome)

            item_ordenavel_preco_venda = QTableWidgetItem(str(i["preco_venda"]))
            parent.tableWidget.setItem(linha_atual, 2, item_ordenavel_preco_venda)

            linha_atual += 1
    
            parent.tableWidget.sortItems(0, Qt.AscendingOrder)
            
    except requests.RequestException as e:
        QMessageBox.critical(parent, "Erro", f"Erro ao buscar produtos: {str(e)}")

class AdicionarProdutoMesa(QMainWindow, addProdutosMesa):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        columns = ["id", "nome", "preco"]

        buscar_produtos(self, columns)

        



    def filtrar_produtos(self, text):
        for row in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(row, 1)
            if text.lower() in item.text().lower():
                self.tableWidget.showRow(row)
            else:
                self.tableWidget.hideRow(row)

