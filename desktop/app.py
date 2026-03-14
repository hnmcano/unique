from  windows.login_ui import Ui_MainWindow as login_ui
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

from services.websocket import WebSocketService 
from controller.unique.unique import Uniq as unique

from infra.api_client import APIClient
from core.app_context import app_context as AppContext
from config.config import settings
from pictures import imagens_rc

import sys
import ctypes

AppContext.api_client = APIClient(settings.API_URL)

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("unique.pos.system")

#funcao para centralizar a janelas
def center_window(self):

    screen = QGuiApplication.primaryScreen()
    screen_geometry = screen.availableGeometry()
    window_geometry = self.frameGeometry()

    window_geometry.moveCenter(screen_geometry.center())
    self.move(window_geometry.topLeft())

class Login(QMainWindow, login_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        center_window(self)

        self.LoginButton.clicked.connect(self.autenticar_usuario)
        self.CancelButton.clicked.connect(self.cancelar_login)

    def autenticar_usuario(self):
        try:    
            response = AppContext.api_client.post("usuarios/login", {
                "email": self.LoginLine.text(), 
                "senha_hash": self.PassLine.text()
            })
    
            token = response["access_token"]

            AppContext.token = token

            AppContext.api_client.set_token(token)

            AppContext.websocket_client = WebSocketService(AppContext.token)
            print("Websocket criado:", AppContext.websocket_client)
            AppContext.websocket_client.start()

            self.close()

            self.unique_window = unique()
            self.unique_window.show()

        except Exception as e:
            return print(e)

    def cancelar_login(self):
        pass

# funcao principal da aplicação
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Unique POS")
    app.setWindowIcon(QIcon(":/unique/icone.png"))
    window = Login()
    window.show()
    sys.exit(app.exec())