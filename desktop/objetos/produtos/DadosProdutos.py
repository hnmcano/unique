
from PySide6.QtWidgets import  QMainWindow
from telas.form_products.data_produto_ui import Ui_MainWindow as DataProduto
from PySide6.QtNetwork import QNetworkAccessManager
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

from scripts.produtos import preencher_dropdown_categoria, atualizar_dados_produtos, inserir_imagem, excluir_produto_base_dados

import base64


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
