from connection.network_conn import handle_network_reply
from PySide6.QtWidgets import (QMessageBox, QFileDialog)
from PySide6.QtNetwork import (QNetworkRequest)
from PySide6.QtCore import QUrl, QByteArray, Qt, QBuffer, QIODevice
from PySide6.QtGui import QPixmap
import requests
import json
from time import sleep

def enviar_dados_estabelecimento(parent=None):
    nome = parent.NomeEstabelecimento_input.text()  # type: ignore
    endereco = parent.EnderecoEstabelecimento_input.text()  # type: ignore
    instagram = parent.InstagramEstabelecimento_input.text()  # type: ignore
    telefone = parent.TelefoneEstabelecimento_input.text()  # type: ignore
    pixmap = QPixmap(parent.estabelecimento_logo.pixmap())

    buffer = QBuffer()
    buffer.open(QIODevice.OpenModeFlag.WriteOnly)
    pixmap.save(buffer, "PNG")
    image_data = buffer.data().toBase64().data()
    imagem_data_string = image_data.decode("utf-8")

    try:
        QMessageBox.information(parent, "Aguarde", "Enviando dados para o servidor!")
        url= QUrl("http://api.uniqsystems.com.br/estabelecimento/desktop/add/estabelecimento")
        data_json = {
                "nome": f"{nome}",
                "endereco": f"{endereco}",
                "instagram": f"{instagram}",
                "telefone": f"{telefone}",
                "imagem": f"{imagem_data_string}"
        }
        print(data_json)

        json_data=json.dumps(data_json).encode("utf-8")

        reply = requests.post(url, json_data, headers={"Content-Type": "application/json"})
        handle_network_reply(reply, parent=parent)
        
    except Exception as e:
        QMessageBox.critical(parent, "Erro", f"Erro ao enviar dados: {str(e)}")