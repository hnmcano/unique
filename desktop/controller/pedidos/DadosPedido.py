from PySide6.QtWidgets import *
from windows.form_delivery.pedido_delivery_ui import Ui_MainWindow as dados_pedidos
from controller.pedidos.AtualizarQuantidade import AtualizarQuantidade_ui as EditarItem
from controller.pedidos.AddProdutoPedidos import AdicionarProdutoPedido

from PySide6.QtNetwork import *
from PySide6.QtCore import *
from core.app_context import app_context as APPContext


from datetime import datetime, timedelta
import os
from config.config import settings

def exibir_confirmacao_exclusao(self):
    msg_box = QMessageBox(self)
    msg_box.setIcon(QMessageBox.Question) # type: ignore
    msg_box.setWindowTitle("Confirmar Exclusão")
    msg_box.setText("Tem certeza que gostaria de excluir esse pedido? Todos os dados serão perdidos.")
    msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No) # type: ignore

    # A resposta é armazenada aqui, o código é bloqueado até o usuário interagir
    resposta = msg_box.exec()

    if resposta == QMessageBox.Yes: # type: ignore
        # Se o usuário confirmar, emita o sinal e feche a janela
        try:
            response = APPContext.api_client.delete(f"pedidos/desktop/deletar-dados-pedidos/{self.id}", data=None )
            
            QMessageBox.information(self, "Sucesso", "Pedido excluido com sucesso!")

            APPContext.pedido_store.remover(self.pedido)
            self.close() # type: ignore

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Falha ao excluir pedido. {str(e)}")
            return

class DadosPedido(QMainWindow, dados_pedidos):
    mensagem_recebida = Signal(dict)

    def __init__(self, pedido, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.network_manager = QNetworkAccessManager(self)
        self.pedido = pedido

        self.id = pedido["id_pedido"]

        self.websocket = APPContext.websocket_client

        self.websocket.mensagem_recebida.connect(self.on_evento_recebido)

        self.status.setText(pedido["status"])
        self.status.setAlignment(Qt.AlignCenter)
        if self.status.text() == "PENDENTE":
            self.status.setStyleSheet("background-color: yellow; color: black; font-weight: bold;")
        elif self.status.text() == "EM PRODUCAO":
             self.status.setStyleSheet("background-color: green; color: black; font-weight: bold;")    

        self.data_criacao.setText(f"{(datetime.fromisoformat(pedido["data_criacao"])- timedelta(hours=3)).strftime('%d/%m/%Y %H:%M:%S')}")
        self.data_criacao.setAlignment(Qt.AlignCenter)

        self.setup_table()
        self.atualizar_tabela(pedido)

        self.btn_excluir.clicked.connect(lambda: exibir_confirmacao_exclusao(self))
        self.btn_adicionar.clicked.connect(lambda: self.abrir_produtos(data=pedido))

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

    def atualizar_tabela(self, data):
            quantidade_itens = str(len(data["itens"]))
            self.quantidade_itens_mesa.setText(quantidade_itens)

            valor_total_formatado = f"R$ {data['valor_total']}"
            self.valor_total_mesa.setText(valor_total_formatado)

            taxa_entrega_formatada = f"R$ {data["endereco_entrega"]['taxa_entrega']}"
            self.taxa_entrega.setText(taxa_entrega_formatada)


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

                # Botão editar
                btn_editar = QPushButton()
                btn_editar.setIcon(
                    QApplication.style().standardIcon(QStyle.SP_FileDialogContentsView)
                )

                btn_editar.setStyleSheet("""
                QPushButton {
                    background-color: transparent; 
                    border: none;
                }
                QPushButton:hover {
                    background-color: rgb(131, 131, 131);
                }
                QPushButton:pressed {
                    background-color: rgb(131, 131, 131);
                }
                """)

                btn_editar.clicked.connect(
                    lambda _, row=i: self.editar_item_quantidade(row=row, data=data)
                )

                self.tableWidget.setCellWidget(i, 3, btn_editar)

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
                btn_excluir.clicked.connect(lambda _, row=i: self.excluir_item(row=row, data=data))
                self.tableWidget.setCellWidget(i, 4, btn_excluir)

    def on_evento_recebido(self, evento: dict):
        if evento["tipo"] == "pedido_em_delivery":
            print(evento["dados"])
            if evento["dados"]["id_pedido"] == self.id:
                self.atualizar_tabela(evento["dados"])

    def editar_item_quantidade( self,row, data=None):
        id = data["id_pedido"]
        data = data["itens"][row]

        self.editar_item = EditarItem(item=data, id=id, parent=self)
        self.editar_item.show()

    def excluir_item( self,row, data=None):
        id = data["id_pedido"]
        data = data["itens"][row]

        try:
            response = APPContext.api_client.delete(f"/pedidos/desktop/deletar-item-pedido", 
                                                    {
                                                        "id_pedido": id, 
                                                        "id_itens_pedido": data["id_itens_pedido"]
                                                     })
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"{e}")

    def abrir_produtos(self, data=None):
        self.produtos = AdicionarProdutoPedido(parent=self, data=data)
        self.produtos.show()