from PySide6.QtWidgets import *
from telas.form_products.add_produtos_ui import Ui_MainWindow as addprodutos
from .AddCategoria import AddCategoria
from connection.network_conn import handle_network_reply

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest

import requests
import json

APIURLDESENV = "http://localhost:8000"

def center_window(self):

    screen = QGuiApplication.primaryScreen()
    screen_geometry = screen.availableGeometry()
    window_geometry = self.frameGeometry()

    window_geometry.moveCenter(screen_geometry.center())
    self.move(window_geometry.topLeft())

def preencher_dropdown_categoria(parent=None):
    try:
        response = requests.get(f"{APIURLDESENV}/categorias/dropdown/categories")
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
        
        if parent.image_label is None:
            imagem_data_string = None
        else:
            pixmap = QPixmap(parent.image_label.pixmap())
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
            url= QUrl(f"{APIURLDESENV}/produtos/desktop/add/product")
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


class AddProdutos(QMainWindow, addprodutos):
    janela_fechada = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        center_window(self)

        # Esconde o botão do windows de fechar(X) a janela
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)# type: ignore

        # Gerenciador de rede para requisições HTTP
        self.network_manager = QNetworkAccessManager(self)
    
        preencher_dropdown_categoria(self)
        # Ao clicar no botão selecionar imagem, Aciona a função de inserir imagem localizada em scripts/aux_func.py
        self.selecionar_imagem.clicked.connect(lambda: inserir_imagem(self))
        # Ao clicar no botão salvar, Aciona a função de salvar dados produtos localizada em scripts/aux_func.py
        self.add_produto.clicked.connect(lambda: salvar_dados_produtos(self))
        # Ao clicar no botão cancelar, Aciona a função de confirmação de exclusão localizada em scripts/aux_func.py
        self.cancelar.clicked.connect(lambda: exibir_confirmacao_exclusao(self))
        # Ao clicar no botão adicionar categoria, Aciona a função de abrir a janela de categorias localizada em scripts/aux_func.py
        self.add_categoria.clicked.connect(self.abrir_categoria)


    def abrir_categoria(self):
        self.categoria_window = AddCategoria(parent=self)# type: ignore
        self.categoria_window.show()# type: ignore
