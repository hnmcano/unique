from PySide6.QtWidgets import *
from PySide6.QtGui import QGuiApplication

from telas.form_products.produtos_ui import Ui_MainWindow as produtos

from .DadosProdutos import DadosProduto
from .AddCategoria import AddCategoria
from .Addprodutos import AddProdutos

from PySide6.QtCore import Qt

import requests

APIURLDESENV = "http://localhost:8000"

def center_window(self):

    screen = QGuiApplication.primaryScreen()
    screen_geometry = screen.availableGeometry()
    window_geometry = self.frameGeometry()

    window_geometry.moveCenter(screen_geometry.center())
    self.move(window_geometry.topLeft())

def buscar_produtos(parent, columns=None):
    
    tela = (str(parent).split('.')[1]).split('(')[0]

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

            item_ordenavel_cod_pdv = QTableWidgetItem(str(i["cod_pdv"]))
            parent.tableWidget.setItem(linha_atual, 1, item_ordenavel_cod_pdv)

            item_ordenavel_categoria = QTableWidgetItem(str(i["nome_categoria"]))
            parent.tableWidget.setItem(linha_atual, 2, item_ordenavel_categoria)

            item_ordenavel_nome = QTableWidgetItem(i["nome"])
            parent.tableWidget.setItem(linha_atual, 3, item_ordenavel_nome)

            item_ordenavel_preco_custo = QTableWidgetItem(str(i["preco_custo"]))
            parent.tableWidget.setItem(linha_atual, 4, item_ordenavel_preco_custo)

            item_ordenavel_preco_venda = QTableWidgetItem(str(i["preco_venda"]))
            parent.tableWidget.setItem(linha_atual, 5, item_ordenavel_preco_venda)

            item_ordenavel_estoque = QTableWidgetItem(str(i["estoque_min"]))
            parent.tableWidget.setItem(linha_atual, 6, item_ordenavel_estoque)

            item_ordenavel_estoque_min = QTableWidgetItem(str(i["estoque"]))
            parent.tableWidget.setItem(linha_atual, 7, item_ordenavel_estoque_min)

            item_ordenavel_medida = QTableWidgetItem(str(i["medida"]))
            parent.tableWidget.setItem(linha_atual, 8, item_ordenavel_medida)

            item_ordenavel_status_venda = QTableWidgetItem(str(i["status_venda"]))
            parent.tableWidget.setItem(linha_atual, 9, item_ordenavel_status_venda)

            linha_atual += 1

        parent.tableWidget.sortItems(0, Qt.AscendingOrder)

            
    except requests.RequestException as e:
        QMessageBox.critical(parent, "Erro", f"Erro ao buscar produtos: {str(e)}")

class Produtos(QMainWindow, produtos):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        center_window(self)

        columns = ["ID","CODIGO PDV", "CATEGORIA", "NOME", "PREÇO DE CUSTO", "PREÇO DE VENDA","ESTOQUE MIN", "ESTOQUE", "MEDIDA", "STATUS"]
        # Esconde o botão do windows de fechar(X) a janela
        self.tableWidget.cellClicked.connect(self.abrir_dados_produto)
        buscar_produtos(self, columns)

        # Ao clicar no botão adicionar produto, abre a janela de adicionar produtos
        self.add_products.clicked.connect(self.abrir_add_produto)
        self.add_categoria.clicked.connect(self.abrir_categoria)

    def abrir_add_produto(self):
        self.add_produto_window = AddProdutos(parent=self)# type: ignore
        self.add_produto_window.show()# type: ignore

    def abrir_dados_produto(self, row, column):
        item = self.tableWidget.item(row, 0)
        produto = item.data(Qt.UserRole)
        self.dados_produto_window = DadosProduto(produto=produto, parent=self)
        self.dados_produto_window.show()

    def abrir_categoria(self):
        self.categoria_window = AddCategoria(parent=self)
        self.categoria_window.show()

    def filtrar_produtos(self, text):
        for row in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(row, 3)
            if text.lower() in item.text().lower():
                self.tableWidget.showRow(row)
            else:
                self.tableWidget.hideRow(row)

