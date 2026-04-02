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
import keyring

AppContext.api_client = APIClient(settings.API_URL)

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("unique.pos.system")

import requests
import subprocess
import sys
import json

CURRENT_VERSION = settings.CURRENT_VERSION
UPDATE_URL = settings.UPDATE_URL


def exibir_confirmacao_atualizacao(self):
    msg_box = QMessageBox(self)
    msg_box.setIcon(QMessageBox.Question) # type: ignore
    msg_box.setWindowTitle("Atualização Disponível!")
    msg_box.setText("Gostaria de baixar a nova versão?")
    msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No) # type: ignore

    # A resposta é armazenada aqui, o código é bloqueado até o usuário interagir
    resposta = msg_box.exec()

    if resposta == QMessageBox.Yes: # type: ignore
        return True
    else:
        return False

def check_update():
    try:
        data = requests.get(UPDATE_URL) 
        data = data.json() 

        if data["version"] != CURRENT_VERSION:
            autorizacao = exibir_confirmacao_atualizacao(None)
            if autorizacao:
                QMessageBox.information(None, "Atualização", "Iniciando download da atualização...")
                download_and_update(data["url"])
            else:
                QMessageBox.information(None, "Atualização", "Ao reiniciar o aplicativo, a atualização estará disponível.")
                return
        else:
            QMessageBox.information(None, "Atualização", "Aplicativo atualizado.")
    except Exception as e:
        QMessageBox.warning(None, "Erro de Atualização", "Não foi possível verificar atualizações. Verifique sua conexão com a internet.")

def download_and_update(url):
    response = requests.get(url, stream=True)

    with open("update.exe", "wb") as f:
        QMessageBox.information(None, "Download", "Baixando atualização... Isso pode levar alguns minutos.")
        for chunk in response.iter_content(1024):
            f.write(chunk)

    QMessageBox.information(None, "Download", "Download concluído. Iniciando atualização...")

    subprocess.run(["update.exe"])

    sys.exit()

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
        check_update()

        self.setupUi(self)
        center_window(self)

        saved_email = keyring.get_password("unique_pos", "user_email")

        if saved_email:
            self.LoginLine.setText(saved_email)

        self.LoginButton.clicked.connect(self.autenticar_usuario)
        self.CancelButton.clicked.connect(self.cancelar_login)

    def autenticar_usuario(self):
        try:    
            response = AppContext.api_client.post("usuarios/login", {
                "email": self.LoginLine.text(), 
                "senha_hash": self.PassLine.text()
            })

            email = self.LoginLine.text()

            token = response["access_token"]
            AppContext.token = token
            AppContext.api_client.set_token(token)
            AppContext.websocket_client = WebSocketService(AppContext.token)
            AppContext.websocket_client.start()

            keyring.set_password("unique_pos", "user_email", email)

            self.close()

            self.unique_window = unique()
            self.unique_window.show()

        except Exception as e:
            QMessageBox.critical(None, "Erro de Autenticação", "Não foi possível autenticar o usuário. Verifique suas credenciais.")

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