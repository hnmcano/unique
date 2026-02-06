
from PySide6.QtWidgets import (QApplication, QPushButton, QMainWindow, QMessageBox, QTableWidgetItem, QWidget, QHeaderView, QTableWidget, QAbstractItemView, QFileDialog)
from telas.form_orders.mesas_ui import Ui_MainWindow as mesas
from ..mesas.PedidosMesas import DadosMesa
from PySide6.QtNetwork import ( QNetworkAccessManager)
import requests

class Mesas(QMainWindow, mesas):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.estilos_originais = {}

        self.network_manager = QNetworkAccessManager(self)

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

        response = requests.post("http://127.0.0.1:8000/mesas/abrir-mesa", json={
            "numero": numero_mesa,
            "pedido": {
                "status": "ABERTO",
                "itens": []
                }
            }
        )

        data = response.json()
        print(data)

        if response.status_code == 201:
            self.window_table = DadosMesa(mesa=name_button, data=data, parent=self)
            self.window_table.show()
            
        elif response.status_code == 400:
            QMessageBox.information(self, "aviso", "Não há caixa aberto, por favor realizar a abertura do caixa para continuar")
            botao_clicado.setStyleSheet("""
            """)
            return

        # 2. Criar e abrir a nova janela

            self.window_table.janela_fechada.connect(
                lambda: self.restaurar_cor(botao_clicado.objectName())
            )


    def restaurar_cor(self, nome_do_botao):

        # 5. Restaurar a cor original do botão
        botao_a_restaurar = self.findChild(QPushButton, nome_do_botao)

        # 5. Restaura a cor original do botão, se ele ainda existir

        # Verifica se o botão ainda existe
        if botao_a_restaurar is not None:
            botao_a_restaurar.setStyleSheet("""
            """)
