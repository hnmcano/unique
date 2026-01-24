from connection.network_conn import handle_network_reply
from PySide6.QtWidgets import (QMessageBox, QFileDialog, QRadioButton, QButtonGroup)
from PySide6.QtNetwork import (QNetworkRequest)
from PySide6.QtCore import QUrl, QByteArray, Qt, QBuffer, QIODevice
from PySide6.QtGui import QPixmap
import requests
import json
from time import sleep


def salvar_dados_produtos(parent=None):
        categoria_id = parent.categoria_combo.currentData()
        cod_pdv = parent.cod_pdv_input.text()# type: ignore
        nome = parent.nome_input.text()# type: ignore
        botão_marcado = parent.buttonGroup.checkedButton()# type: ignore   
        medida = botão_marcado.text()# type: ignore
        preco_custo = float(parent.preco_custo_input.text().replace(",", "."))# type: ignore
        preco_venda = float(parent.preco_venda_input.text().replace(",", "."))# type: ignore
        estoque = int(parent.Estoque_input.text())# type: ignore
        estoque_min = int(parent.estoque_min_input.text())# type: ignore
        descricao_ = parent.desc_input.toPlainText()# type: ignore
        pixmap = QPixmap(parent.pixmap_original)
        

        buffer = QBuffer()
        buffer.open(QIODevice.OpenModeFlag.WriteOnly)
        pixmap.save(buffer, "PNG")
        image_data = buffer.data().toBase64().data()
        imagem_data_string = image_data.decode("utf-8")

        if botão_marcado is None:
            QMessageBox.warning(parent, "Erro", "Selecione uma unidade de medida.")
            return

        try:
            QMessageBox.information(parent, "Aguarde", "Enviando dados para o servidor!")
            url= QUrl("http://api.uniqsystems.com.br/produtos/desktop/add/product")
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
                    "imagem_name": f"{nome}.png",
                    "imagem": f"{imagem_data_string}"
            }

           
            json_data=json.dumps(data_json).encode("utf-8")
            data_to_send=QByteArray(json_data)
            request= QNetworkRequest(url)
            request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")# type: ignore
            reply= parent.network_manager.post(request, data_to_send)# type: ignore
            reply.finished.connect(lambda: handle_network_reply(reply, parent))

            QMessageBox.information(parent, "Sucesso", "Produto adicionado com sucesso!")

            #Limpa os campos após salvar
            parent.cod_pdv_input.clear()# type: ignore
            parent.categoria_combo.clear()# type: ignore
            parent.nome_input.clear()# type: ignore
            parent.preco_custo_input.clear()# type: ignore
            parent.preco_venda_input.clear()# type: ignore
            
            parent.buttonGroup.setExclusive(False) # type: ignore
            for button in parent.buttonGroup.buttons(): # type: ignore
                button.setChecked(False)
            parent.buttonGroup.setExclusive(True) # type: ignore

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
        parent.pixmap_original = QPixmap(file_path)
        if not parent.pixmap_original.isNull():
            preview_pixmap = parent.pixmap_original.scaled(parent.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            parent.image_label.setPixmap(preview_pixmap)
            parent.image_label.setText("")
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
            "http://api.uniqsystems.com.br/produtos/category",
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
        response = requests.get("http://api.uniqsystems.com.br/produtos/dropdown/categories")
        if response.status_code == 200:
            categorias = response.json()
            parent.categoria_combo.clear()
            parent.categoria_combo.addItem("")

            for categoria in categorias:
                parent.categoria_combo.addItem(categoria["nome"], categoria["id"])
        else:
            QMessageBox.critical(parent, "Erro", "Falha ao buscar categorias.")

    except Exception as e:
        QMessageBox.critical(parent, "Erro", f"Erro ao buscar categorias: {str(e)}")

def excluir_categoria(parent=None, categoria_selecionada=None):

    try:
        response = requests.delete(f"http://api.uniqsystems.com.br/produtos/category/{categoria_selecionada}")
        if response.status_code == 200:
            QMessageBox.information(parent, "Sucesso", "Categoria excluida com sucesso!")
            parent.preencher_dropdown()  # Atualiza o dropdown
        else:
            QMessageBox.critical(parent, "Erro", "Falha ao excluir categoria.")
    except Exception as e:
        QMessageBox.critical(parent, "Erro", f"Erro ao excluir categoria: {str(e)}")

def excluir_produto_base_dados(id, parent=None):

    confirmacao_exclusao = QMessageBox(parent)
    confirmacao_exclusao.setIcon(QMessageBox.Question)
    confirmacao_exclusao.setWindowTitle("Confirmar Exclusão")
    confirmacao_exclusao.setText("Tem certeza de que deseja excluir este produto?")
    confirmacao_exclusao.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

    resposta = confirmacao_exclusao.exec()

    if resposta == QMessageBox.No:
        return

    try:
        response = requests.delete(
            f"http://api.uniqsystems.com.br/produtos/desktop/delete-product-data-base/{id}"
        )

        if response.status_code == 200:
            QMessageBox.information(
                parent, "Sucesso", "Produto excluído com sucesso!"
            )
        else:
            QMessageBox.critical(
                parent, "Erro",
                f"Falha ao excluir produto (status {response.status_code})"
            )

    except requests.RequestException as e:
        QMessageBox.critical(
            parent, "Erro", f"Erro ao excluir produto: {str(e)}"
        )

def atualizar_dados_produtos(parent=None):
        
        produto_id = parent.produto["id"]

        categoria_id = parent.categoria_combo.currentData()
        cod_pdv = parent.cod_pdv_input.text()# type: ignore
        nome = parent.nome_input.text()# type: ignore
        medida = parent.GroupMedida.checkedButton().text()# type: ignore  
        status = parent.GroupStatus.checkedButton().text()# type: ignore 
        preco_custo = float(parent.preco_custo_input.text().replace(",", "."))# type: ignore
        preco_venda = float(parent.preco_venda_input.text().replace(",", "."))# type: ignore
        estoque = int(parent.Estoque_input.text())# type: ignore
        estoque_min = int(parent.estoque_min_input.text())# type: ignore
        descricao_ = parent.desc_input.toPlainText()# type: ignore
        pixmap = QPixmap(parent.image_label.pixmap())
        

        buffer = QBuffer()
        buffer.open(QIODevice.OpenModeFlag.WriteOnly)
        pixmap.save(buffer, "PNG")
        image_data = buffer.data().toBase64().data()
        imagem_data_string = image_data.decode("utf-8")

        if parent.GroupMedida.checkedButton() is None or parent.GroupStatus.checkedButton() is None:
            QMessageBox.warning(parent, "Erro", "Selecione uma unidade de medida e um status.")
            return

        try:
            QMessageBox.information(parent, "Aguarde", "Enviando dados para o servidor!")
            url= QUrl(f"http://api.uniqsystems.com.br/produtos/desktop/alter-product-data-base/{produto_id}")
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
                    "status_venda": f"{status}",
                    "imagem_name": f"{nome}.png",
                    "imagem": f"{imagem_data_string}"
            }

           
            json_data=json.dumps(data_json).encode("utf-8")
            data_to_send=QByteArray(json_data)
            request= QNetworkRequest(url)
            request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")# type: ignore
            reply= parent.network_manager.post(request, data_to_send)# type: ignore
            reply.finished.connect(lambda: handle_network_reply(reply, parent))

            QMessageBox.information(parent, "Sucesso", "Produto atualizado com sucesso!")
            
        except ValueError:
            QMessageBox.warning(parent, "Erro", "A informação está incorreta.")
        except Exception as e:
            QMessageBox.critical(parent, "Erro de BD", f"Ocorreu um erro: {e}")
            # Limpa o objeto de resposta para evitar vazamento de memória (melhor prática)
            reply.deleteLater()