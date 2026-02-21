from PySide6.QtWidgets import *
from windows.form_delivery.pedido_delivery_ui import Ui_MainWindow as dados_pedidos
from PySide6.QtNetwork import *
from PySide6.QtCore import *
from services.websocket import WebSocketService
import requests

from datetime import datetime
import os

APIURLDESENV = os.getenv("APIURLDESENV")

class DadosPedido(QMainWindow, dados_pedidos):
    mensagem_recebida = Signal(dict)
    def __init__(self, pedido: dict, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.network_manager = QNetworkAccessManager(self)
        self.pedido = pedido

        self.id = pedido["id"]

        self.ws = WebSocketService()
        self.ws.mensagem_recebida.connect(self.on_evento_recebido)
        self.ws.start()

        self.status.setText(pedido["status"])
        self.status.setAlignment(Qt.AlignCenter)
        if self.status.text() == "PENDENTE":
            self.status.setStyleSheet("background-color: yellow; color: black; font-weight: bold;")
        elif self.status.text() == "EM PRODUCAO":
             self.status.setStyleSheet("background-color: green; color: black; font-weight: bold;")    

        self.data_criacao.setText(f"{datetime.fromisoformat(pedido["data_criacao"]).strftime('%d/%m/%Y %H:%M:%S')}")
        self.data_criacao.setAlignment(Qt.AlignCenter)

        quantidade_itens = str(len(pedido["itens"]))
        self.quantidade_itens_mesa.setText(quantidade_itens)

        valor_total_formatado = f"R$ {pedido['valor_total']}"
        self.valor_total_mesa.setText(valor_total_formatado)

        taxa_entrega_formatada = f"R$ {pedido["endereco_entrega"]['taxa_entrega']}"
        self.taxa_entrega.setText(taxa_entrega_formatada)

        self.setup_table()
        self.atualizar_tabela(pedido)

    def setup_table(self):
        columns = ["NOME", "QUANTIDADE", "VALOR", "EDITAR", "EXCLUIR"]

        quantidade_columns = len(columns)
        self.tableWidget.setColumnCount(quantidade_columns)
        self.tableWidget.setHorizontalHeaderLabels(columns)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.tableWidget.setShortcutEnabled(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableWidget.setSelectionMode(QTableWidget.SingleSelection)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def atualizar_tabela(self, data, columns=None):

            self.tableWidget.setRowCount(len(data["itens"]))

            for i, item in enumerate(data["itens"]):

                item_nome = QTableWidgetItem(str(item["produtos"]["nome"]))
                self.tableWidget.setItem(i, 0, item_nome)

                item_quantidade = QTableWidgetItem(str(item["quantidade"]))
                item_quantidade.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(i, 1, item_quantidade)

                item_valor_formatado = item['quantidade'] * item['produtos']['preco_venda']
                item_valor = QTableWidgetItem(str(f"R$ {item_valor_formatado:.2f}"))
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
                btn_adicionar.clicked.connect(lambda _, row=i: self.aumentar_quantidade(row, data=item, pedido=data))

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
                btn_diminuir.clicked.connect(lambda _, row=i: self.diminuir_quantidade(row, data=item))

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
                btn_excluir.clicked.connect(lambda _, row=i: self.excluir_item(row, data=item))
                self.tableWidget.setCellWidget(i, 4, btn_excluir)

    def on_evento_recebido(self, evento: dict):
        if evento["tipo"] == "pedido_em_delivery":
            if evento["dados"]["id"] == self.id:
                self.atualizar_tabela(evento["dados"])

    def aumentar_quantidade(self, row, data, pedido):
        
        print("dados:", data)

        response = requests.put(f"{APIURLDESENV}/pedidos/aumentar-item/{pedido["id"]}/{data["id"]}/{data["pedido"]["itens"]["produtos"][row]['produto_id']}")

        if response.status_code == 404:
            QMessageBox.critical(self, "Erro", f"{response.json()['detail']}")

    def diminuir_quantidade(self,row, data):
        response = requests.put(f"{APIURLDESENV}/pedidos/diminuir-item/{data["id"]}/{data["pedido"]["id"]}/{data["pedido"]["itens"][row]['produto_id']}")

        if response.status_code == 400:
            QMessageBox.critical(self, "Erro", f"{response.json()['detail']}")

    def excluir_item(self, row, data):  
        response = requests.delete(f"{APIURLDESENV}/pedidos/excluir-item/{data["id"]}/{data["pedido"]["id"]}/{data["pedido"]["itens"][row]['produto_id']}")

        if response.status_code == 400:
            QMessageBox.critical(self, "Erro", f"{response.json()['detail']}")