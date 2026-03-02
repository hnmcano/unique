from PySide6.QtWidgets import *
from PySide6.QtGui import QGuiApplication
from windows.form_config.painel_configuracoes_ui import Ui_MainWindow as painel_configuracoes

from controller.estabelecimento.Estabelecimento import Estabelecimento

def center_window(self):

    screen = QGuiApplication.primaryScreen()
    screen_geometry = screen.availableGeometry()
    window_geometry = self.frameGeometry()

    window_geometry.moveCenter(screen_geometry.center())
    self.move(window_geometry.topLeft())
    
class PainelConfig(QMainWindow, painel_configuracoes):
    def __init__(self, parent=None):
        super(PainelConfig, self).__init__(parent)
        self.setupUi(self)
        center_window(self)

        self.btn_estabelecimento.clicked.connect(self.abrir_estabelecimento)

    def abrir_estabelecimento(self):
        self.estabelecimento_window = Estabelecimento(parent=self)
        self.estabelecimento_window.show()
