
from PySide6.QtWidgets import *
from windows.form_products.data_produto_ui import Ui_MainWindow as DataProduto
from PySide6.QtNetwork import QNetworkRequest, QNetworkAccessManager
from PySide6.QtGui import QPixmap
from PySide6.QtCore import *
from core.app_context import app_context as APPContext

import requests
import base64
import json
import os
from config.config import settings

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

def coletar_dados_produtos(self):
    try:
        produto_id = self.produto["id_produto"]
        categoria_id = self.categoria_combo.currentData()
        cod_pdv = self.cod_pdv_input.text()# type: ignore
        nome = self.nome_input.text()# type: ignore
        medida = self.GroupMedida.checkedButton().text()# type: ignore  
        status = self.GroupStatus.checkedButton().text()# type: ignore 
        preco_custo = float(self.preco_custo_input.text().replace(",", "."))# type: ignore
        preco_venda = float(self.preco_venda_input.text().replace(",", "."))# type: ignore
        estoque = int(self.Estoque_input.text())# type: ignore
        estoque_min = int(self.estoque_min_input.text())# type: ignore
        descricao_ = self.desc_input.toPlainText()# type: ignore
        pixmap = QPixmap(self.image_label.pixmap())
    except Exception as e:
        QMessageBox.warning(self, "Erro", f"Erro ao coletar dados: {str(e)}")
        return
    
    print("dados coletados:", produto_id, categoria_id, cod_pdv, nome, medida, status, preco_custo, preco_venda, estoque, estoque_min, descricao_, pixmap)

    buffer = QBuffer()
    buffer.open(QIODevice.OpenModeFlag.WriteOnly)
    pixmap.save(buffer, "PNG")
    image_data = buffer.data().toBase64().data()
    imagem_data_string = image_data.decode("utf-8")

    if self.GroupMedida.checkedButton() is None or self.GroupStatus.checkedButton() is None:
        QMessageBox.warning(self, "Erro", "Selecione uma unidade de medida e um status.")
        return


    return {
        "id_produto": produto_id,
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

def preencher_dropdown_categoria(parent=None):
    parent.categoria_combo.clear()
    parent.categoria_combo.addItem("")
    try:
        response = APPContext.api_client.get("/categorias/dropdown/categories")

        categorias = response

        for categoria in categorias:
            parent.categoria_combo.addItem(categoria["nome"], categoria["id_categoria"])
            
    except Exception as e:
        QMessageBox.critical(parent, "Erro", f"Erro ao buscar categorias: {str(e)}")


class DadosProduto(QMainWindow, DataProduto):
    def __init__(self, produto: dict, parent=None):

        super().__init__(parent)
        self.setupUi(self)
        
        self.network_manager = QNetworkAccessManager(self)

        self.produto = produto        
        self.id = produto["id_produto"]

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
        
        data = base64.b64decode(produto["imagem"])
        self.pixmap = QPixmap()
        self.pixmap.loadFromData(data)
        visualizacao = self.pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.image_label.setPixmap(visualizacao)

        self.selecionar_imagem.clicked.connect(lambda: inserir_imagem(self))
        self.limp_img.clicked.connect(self.limpar_imagem)
        self.excluir_produtos.clicked.connect(lambda: self.excluir_produto_base_dados(self.id))
        self.atualizar_dados.clicked.connect(lambda: self.atualizar_dados_produtos(self.id))
        self.duplicar_produtos.clicked.connect(self.duplicar_produto)

    def limpar_imagem(self):
        self.image_label.clear()

    def atualizar_dados_produtos(self, id):
        dados_produto = coletar_dados_produtos(self)

        if dados_produto is None:
            return
        try:
            QMessageBox.information(self, "Aguarde", "Enviando dados para o servidor!")
            
            response = APPContext.api_client.put(f"/produtos/desktop/alter-product-data-base/{id}", dados_produto)
            QMessageBox.information(self, "Sucesso", "Produto atualizado com sucesso!")
            APPContext.produtos_store.atualizar(response)
        except ValueError:
            QMessageBox.warning(self, "Erro", "A informação está incorreta.")
        except Exception as e:
            QMessageBox.critical(self, "Erro de BD", f"Ocorreu um erro: {e}")

    
    def excluir_produto_base_dados(self, id):
        confirmacao_exclusao = QMessageBox(self)
        confirmacao_exclusao.setIcon(QMessageBox.Question)
        confirmacao_exclusao.setWindowTitle("Confirmar Exclusão")
        confirmacao_exclusao.setText("Tem certeza de que deseja excluir este produto?")
        confirmacao_exclusao.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resposta = confirmacao_exclusao.exec()

        if resposta == QMessageBox.No:
            return

        try:
            response = APPContext.api_client.delete(f"/produtos/desktop/delete-product-data-base/{id}", data=None)
            QMessageBox.information(
                self, "Sucesso", "Produto excluído com sucesso!"
            )

            APPContext.produtos_store.remover(self.produto)
        except requests.RequestException as e:
            QMessageBox.critical(
                self, "Erro", f"Erro ao excluir produto: {str(e)}"
            )

    def duplicar_produto(self):
        dados_produto = coletar_dados_produtos(self)

        quantidade_produtos = len(APPContext.produtos_store.listar())

        if dados_produto is None:
            return

        dados_produto["cod_pdv"] = str(quantidade_produtos + 1)

        try:
            response = APPContext.api_client.post("/produtos/desktop/add/product", dados_produto)
            QMessageBox.information(self, "Sucesso", "Produto duplicado com sucesso!")
            APPContext.produtos_store.adicionar(response)
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao duplicar produto: {str(e)}")


