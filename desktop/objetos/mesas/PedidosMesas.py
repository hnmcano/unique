
from PySide6.QtWidgets import (QApplication, QPushButton, QMainWindow, QMessageBox, QTableWidgetItem, QWidget, QHeaderView, QTableWidget, QAbstractItemView, QFileDialog)
from telas.form_orders.pedido_mesa_ui import Ui_MainWindow as pedido_mesa
from .AddProdutoMesas import AdicionarProdutoMesa
from PySide6.QtNetwork import ( QNetworkAccessManager)
from PySide6.QtCore import Signal, Qt
from datetime import datetime
import requests

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


class DadosMesa(QMainWindow, pedido_mesa):
    mesa_excluida = Signal(dict)
    print("mesa excluida", mesa_excluida)
    
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
        self.btn_excluir.clicked.connect(lambda: exibir_confirmacao_exclusao(self, data))
        self.adicionar_produto.clicked.connect(self.abrir_produtos)

        try:

            self.tableWidget.setRowCount(len(data["pedido"]["itens"]))  

            for i in range(len(data["pedido"]["itens"])):
                self.tableWidget.setItem(i, 0, QTableWidgetItem(str(data["pedido"]["itens"][i]["produto"]["nome"])))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(str(data["pedido"]["itens"][i]["quantidade"])))
                self.tableWidget.setItem(i, 2, QTableWidgetItem(str(data["pedido"]["itens"][i]["valor_unitario"])))

        except Exception as e:
            print("erro apresentado", e)



    # Override do método closeEvent para emitir o sinal quando a janela for fechada
    def closeEvent(self, event):
        event.accept()

    def abrir_produtos(self):
        self.produtos = AdicionarProdutoMesa(parent=self)
        self.produtos.show()
