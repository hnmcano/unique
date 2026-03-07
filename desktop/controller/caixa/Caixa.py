from PySide6.QtWidgets import *
from windows.form_box.Caixa_ui import Ui_CAIXA as caixa
from infra.api_client import APIClient
from core.app_context import app_context as APPContext
from config.config import settings

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
        try:
            data_json = {
                "valor": valor_caixa
            }

            response = APPContext.api_client.post("caixa/open_box", data_json)

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

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao abrir caixa: {str(e)}")

        
        self.ValorCaixa.setText("0,00")

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
                except Exception as e:
                    QMessageBox.critical(self, "Erro", f"Erro ao fechar caixa: {str(e)}")

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao fechar caixa: {str(e)}")

    def validar_caixa(self):

        try:
            response = APPContext.api_client.get("caixa/valid_box")

            self.CloseCaixa.setDisabled(False)
            self.StatusCaixa.setText("Caixa Aberto")
            self.StatusCaixa.setStyleSheet("background-color: green; color: white; font-weight: bold;")
            self.open_caixa.setDisabled(True)
            self.open_caixa.setStyleSheet("background-color: rgb(91, 91, 91); color: black; font-weight: bold;")
            
        except:
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
