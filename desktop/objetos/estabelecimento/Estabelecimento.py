from PySide6.QtWidgets import *
from telas.form_estabelecimento_ui import Ui_MainWindow as estabelecimento
from scripts.estabelecimento import enviar_dados_estabelecimento

from PySide6.QtNetwork import QNetworkAccessManager
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

class Estabelecimento(QMainWindow, estabelecimento):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.network_manager = QNetworkAccessManager(self)

        self.EnviaDados.clicked.connect(lambda: enviar_dados_estabelecimento(self))

    def mouseDoubleClickEvent(self, event):
        if self.estabelecimento_logo.geometry().contains(event.pos()):
            file_dialog = QFileDialog()
            file_path, _ = file_dialog.getOpenFileName(self, "Selecionar Imagem", "", "Arquivos de Imagem (*.png *.jpg *.jpeg *.bmp *.gif)")
            
            if not file_path:
                return
            
            self.pixmap_original = QPixmap(file_path)

            if self.pixmap_original is None:
                QMessageBox.critical(self, "Erro", "Falha ao carregar a imagem.")
                return

            preview_pixmap = self.pixmap_original.scaled(self.estabelecimento_logo.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)

            self.estabelecimento_logo.setPixmap(preview_pixmap)
            self.estabelecimento_logo.setText("")
               