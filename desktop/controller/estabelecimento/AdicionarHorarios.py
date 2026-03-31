from PySide6.QtWidgets import *
from windows.form_establishment.horarios_add_ui import Ui_MainWindow as add_horarios

from datetime import datetime, time

from core.app_context import app_context as APPContext

def dias_da_semana():
    return ['segunda-feira', 'terca-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sabado', 'domingo']

class AddHorarios(QMainWindow, add_horarios):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)

        self.dias_da_semana = dias_da_semana()
        self.dia_semana.addItems(self.dias_da_semana)

        self.btn_aplicar.clicked.connect(self.aplicar_horarios)


    def aplicar_horarios(self, parent=None):
        data_json = {
            "dia_semana": self.dia_semana.currentText(),
            "horario_inicio": self.hora_inicial.text(),
            "horario_final": self.hora_final.text(),
        }

        response = APPContext.api_client.post(
            "/estabelecimento/horarios",
            data_json
        )

        print(response)

        QMessageBox.information(self, "Sucesso", "Horarios adicionados com sucesso")