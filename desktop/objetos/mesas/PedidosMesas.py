
from PySide6.QtWidgets import (QApplication, QPushButton, QMainWindow, QMessageBox, QTableWidgetItem, QWidget, QHeaderView, QTableWidget, QAbstractItemView, QFileDialog)
from telas.form_orders.pedido_mesa_ui import Ui_MainWindow as pedido_mesa
from .AddProdutoMesas import AdicionarProdutoMesa
from PySide6.QtNetwork import ( QNetworkAccessManager)
from PySide6.QtCore import Signal, Qt
from datetime import datetime
import requests
from scripts.produtos import exibir_confirmacao_exclusao

class DadosMesa(QMainWindow, pedido_mesa):
    janela_fechada = Signal()

    def __init__(self, mesa, data, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.mesa.setText(f"{str.replace(mesa, '_', ' ')} ")

        data_str = data["pedido"]["data_criacao"]
        dt_utc = datetime.fromisoformat(data_str.replace("Z", "+00:00"))
        dt_local = dt_utc.astimezone()
        data_formatada = dt_local.strftime("%d/%m/%Y %H:%M:%S")

        self.status.setText(data["pedido"]["status"])
        self.data_criacao.setText(data_formatada)

        self.network_manager = QNetworkAccessManager(self)

        columns = ["NOME", "QUANTIDADE", "VALOR"]

        quantidade_columns = len(columns)
        self.tableWidget.setColumnCount(quantidade_columns)
        self.tableWidget
        self.tableWidget.setHorizontalHeaderLabels(columns)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Interactive)
        self.tableWidget.setShortcutEnabled(True)
        header.setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableWidget.setSelectionMode(QTableWidget.SingleSelection)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # Ao clicar no botão cancelar, Aciona a função de confirmação de exclusão localizada em scripts/aux_func.py
        self.btn_excluir.clicked.connect(lambda: exibir_confirmacao_exclusao(self))
        self.adicionar_produto.clicked.connect(self.abrir_produtos)


    # Override do método closeEvent para emitir o sinal quando a janela for fechada
    def closeEvent(self, event):
        event.accept()

    def abrir_produtos(self):
        self.produtos = AdicionarProdutoMesa(parent=self)
        self.produtos.show()
