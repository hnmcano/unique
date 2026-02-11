
from PySide6.QtWidgets import (QApplication, QPushButton, QMainWindow, QMessageBox, QTableWidgetItem, QWidget, QHeaderView, QTableWidget, QAbstractItemView, QFileDialog)
from telas.form_orders.pedido_mesa_ui import Ui_MainWindow as pedido_mesa
from .AddProdutoMesas import AdicionarProdutoMesa
from PySide6.QtNetwork import ( QNetworkAccessManager)
from PySide6.QtCore import Signal, Qt
from datetime import datetime
import requests

from services.websocket import WebSocketService

APIURLDESENV = "http://localhost:8000"

def exibir_confirmacao_exclusao(parent= None, data=None):
    msg_box = QMessageBox(parent)
    msg_box.setIcon(QMessageBox.Question) # type: ignore
    msg_box.setWindowTitle("Confirmar Exclusão")
    msg_box.setText("Tem certeza que gostaria de excluir essa mesa? Todos os dados serão perdidos.")
    msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No) # type: ignore

    # A resposta é armazenada aqui, o código é bloqueado até o usuário interagir
    resposta = msg_box.exec()

    if resposta == QMessageBox.Yes: # type: ignore
        # Se o usuário confirmar, emita o sinal e feche a janela
        response = requests.delete(f"{APIURLDESENV}/mesas/excluir-mesa/{data["id"]}")

        if response.status_code == 200:
            QMessageBox.information(parent, "Sucesso", "Mesa excluida com sucesso!")
            
            parent.mesa_excluida.emit(data) # type: ignore
            parent.close() # type: ignore
        else:
            QMessageBox.critical(parent, "Erro", "Falha ao excluir mesa.")
            return

    # Se a resposta for QMessageBox.No, o diálogo simplesmente fecha e nada acontece

def abrir_produto(self, data=None):
    self.produtos = AdicionarProdutoMesa(parent=self, data=data)
    self.produtos.show()    

class DadosMesa(QMainWindow, pedido_mesa):
    mesa_excluida = Signal(dict)
    mensagem_recebida = Signal(dict)

    def __init__(self, mesa, data, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.ws = WebSocketService()
        self.ws.mensagem_recebida.connect(self.on_evento_recebido)
        self.ws.start()

        self.mesa.setText(f"{str.replace(mesa, '_', ' ')} ")
        self.id_mesa = data["id"]

        data_str = data["pedido"]["data_criacao"]
        dt_utc = datetime.fromisoformat(data_str.replace("Z", "+00:00"))
        dt_local = dt_utc.astimezone()
        data_formatada = dt_local.strftime("%d/%m/%Y %H:%M:%S")

        self.status.setText(data["pedido"]["status"])
        self.data_criacao.setText(data_formatada)

        self.network_manager = QNetworkAccessManager(self)

        self.setup_table()
        self.atualizar_tabela(data["pedido"]["itens"])

        # Ao clicar no botão cancelar, Aciona a função de confirmação de exclusão localizada em scripts/aux_func.py
        self.btn_excluir.clicked.connect(lambda: exibir_confirmacao_exclusao(self, data))
        self.adicionar_produto.clicked.connect(lambda: abrir_produto(self, data))

    def setup_table(self):
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

    def atualizar_tabela(self, itens):

            self.tableWidget.setRowCount(len(itens))  

            for i, item in enumerate(itens):
                self.tableWidget.setItem(i, 0, QTableWidgetItem(str(item["produto"]["nome"])))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(str(item["quantidade"])))
                self.tableWidget.setItem(i, 2, QTableWidgetItem(str(item["valor_unitario"])))

    # Override do método closeEvent para emitir o sinal quando a janela for fechada
    def closeEvent(self, event):
        event.accept()

    def on_evento_recebido(self, evento: dict):
        if evento["tipo"] == "produto_em_mesa":
            if evento["dados"]["id"] == self.id_mesa:
                self.atualizar_tabela(evento["dados"]["pedido"]["itens"])
            