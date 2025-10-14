from connection.network_conn import handle_network_reply
from PySide6.QtWidgets import (QMessageBox, QFileDialog)
from PySide6.QtNetwork import (QNetworkRequest)
from PySide6.QtCore import QUrl, QByteArray, Qt, Signal
from PySide6.QtGui import QPixmap
import requests
import json

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
        url= QUrl("http://127.0.0.1:8000/users/users")
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
def salvar_dados_produtos(parent=None):
        cod_pdv = parent.cod_pdv_input.text()# type: ignore
        cod_sistema = int(parent.cod_sistema_input.text())# type: ignore
        categoria = parent.categoria_combo.currentText()# type: ignore
        nome = parent.nome_input.text()# type: ignore
        preco_custo = float(parent.preco_custo_input.text().replace(",", "."))# type: ignore
        preco_venda = float(parent.preco_venda_input.text().replace(",", "."))# type: ignore
        medida = parent.Medida_input.text()# type: ignore
        estoque = int(parent.Estoque_input.text())# type: ignore
        estoque_min = int(parent.estoque_min_input.text())# type: ignore
        sit_estoque = parent.sit_estoque_input.text()# type: ignore
        ficha_tec = parent.ficha_tec_input.text()# type: ignore
        status_venda = parent.status_venda_input.text()# type: ignore
        descricao_ = parent.desc_input.text()# type: ignore
        
        try:

            QMessageBox.information(parent, "Aguarde", "Enviando dados para o servidor!")
            url= QUrl("http://127.0.0.1:8000/products/products")
            data_json = {
                    "cod_sistema": cod_sistema,
                    "cod_pdv": f"{cod_pdv}",
                    "categoria": f"{categoria}",
                    "nome": f"{nome}",
                    "preco_custo": preco_custo,
                    "preco_venda": preco_venda,
                    "medida": f"{medida}",
                    "estoque": estoque,
                    "estoque_min": estoque_min,
                    "sit_estoque": f"{sit_estoque}",
                    "descricao": f"{descricao_}",
                    "ficha_tecnica": f"{ficha_tec}",
                    "status_venda": f"{status_venda}",
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
            parent.cod_sistema_input.clear()# type: ignore
            parent.categoria_combo.clear()# type: ignore
            parent.nome_input.clear()# type: ignore
            parent.preco_custo_input.clear()# type: ignore
            parent.preco_venda_input.clear()# type: ignore
            parent.Medida_input.clear()# type: ignore
            parent.Estoque_input.clear()# type: ignore
            parent.estoque_min_input.clear()# type: ignore
            parent.sit_estoque_input.clear()# type: ignore
            parent.ficha_tec_input.clear()# type: ignore
            parent.status_venda_input.clear()# type: ignore
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
