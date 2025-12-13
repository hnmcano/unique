from connection.network_conn import handle_network_reply
from PySide6.QtWidgets import (QMessageBox, QFileDialog)
from PySide6.QtNetwork import (QNetworkRequest)
from PySide6.QtCore import QUrl, QByteArray, Qt, Signal
from PySide6.QtGui import QPixmap
import requests
import json
from time import sleep


def buscar_cep(parent=None):
    """Busca CEP usando ViaCEP"""
    try:
        cep = parent.cepinput.text().replace("-", "").replace(".", "").strip()# type: ignore
        if len(cep) != 8:
            QMessageBox.warning(parent, "CEP Inválido", "Digite um CEP válido com 8 dígitos")
            return

        response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        if response.status_code == 200:
            data = response.json()
            if "erro" not in data:
                parent.endereco_input.setText(data.get("logradouro", ""))# type: ignore
                parent.bairro_input.setText(data.get("bairro", ""))# type: ignore
                parent.cidade_input.setText(f"{data.get('localidade', '')}/{data.get('uf', '')}")# type: ignore
            else:
                QMessageBox.warning(parent, "CEP não encontrado", "O CEP informado não foi encontrado")
        else:
            QMessageBox.critical(parent, "Erro", "Falha ao buscar CEP")

    except Exception as e:
        QMessageBox.critical(parent, "Erro", f"Erro na busca do CEP: {str(e)}")


            


