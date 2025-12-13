from connection.network_conn import handle_network_reply
from PySide6.QtWidgets import (QMessageBox, QFileDialog)
from PySide6.QtNetwork import (QNetworkRequest)
from PySide6.QtCore import QUrl, QByteArray, Qt, Signal
from PySide6.QtGui import QPixmap
import requests
import json
from time import sleep


def salvar_dados_produtos(parent=None):
        categoria_id = parent.categoria_combo.currentData()
        cod_pdv = parent.cod_pdv_input.text()# type: ignore
        nome = parent.nome_input.text()# type: ignore
        preco_custo = float(parent.preco_custo_input.text().replace(",", "."))# type: ignore
        preco_venda = float(parent.preco_venda_input.text().replace(",", "."))# type: ignore
        medida = parent.Medida_input.text()# type: ignore
        estoque = int(parent.Estoque_input.text())# type: ignore
        estoque_min = int(parent.estoque_min_input.text())# type: ignore
        descricao_ = parent.desc_input.text()# type: ignore
        
        try:

            QMessageBox.information(parent, "Aguarde", "Enviando dados para o servidor!")
            url= QUrl("http://127.0.0.1:8000/products/desktop/add")
            data_json = {
                    "categoria_id": f"{categoria_id}",
                    "cod_pdv": f"{cod_pdv}",
                    "nome": f"{nome}",
                    "preco_custo": preco_custo,
                    "preco_venda": preco_venda,
                    "medida": f"{medida}",
                    "estoque": estoque,
                    "estoque_min": estoque_min,
                    "descricao": f"{descricao_}",
                    "ficha_tecnica": "Não",
                    "status_venda": "Ativo",
                    "imagem_url": ""
            }

            print(data_json)
            
            json_data=json.dumps(data_json).encode("utf-8")
            data_to_send=QByteArray(json_data)
            request= QNetworkRequest(url)
            request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")# type: ignore
            reply= parent.network_manager.post(request, data_to_send)# type: ignore
            reply.finished.connect(lambda: handle_network_reply(reply, parent))

            QMessageBox.information(parent, "Sucesso", "Produto adicionado com sucesso!")
            # Limpa os campos após salvar
            parent.cod_pdv_input.clear()# type: ignore
            parent.categoria_combo.clear()# type: ignore
            parent.nome_input.clear()# type: ignore
            parent.preco_custo_input.clear()# type: ignore
            parent.preco_venda_input.clear()# type: ignore
            parent.Medida_input.clear()# type: ignore
            parent.Estoque_input.clear()# type: ignore
            parent.estoque_min_input.clear()# type: ignore
            parent.desc_input.clear()# type: ignore
            parent.image_label.clear()# type: ignore
            parent.image_label.setText("Nenhuma imagem selecionada")# type: ignore
            
        except ValueError:
            QMessageBox.warning(parent, "Erro", "A informação está incorreta.")
        except Exception as e:
            QMessageBox.critical(parent, "Erro de BD", f"Ocorreu um erro: {e}")
            # Limpa o objeto de resposta para evitar vazamento de memória (melhor prática)
            reply.deleteLater()

def inserir_imagem(parent=None):
    file_dialog = QFileDialog()
    file_path, _ = file_dialog.getOpenFileName(parent, "Selecionar Imagem", "", "Arquivos de Imagem (*.png *.jpg *.jpeg *.bmp *.gif)")
    if file_path:
        # Agora sim, imprima o caminho do arquivo para depuração
        print(f"Caminho do arquivo selecionado: {file_path}")
        pixmap = QPixmap(file_path)
        if not pixmap.isNull():
            parent.image_label.setPixmap(pixmap.scaled(parent.image_label.size(), aspectMode=Qt.KeepAspectRatio))# type: ignore
            parent.image_label.setText("")  # Remove o texto quando a imagem é carregada # type: ignore
        else:
            parent.image_label.setText("Erro ao carregar a imagem.")# type: ignore

def exibir_confirmacao_exclusao(parent= None):
    msg_box = QMessageBox(parent)
    msg_box.setIcon(QMessageBox.Question) # type: ignore
    msg_box.setWindowTitle("Confirmar Exclusão")
    msg_box.setText("Tem certeza de que deseja fechar esta janela?\n Todos os dados serão perdidos.")
    msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No) # type: ignore

    # A resposta é armazenada aqui, o código é bloqueado até o usuário interagir
    resposta = msg_box.exec()

    if resposta == QMessageBox.Yes: # type: ignore
        # Se o usuário confirmar, emita o sinal e feche a janela
        parent.janela_fechada.emit() # type: ignore
        parent.close() # type: ignore
    # Se a resposta for QMessageBox.No, o diálogo simplesmente fecha e nada acontece

def adicionar_categoria(parent=None):
    nova_categoria = parent.adicionar_cat_input.text().strip()
    if not nova_categoria:
        QMessageBox.warning(parent, "Erro", "O campo de categoria não pode estar vazio.")
        return

    try:
        response = requests.post(
            "http://127.0.0.1:8000/produtos/category",
            json={"nome": nova_categoria}
        )
        if response.status_code == 200:
            QMessageBox.information(parent, "Sucesso", "Categoria adicionada com sucesso!")
            parent.adicionar_cat_input.clear()
            parent.preencher_dropdown()  # Atualiza o dropdown
        else:
            QMessageBox.critical(parent, "Erro", "Falha ao adicionar categoria.")
    except Exception as e:
        QMessageBox.critical(parent, "Erro", f"Erro ao adicionar categoria: {str(e)}")

def preencher_dropdown_categoria(parent=None):

    try:
        url = QUrl("http://127.0.0.1:8000/produtos/dropdown/categories")
        request = QNetworkRequest(url)
        reply = parent.network_manager.get(request)
        response = reply.finished.connect(lambda: handle_network_reply(reply, parent))

    except Exception as e:
        QMessageBox.critical(parent, "Erro", f"Erro ao buscar categorias: {str(e)}")

def excluir_categoria(parent=None, categoria_selecionada=None):

    try:
        url = QUrl(f"http://127.0.0.1:8000/produtos/category/{categoria_selecionada}")
        request = QNetworkRequest(url)
        reply = parent.network_manager.delete(request)
        response = reply.finished.connect(lambda: handle_network_reply(reply, parent))
    except Exception as e:
        QMessageBox.critical(parent, "Erro", f"Erro ao excluir categoria: {str(e)}")