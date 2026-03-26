from PySide6.QtWidgets import *
from PySide6.QtCore import *
from windows.form_box.Caixa_ui import Ui_CAIXA as caixa
from infra.api_client import APIClient
from core.app_context import app_context as APPContext
from config.config import settings
from datetime import datetime, timedelta

class Caixa(QMainWindow, caixa):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.validar_caixa()
        self.layout_tabela()
        self.carregar_tabela()
        self.AbrirCaixa.clicked.connect(self.iniciar_caixa)
        self.FecharCaixa.clicked.connect(self.fechar_caixa)
        self.FecharAndImprimir.clicked.connect(self.fechar_caixa_imprimir)

        

    def layout_tabela(self):
        columns = [ "Abertura Caixa", "Forma de Pagamento", "Bandeira", "Total"]

        quantidade_columns = len(columns)
        self.tableCaixa.setColumnCount(quantidade_columns)
        self.tableCaixa.setHorizontalHeaderLabels(columns)
        header = self.tableCaixa.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.tableCaixa.setSortingEnabled(True)
        self.tableCaixa.verticalHeader().setVisible(False)
        self.tableCaixa.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableCaixa.setSelectionMode(QTableWidget.SingleSelection)
        self.tableCaixa.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def atualizar_tabela(self, dados):
        self.tableCaixa.setRowCount(len(dados))

        for index, item in enumerate(dados):
            dataDeAbertura = (datetime.fromisoformat(item["data_abertura"]) - timedelta(hours=3)).strftime("%d/%m/%Y")
            self.data_abertura =QTableWidgetItem(dataDeAbertura)
            self.data_abertura.setTextAlignment(Qt.AlignCenter)
            self.tableCaixa.setItem(index, 0, self.data_abertura)

            self.forma_pagamento = QTableWidgetItem(item["forma_pagamento"])
            self.forma_pagamento.setTextAlignment(Qt.AlignCenter)
            self.tableCaixa.setItem(index, 1, self.forma_pagamento)

            self.bandeira = QTableWidgetItem(item["bandeira"])
            self.bandeira.setTextAlignment(Qt.AlignCenter)
            self.tableCaixa.setItem(index, 2, self.bandeira)

            self.valor_total = QTableWidgetItem(str(f"R$ {item["total"]:.2f}"))
            self.valor_total.setTextAlignment(Qt.AlignCenter)
            self.tableCaixa.setItem(index, 3, self.valor_total)

    def iniciar_caixa(self):
        valor_caixa = float(self.ValorCaixa.text().replace(",", "."))
        try:
            data_json = {
                "valor_inicial": valor_caixa
            }

            response = APPContext.api_client.post("caixa/open_box", data_json)
            self.ValorCaixa.setText(f"{response['valor_inicial']:.2f}")
            data_abertura = (datetime.fromisoformat(response['data_abertura']) - timedelta(hours=3)).strftime("%d/%m/%Y - %H:%M:%S")
            self.DataAbertura.setText(data_abertura)
            QMessageBox.information(self, "Sucesso", "Caixa aberto com sucesso")
 
            self.StatusCaixa.setText("Caixa Aberto")
            self.StatusCaixa.setStyleSheet("background-color: green; color: white; font-weight: bold;")

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao abrir caixa: {str(e)}")

    def fechar_caixa(self):
        try:
            questionamento = QMessageBox.question(self, "Confirmação", "Deseja realmente fechar o caixa?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if questionamento == QMessageBox.No:
                return
            else:
                try:
                    response = APPContext.api_client.get("caixa/close_box")
                    self.StatusCaixa.setText("Caixa Fechado")
                    self.StatusCaixa.setStyleSheet("background-color: red; color: white; font-weight: bold;")
                    self.DataAbertura.setText("00/00/0000 - 00:00:00")
                    self.ValorCaixa.setText("0,00")
                    QMessageBox.information(self, "Sucesso", "Caixa fechado com sucesso")
                except Exception as e:
                    QMessageBox.critical(self, "Erro", f"Erro ao fechar caixa: {str(e)}")

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao fechar caixa: {str(e)}")

    def validar_caixa(self):

        try:
            response = APPContext.api_client.get("caixa/valid_box")
            print(response)
            self.ValorCaixa.setText(f"{response['valor_inicial']:.2f}")
            self.LabelTotal.setText(f"{response["valor_final"]:.2f}")
            data_abertura = (datetime.fromisoformat(response['data_abertura']) - timedelta(hours=3)).strftime("%d/%m/%Y - %H:%M:%S") 
            self.DataAbertura.setText(data_abertura)
            self.StatusCaixa.setText("Caixa Aberto")
            self.StatusCaixa.setStyleSheet("background-color: green; color: white; font-weight: bold;")            
        except:
            self.StatusCaixa.setText("Caixa Fechado")
            self.DataAbertura.setText("00/00/0000 - 00:00:00")
            self.ValorCaixa.setText("0,00")
            self.StatusCaixa.setStyleSheet("background-color: red; color: white; font-weight: bold;")

    def fechar_caixa_imprimir(self):
        print("fechar")
        print("imprimir")

    def carregar_tabela(self):
        try:
            response = APPContext.api_client.get("caixa/desktop/carregar-tabela")
            self.atualizar_tabela(response)
        except Exception as e:
            print(e)
