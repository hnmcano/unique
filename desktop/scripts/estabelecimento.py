from connection.network_conn import handle_network_reply
from PySide6.QtWidgets import (QMessageBox, QFileDialog)
from PySide6.QtNetwork import (QNetworkRequest)
from PySide6.QtCore import QUrl, QByteArray, Qt, QBuffer, QIODevice
from PySide6.QtGui import QPixmap
import requests
import json
from time import sleep
import os

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