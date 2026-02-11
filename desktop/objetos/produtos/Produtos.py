from PySide6.QtWidgets import *
from PySide6.QtGui import QGuiApplication

from telas.form_products.produtos_ui import Ui_MainWindow as produtos

from .DadosProdutos import DadosProduto
from .AddCategoria import AddCategoria
from .Addprodutos import AddProdutos
from services.websocket import WebSocketService

from PySide6.QtCore import Qt, Signal

import requests
import json

APIURLDESENV = "http://localhost:8000"

def center_window(self):

    screen = QGuiApplication.primaryScreen()
    screen_geometry = screen.availableGeometry()
    window_geometry = self.frameGeometry()

    window_geometry.moveCenter(screen_geometry.center())
    self.move(window_geometry.topLeft())

def carregar_produto():
    response = requests.get(f"{APIURLDESENV}/produtos/desktop/table")
    response.raise_for_status()  # Levanta um erro para códigos de status HTTP ruins
    produtos = response.json()

    return produtos

class Produtos(QMainWindow, produtos):
    mensagem_recebida = Signal(dict)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        center_window(self)

        self.ws = WebSocketService()
        self.ws.mensagem_recebida.connect(self.on_evento_recebido)
        self.ws.start()


        self.layout_tabela()
        data = carregar_produto()
        self.atualizar_tabela(data)

        # Ao clicar no botão adicionar produto, abre a janela de adicionar produtos
        self.tableWidget.cellClicked.connect(self.abrir_dados_produto)
        self.add_products.clicked.connect(self.abrir_add_produto)
        self.add_categoria.clicked.connect(self.abrir_categoria)

    def layout_tabela(parent):

        columns = ["ID","CODIGO PDV", "CATEGORIA", "NOME", "PREÇO DE CUSTO", "PREÇO DE VENDA","ESTOQUE MIN", "ESTOQUE", "MEDIDA", "STATUS"]
        # Esconde o botão do windows de fechar(X) a janela
        
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

    def atualizar_tabela(parent, data):

        if isinstance(data, str):
            data = json.loads(data)

        parent.tableWidget.setRowCount(len(data))

        for i, prod in enumerate(data):
            parent.tableWidget.setItem(i, 0, QTableWidgetItem(str(prod["id"])))
            parent.tableWidget.setItem(i, 1, QTableWidgetItem(prod["cod_pdv"]))          
            parent.tableWidget.setItem(i, 2, QTableWidgetItem(prod["nome_categoria"]))
            parent.tableWidget.setItem(i, 3, QTableWidgetItem(prod["nome"]))
            parent.tableWidget.setItem(i, 4, QTableWidgetItem(str(prod["preco_custo"])))
            parent.tableWidget.setItem(i, 5, QTableWidgetItem(str(prod["preco_venda"])))
            parent.tableWidget.setItem(i, 6, QTableWidgetItem(str(prod["estoque_min"])))
            parent.tableWidget.setItem(i, 7, QTableWidgetItem(str(prod["estoque"])))
            parent.tableWidget.setItem(i, 8, QTableWidgetItem(prod["medida"]))
            parent.tableWidget.setItem(i, 9, QTableWidgetItem(prod["status_venda"]))

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

    def on_evento_recebido(self, evento: dict):

        data = evento["dados"]

        if evento["tipo"] == "Atualizar_produtos":
            # Se vier um dicionário único, transformamos em lista
            if isinstance(data, dict):
                data = [data]

            self.atualizar_tabela(data)

