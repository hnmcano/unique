
from PySide6.QtWidgets import (QApplication, QPushButton, QMainWindow, QMessageBox, QTableWidgetItem, QWidget, QHeaderView, QTableWidget, QAbstractItemView, QFileDialog)
from windows.form_orders.mesas_ui import Ui_MainWindow as mesas
from core.app_context import app_context as APPContext
from ..mesas.PedidosMesas import DadosMesa
from PySide6.QtNetwork import *
import requests
import os
from config.config import settings


def atualizar_dados(numero_mesa):
        data_json = {
            "numero": numero_mesa,
            "pedido": {
                "status": "ABERTO",
                "itens": []
            }
        }
        
        response = APPContext.api_client.post("/mesas/abrir-mesa", data_json)

        return response

class Mesas(QMainWindow, mesas):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.estilos_originais = {}
        
        mesa = APPContext.api_client.get("/mesas/em-atendimento")

        for i in range(len(mesa)):
            if mesa[i] < 10:
                mesa[i] = f"0{mesa[i]}"
    
            self.estilos_originais[f"Mesa_{mesa[i]}"] = self.findChild(QPushButton, f"Mesa_{mesa[i]}").setStyleSheet( """QPushButton {
                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                    stop: 0 #000000, stop: 1 #000000);
                color: white;
                border: 2px solid green;
                padding: 12px 24px;
                border-radius: 8px;
                font-weight: bold;
                font-size: 14px;
            }""")

        for botao in self.findChildren(QPushButton):
            if botao.objectName().startswith("Mesa_"):
                botao.clicked.connect(self.abrir_mesas_cor_atualiza)


    def abrir_mesas_cor_atualiza(self):

        # A linha abaixo já retorna o objeto do botão que foi clicado.
        botao_clicado = self.sender()

        # A variável 'name_button' é apenas para fins de depuração ou identificação,
        # mas não deve ser usada para aplicar o estilo.
        name_button = botao_clicado.objectName()
        numero_mesa = int(name_button.split("_")[1])

        # Mude a cor do botão clicado chamando o método diretamente no objeto.
        if isinstance(botao_clicado, QPushButton):
            botao_clicado.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                    stop: 0 #000000, stop: 1 #000000);
                color: white;
                border: 2px solid green;
                padding: 12px 24px;
                border-radius: 8px;
                font-weight: bold;
                font-size: 14px;
            }""")


        data = atualizar_dados(numero_mesa)
        self.window_table = DadosMesa(mesa=name_button, data=data, parent=self)
        self.window_table.mesa_excluida.connect(self.mesa_excluida_manualmente)
        self.window_table.show()
            


    def restaurar_cor(self, nome_do_botao):

        # 5. Restaurar a cor original do botão
        botao_a_restaurar = self.findChild(QPushButton, nome_do_botao)

        # 5. Restaura a cor original do botão, se ele ainda existir

        # Verifica se o botão ainda existe
        if botao_a_restaurar is not None:
            botao_a_restaurar.setStyleSheet("""
            """)

    def mesa_excluida_manualmente(self, mesa):
        numero = mesa["numero"]

        if numero < 10:
            numero = f"0{numero}"

        self.estilos_originais[f"Mesa_{numero}"] = self.findChild(QPushButton, f"Mesa_{numero}").setStyleSheet( """
                }""")
