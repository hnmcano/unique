from PySide6.QtWidgets import *
from telas.form_box.Caixa_ui import Ui_CAIXA as caixa

import requests

APIURLDESENV = "http://localhost:5000"

class Caixa(QMainWindow, caixa):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.ValorCaixa.setText("0,00")

        self.validar_caixa()
        self.open_caixa.clicked.connect(self.iniciar_caixa)
        self.CloseCaixa.clicked.connect(self.fechar_caixa)

    def iniciar_caixa(self):
        valor_caixa = float(self.ValorCaixa.text().replace(",", "."))

        data_json = {
            "valor": valor_caixa
        }

        url = f"{APIURLDESENV}/caixa/open_box"

        response = requests.post(url, json=data_json)

        if response.status_code == 200:
            QMessageBox.information(self, "Sucesso", "Caixa aberto com sucesso")
            self.CloseCaixa.setDisabled(False)
            self.CloseCaixa.setStyleSheet("""QPushButton {
                background: qlineargradient(
                    spread:pad,
                    x1:0, y1:0,
                    x2:1, y2:0,
                    stop:0 #393939,
                    stop:1 #7d7d7d
                );
                color: white;
                border: 2px solid #282828;
                border-radius: 6px;
                padding: 6px 12px;
            }

            QPushButton::hover{
                background: qlineargradient(
                    spread:pad,
                    x1:0, y1:0,
                    x2:1, y2:0,
                    stop:0 #7d7d7d,
                    stop:1 #393939
                );
            }""")
            self.StatusCaixa.setText("Caixa Aberto")
            self.StatusCaixa.setStyleSheet("background-color: green; color: white; font-weight: bold;")
        else:
            QMessageBox.critical(self, "Erro", f"{response.json().get('detail')}" )
        
        self.ValorCaixa.setText("0,00")

    def fechar_caixa(self):
        try:
            questionamento = QMessageBox.question(self, "Confirmação", "Deseja realmente fechar o caixa?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if questionamento == QMessageBox.No:
                return
            else:
                try:
                    url = f"{APIURLDESENV}/caixa/close_box"
                    response = requests.get(url)

                    if response.status_code == 200:
                        self.StatusCaixa.setText("Caixa Fechado")
                        self.StatusCaixa.setStyleSheet("background-color: red; color: white; font-weight: bold;")
                        self.CloseCaixa.setDisabled(True)
                        self.CloseCaixa.setStyleSheet("background-color: rgb(91, 91, 91); color: black; font-weight: bold;")
                        self.open_caixa.setDisabled(False)
                        self.open_caixa.setStyleSheet("""QPushButton {
                            background: qlineargradient(
                                spread:pad,
                                x1:0, y1:0,
                                x2:1, y2:0,
                                stop:0 #393939,
                                stop:1 #7d7d7d
                            );
                            color: white;
                            border: 2px solid #282828;
                            border-radius: 6px;
                            padding: 6px 12px;
                        }

                        QPushButton::hover{
                            background: qlineargradient(
                                spread:pad,
                                x1:0, y1:0,
                                x2:1, y2:0,
                                stop:0 #7d7d7d,
                                stop:1 #393939
                            );
                        }""")
                    else:
                        QMessageBox.critical(self, "Erro", f"{response.json().get('detail')}")
                except Exception as e:
                    QMessageBox.critical(self, "Erro", f"Erro ao fechar caixa: {str(e)}")

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao fechar caixa: {str(e)}")

    def validar_caixa(self):

        url = f"{APIURLDESENV}/caixa/valid_box"
        response = requests.get(url)

        if response.status_code == 200:
            self.CloseCaixa.setDisabled(False)
            self.StatusCaixa.setText("Caixa Aberto")
            self.StatusCaixa.setStyleSheet("background-color: green; color: white; font-weight: bold;")
            self.open_caixa.setDisabled(True)
            self.open_caixa.setStyleSheet("background-color: rgb(91, 91, 91); color: black; font-weight: bold;")
        else:
            self.CloseCaixa.setDisabled(True)
            self.CloseCaixa.setStyleSheet("background-color: rgb(91, 91, 91); color: black; font-weight: bold;")
            self.StatusCaixa.setText("Caixa Fechado")
            self.StatusCaixa.setStyleSheet("background-color: red; color: white; font-weight: bold;")
            self.open_caixa.setDisabled(False)
            self.open_caixa.setStyleSheet("""QPushButton {
                background: qlineargradient(
                    spread:pad,
                    x1:0, y1:0,
                    x2:1, y2:0,
                    stop:0 #393939,
                    stop:1 #7d7d7d
                );
                color: white;
                border: 2px solid #282828;
                border-radius: 6px;
                padding: 6px 12px;
            }

            QPushButton::hover{
                background: qlineargradient(
                    spread:pad,
                    x1:0, y1:0,
                    x2:1, y2:0,
                    stop:0 #7d7d7d,
                    stop:1 #393939
                );
            }""")
