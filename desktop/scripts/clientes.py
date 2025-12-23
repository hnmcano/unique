from connection.network_conn import handle_network_reply
from PySide6.QtWidgets import (QMessageBox, QFileDialog)
from PySide6.QtNetwork import (QNetworkRequest)
from PySide6.QtCore import QUrl, QByteArray, Qt, Signal
from PySide6.QtGui import QPixmap
import requests
import json
from time import sleep


def salvar_dados_clientes(parent=None):

    # O parent.nome_input é acessível diretamente
    cliente = parent.nome_input.text()# type: ignore
    email = parent.email_input.text()# type: ignore
    telefone = parent.telefone_input.text()# type: ignore
    cep = parent.cepinput.text()# type: ignore
    endereco = parent.endereco_input.text()# type: ignore
    bairro = parent.bairro_input.text()# type: ignore
    cidade= parent.cidade_input.text()# type: ignore
    complemento = parent.complemento_input.text()# type: ignore
    referencia = parent.referencia_input.text()# type: ignore

    try:
        QMessageBox.information(parent, "Aguarde", "Enviando dados para o servidor!")
        url= QUrl("http://api.uniqsystems.com.br/clientes/users")
        data_json = {
                "cliente": f"{cliente}",
                "telefone": f"{telefone}",
                "email": f"{email}",
                "cep": f"{cep}",
                "endereco": f"{endereco}",
                "bairro": f"{bairro}",
                "cidade": f"{cidade}",
                "complemento": f"{complemento}",
                "referencia": f"{referencia}"
        }
        print(data_json)

        json_data=json.dumps(data_json).encode("utf-8")
        data_to_send=QByteArray(json_data)
        request= QNetworkRequest(url)
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")# type: ignore
        reply= parent.network_manager.post(request, data_to_send)# type: ignore
        reply.finished.connect(lambda: handle_network_reply(reply, parent))

        #adicionar_novo_usuario(Cliente, email, telefone, cep, endereco, bairro, cidade, complemento, referencia)
        QMessageBox.information(parent, "Sucesso", "Usuário adicionado com sucesso!")
        # Limpa os campos após salvar
        parent.nome_input.clear()# type: ignore
        parent.email_input.clear()# type: ignore
        parent.telefone_input.clear()# type: ignore
        parent.cepinput.clear()# type: ignore
        parent.endereco_input.clear()# type: ignore
        parent.bairro_input.clear()# type: ignore
        parent.cidade_input.clear()# type: ignore
        parent.complemento_input.clear()# type: ignore
        parent.referencia_input.clear()# type: ignore

    except ValueError:
        QMessageBox.warning(parent, "Erro", "A informação está incorreta.")
    except Exception as e:
        QMessageBox.critical(parent, "Erro de BD", f"Ocorreu um erro: {e}")
        # Limpa o objeto de resposta para evitar vazamento de memória (melhor prática)
        reply.deleteLater()
