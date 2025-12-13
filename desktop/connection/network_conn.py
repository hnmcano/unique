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
           
            if reply.url().toString() == "http://127.0.0.1:8000/produtos/dropdown/categories": # type: ignore
                for item in response_json:
                    parent.categoria_combo.addItem(item["nome"])

            print(reply.url().toString())
            
            if reply.url().toString() == f"http://127.0.0.1:8000/produtos/category/": # type: ignore
                for item in response_json:
                    parent.produtos_combo.addItem(item["nome"])

                    
        except json.JSONDecodeError:
            QMessageBox.warning(parent, "Erro", f"Erro Inesperado")