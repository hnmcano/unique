
from PySide6.QtWidgets import *
from telas.form_products.data_produto_ui import Ui_MainWindow as DataProduto
from PySide6.QtNetwork import QNetworkRequest, QNetworkAccessManager
from PySide6.QtGui import QPixmap
from PySide6.QtCore import *
from PySide6.QtNetwork import QNet
from connection.network_conn import handle_network_reply

import requests
import base64
import json

APIURLDESENV = "http://localhost:8000"

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
        url= QUrl(f"{APIURLDESENV}/produtos/desktop/alter-product-data-base/{produto_id}")
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
        reply= parent.network_manager.put(request, data_to_send)# type: ignore
        reply.finished.connect(lambda: handle_network_reply(reply, parent))

        QMessageBox.information(parent, "Sucesso", "Produto atualizado com sucesso!")
        
    except ValueError:
        QMessageBox.warning(parent, "Erro", "A informação está incorreta.")
    except Exception as e:
        QMessageBox.critical(parent, "Erro de BD", f"Ocorreu um erro: {e}")
        # Limpa o objeto de resposta para evitar vazamento de memória (melhor prática)
        reply.deleteLater()

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
            f"{APIURLDESENV}/produtos/desktop/delete-product-data-base/{id}"
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

class DadosProduto(QMainWindow, DataProduto):
    def __init__(self, produto: dict, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        
        self.network_manager = QNetworkAccessManager(self)

        self.produto = produto
        
        self.id = produto["id"]

        preencher_dropdown_categoria(self)

        self.nome_input.setText(produto["nome"])
        self.cod_pdv_input.setText(produto["cod_pdv"])
        self.preco_custo_input.setText(str(produto["preco_custo"]))
        self.preco_venda_input.setText(str(produto["preco_venda"]))
        self.estoque_min_input.setText(str(produto["estoque_min"]))
        self.Estoque_input.setText(str(produto["estoque"]))

        self.categoria_combo.setCurrentText(produto["nome_categoria"])
        
        grupoMedidaTexto = produto["medida"]
        grupoStatusTexto = produto["status_venda"]

        for i in self.GroupMedida.buttons():
            if i.text() == grupoMedidaTexto:
                i.setChecked(True)
                break

        for i in self.GroupStatus.buttons():
            if i.text() == grupoStatusTexto:
                i.setChecked(True)
                break

        self.desc_input.setPlainText(produto["descricao"])
        
        print(self.image_label.size())

        data = base64.b64decode(produto["imagem"])
        self.pixmap = QPixmap()
        self.pixmap.loadFromData(data)
        visualizacao = self.pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.image_label.setPixmap(visualizacao)

        self.selecionar_imagem.clicked.connect(lambda: inserir_imagem(self))
        self.limp_img.clicked.connect(self.limpar_imagem)
        self.excluir_produtos.clicked.connect(self.excluir_produto_atual)
        self.atualizar_dados.clicked.connect(lambda: atualizar_dados_produtos(self))


    def limpar_imagem(self):
        self.image_label.clear()

    def excluir_produto_atual(self):
        excluir_produto_base_dados(self.id, self)
        self.close()
