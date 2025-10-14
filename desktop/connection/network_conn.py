
from PySide6.QtNetwork import (QNetworkRequest, QNetworkReply)
from PySide6.QtWidgets import (QMessageBox)
import json

def handle_network_reply(reply: QNetworkReply, parent=None):
    """Processa a resposta do servidor."""

    # 1. Verifica se houve algum erro de rede (ex: falha de conexão)
    if reply.error() != QNetworkReply.NetworkError.NoError:
        QMessageBox.warning(parent,  "Erro", "Erro na rede!")
    else:
        # 2. Lê os dados da resposta
        response_bytes = reply.readAll().data()

        # 2. Obtém o status HTTP
        http_status = reply.attribute(QNetworkRequest.Attribute.HttpStatusCodeAttribute)

        if http_status == 422:
            # AQUI VOCÊ EXIBE A MENSAGEM DE ERRO DETALHADA DA API
            try:
                error_details = json.loads(response_bytes.decode('utf-8'))# type: ignore
                QMessageBox.warning(parent, "Erro", f"Erro 422: Dados Inválidos!\nDetalhes do Servidor:\n{error_details}")
            except json.JSONDecodeError:
                QMessageBox.warning(parent, "Erro", f"Erro 422, mas a resposta de erro não é JSON:\n{response_bytes.decode('utf-8')}")# type: ignore

        # Tenta decodificar a resposta JSON
        try:
            response_json = json.loads(response_bytes.decode('utf-8'))# type: ignore
            
            # Exibe o resultado formatado
            status_text = f"Requisição bem-sucedida!\n"
            status_text += f"Status HTTP: {reply.attribute(QNetworkRequest.Attribute.HttpStatusCodeAttribute)}\n"
            status_text += "Dados Recebidos:\n"
            status_text += json.dumps(response_json, indent=2)
            
            QMessageBox.information(parent, "Sucesso", f"{status_text}")
            
        except json.JSONDecodeError:
            QMessageBox.warning(parent, "Erro", f"{status_text}")