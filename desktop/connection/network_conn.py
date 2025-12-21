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

        elif http_status == 200:
            # AQUI VOCÊ EXIBE A MENSAGEM DE SUCESSO DA API
            QMessageBox.information(parent, "Sucesso", "Dados enviados com sucesso!")