
from PySide6.QtWidgets import (QHBoxLayout,QApplication, QPushButton, QMainWindow, QMessageBox, QTableWidgetItem, QWidget, QHeaderView, QTableWidget, QAbstractItemView, QFileDialog, QStyle)
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
        self.atualizar_tabela(data["pedido"]["itens"], data)

        # Ao clicar no botão cancelar, Aciona a função de confirmação de exclusão localizada em scripts/aux_func.py
        self.btn_excluir.clicked.connect(lambda: exibir_confirmacao_exclusao(self, data))
        self.adicionar_produto.clicked.connect(lambda: abrir_produto(self, data))

    def setup_table(self):
        columns = ["NOME", "QUANTIDADE", "VALOR", "EDITAR", "EXCLUIR"]

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

    def atualizar_tabela(self, itens, mesa):

            valor_total_formatado = f"R$ {mesa['pedido']['valor_total']:.2f}"
            self.valor_total_mesa.setText(valor_total_formatado)
            self.quantidade_itens_mesa.setText(str(mesa["pedido"]["quantidade_itens"]))

            self.tableWidget.setRowCount(len(itens))  

            for i, item in enumerate(itens):
                item_nome = QTableWidgetItem(str(item["produto"]["nome"]))
                self.tableWidget.setItem(i, 0, item_nome)

                item_quantidade = QTableWidgetItem(str(item["quantidade"]))
                item_quantidade.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(i, 1, item_quantidade)

                item_valor_formatado = f"R$ {item['valor_total']:.2f}"
                item_valor = QTableWidgetItem(item_valor_formatado)
                item_valor.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(i, 2, item_valor)

                container = QWidget()

                # Cria layout horizontal
                layout = QHBoxLayout(container)
                layout.setContentsMargins(0, 0, 0, 0)
                layout.setSpacing(5)

                # Botão editar
                btn_adicionar = QPushButton("+")
                btn_adicionar.setStyleSheet("""
                QPushButton {
                    max-width: 40px;
                    height: 20px;
                    background-color: green;
                    font-size: 16px;
                }
                QPushButton:hover {
                    background-color: rgb(131, 131, 131);
                }

                QPushButton:clicked {
                    background-color: rgb(131, 131, 131);
                }
                """)
                btn_adicionar.clicked.connect(lambda _, row=i: self.aumentar_quantidade(row, data=mesa))

                # Botão excluir
                btn_diminuir = QPushButton("-")
                btn_diminuir.setStyleSheet("""QPushButton {
                    max-width: 40px;
                    height: 20px;
                    background-color: red;
                    font-size: 26px;
                }
                QPushButton:hover {
                    background-color: rgb(131, 131, 131);
                }

                QPushButton:clicked {
                    background-color: rgb(131, 131, 131);
                }

                """)
                btn_diminuir.clicked.connect(lambda _, row=i: self.diminuir_quantidade(row, data=mesa))

                # Adiciona os botões ao layout
                layout.addWidget(btn_adicionar)
                layout.addWidget(btn_diminuir)
                # Define o container como widget da célula
                self.tableWidget.setCellWidget(i, 3, container)

                btn_excluir = QPushButton()
                btn_excluir.setIcon(
                    QApplication.style().standardIcon(QStyle.SP_TrashIcon)
                )
                btn_excluir.setStyleSheet(
                    """QPushButton {
                            background-color: transparent; 
                            border: none;
                        }
                        QPushButton:hover {
                            background-color: 
                            rgb(131, 131, 131);
                        }
                        QPushButton:clicked {
                            background-color: rgb(131, 131, 131);
                        }
                    """
                )
                btn_excluir.clicked.connect(lambda _, row=i: self.excluir_item(row, data=mesa))
                self.tableWidget.setCellWidget(i, 4, btn_excluir)

    # Override do método closeEvent para emitir o sinal quando a janela for fechada
    def closeEvent(self, event):
        event.accept()

    def on_evento_recebido(self, evento: dict):
        if evento["tipo"] == "produto_em_mesa":
            if evento["dados"]["id"] == self.id_mesa:
                self.atualizar_tabela(evento["dados"]["pedido"]["itens"], evento["dados"])

    def aumentar_quantidade(self, row, data):
        response = requests.put(f"{APIURLDESENV}/mesas/aumentar-item/{data["id"]}/{data["pedido"]["id"]}/{data["pedido"]["itens"][row]['produto_id']}")

        if response.status_code == 400:
            QMessageBox.critical(self, "Erro", f"{response.json()['detail']}")

    def diminuir_quantidade(self,row, data):
        response = requests.put(f"{APIURLDESENV}/mesas/diminuir-item/{data["id"]}/{data["pedido"]["id"]}/{data["pedido"]["itens"][row]['produto_id']}")

        if response.status_code == 400:
            QMessageBox.critical(self, "Erro", f"{response.json()['detail']}")

    def excluir_item(self, row, data):  
        response = requests.delete(f"{APIURLDESENV}/mesas/excluir-item/{data["id"]}/{data["pedido"]["id"]}/{data["pedido"]["itens"][row]['produto_id']}")

        if response.status_code == 400:
            QMessageBox.critical(self, "Erro", f"{response.json()['detail']}")