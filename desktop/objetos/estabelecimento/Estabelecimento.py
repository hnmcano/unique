from PySide6.QtWidgets import *
from telas.form_establishment.form_estabelecimento_ui import Ui_MainWindow as estabelecimento

from connection.network_conn import handle_network_reply

from PySide6.QtNetwork import *
from PySide6.QtCore import *
from PySide6.QtGui import *

import json

APIURLDESENV = "http://localhost:8000"


def enviar_dados_estabelecimento(parent=None):
    nome = parent.NomeEstabelecimento.text()  # type: ignore
    endereco = parent.EnderecoEstabelecimento.text()  # type: ignore
    instagram = parent.EstabelecimentoInstagram.text()  # type: ignore
    telefone = parent.TelefoneEstabelecimento.text()  # type: ignore
    pixmap = QPixmap(parent.pixmap_original)

    buffer = QBuffer()
    buffer.open(QIODevice.OpenModeFlag.WriteOnly)
    pixmap.save(buffer, "PNG")
    image_data = buffer.data().toBase64().data()
    imagem_data_string = image_data.decode("utf-8")

    try:
        QMessageBox.information(parent, "Aguarde", "Enviando dados para o servidor!")
        url= QUrl(f"{APIURLDESENV}/estabelecimento/desktop/add")
        data_json = {
                "nome": f"{nome}",
                "endereco": f"{endereco}",
                "instagram": f"{instagram}",
                "telefone": f"{telefone}",
                "logo_base64": f"{imagem_data_string}"
        }
        QMessageBox.information(parent, "Aguarde", "Enviando dados para o servidor!")
        json_data=json.dumps(data_json).encode("utf-8")
        
        data_to_send=QByteArray(json_data)
        request= QNetworkRequest(url)
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")# type: ignore
        reply= parent.network_manager.post(request, data_to_send)# type: ignore
        reply.finished.connect(lambda: handle_network_reply(reply, parent))
        
    except Exception as e:
        QMessageBox.critical(parent, "Erro", f"Erro ao enviar dados: {str(e)}")

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
               