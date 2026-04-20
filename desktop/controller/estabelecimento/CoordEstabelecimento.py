from windows.form_establishment.atualizacao_localizacao_ui import Ui_MainWindow as coord_estabelecimento

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from core.app_context import app_context as APPContext

class CoordEstabelecimento(QMainWindow, coord_estabelecimento):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.carregar_coordenadas()
        self.btn_atualizar.clicked.connect(self.atualizar_coordenadas)

        
    def atualizar_coordenadas(self):
        try:
            lat = self.LatitudeLine.text()
            lon = self.LongitudeLine.text()
            nome = self.NomeLine.text()

            self.coords_estabelecimento = {
                "lat": lat,
                "lon": lon,
                "nome": nome
            }

            response = APPContext.api_client.put("/estabelecimento/coordenadas-estabelecimento", self.coords_estabelecimento)

            QMessageBox.information(self, "Sucesso", "Coordenadas atualizadas com sucesso")

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao buscar dados: {str(e)}")

    def carregar_coordenadas(self):
        try:
            response = APPContext.api_client.get("/estabelecimento/desktop/coordenadas-estabelecimento")

            self.LatitudeLine.setText(str(response["lat"]))
            self.LongitudeLine.setText(str(response["lon"]))
            self.NomeLine.setText(str(response["nome"]))

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao buscar dados: {str(e)}")