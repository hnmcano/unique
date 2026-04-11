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
import winreg

import winreg
import requests
import subprocess
import sys

def get_installed_version():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\UniqueSystems")
        value, _ = winreg.QueryValueEx(key, "version")
        winreg.CloseKey(key)
        return value
    except FileNotFoundError:
        return "0.0.0"

CURRENT_VERSION = get_installed_version()
UPDATE_URL = settings.UPDATE_URL # Ajuste conforme necessário

def exibir_confirmacao_atualizacao(parent=None):
    msg_box = QMessageBox(parent)
    msg_box.setIcon(QMessageBox.Icon.Question)
    msg_box.setWindowTitle("Atualização Disponível!")
    msg_box.setText(f"Versão atual: {CURRENT_VERSION}\nNova versão disponível!\n\nGostaria de baixar a atualização?")
    msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
    
    return msg_box.exec() == QMessageBox.StandardButton.Yes

def check_update(parent=None):
    try:
        response = requests.get(UPDATE_URL, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if data["version"] != CURRENT_VERSION:
            if exibir_confirmacao_atualizacao(parent):
                download_and_update(data["url"], parent)
            else:
                QMessageBox.information(parent, "Atualização", 
                    "A atualização estará disponível na próxima inicialização.")
        else:
            QMessageBox.information(parent, "Atualização", 
                "Seu aplicativo está atualizado!")
                
    except requests.exceptions.RequestException:
        QMessageBox.warning(parent, "Erro", 
            "Não foi possível verificar atualizações.\nVerifique sua conexão com a internet.")
    except Exception as e:
        QMessageBox.critical(parent, "Erro Crítico", f"Erro na verificação: {str(e)}")

def download_and_update(url, parent=None):
    try:
        response = requests.get(url, stream=True, timeout=30)
        response.raise_for_status()
        
        # Mostra progresso (opcional)
        QMessageBox.information(parent, "Download", 
            "Baixando atualização... O aplicativo será reiniciado automaticamente.")
        
        with open("update_installer.exe", "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        # Executa o instalador em modo silencioso
        subprocess.Popen(
            ["update_installer.exe", "/VERYSILENT", "/SUPPRESSMSGBOXES", "/NORESTART"],
            shell=True
        )
        sys.exit(0)
        
    except Exception as e:
        QMessageBox.critical(parent, "Erro no Download", 
            f"Falha ao baixar atualização:\n{str(e)}")


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