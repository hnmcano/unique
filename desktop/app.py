from scripts.aux_func import (exibir_confirmacao_exclusao, inserir_imagem, salvar_dados_produtos,
                              salvar_dados_clientes, buscar_cep)
from PySide6.QtWidgets import (QApplication, QPushButton, QMainWindow, QMessageBox, QTableWidgetItem, QLabel)
from window.form_orders.ui_pedido_mesa import Ui_MainWindow as pedido_mesa
from window.form_products.ui_add_categorias import Ui_Category as addcategorias
from window.form_products.ui_add_produtos import Ui_MainWindow as addprodutos
from window.form_products.ui_produtos import Ui_MainWindow as produtos
from window.form_clients.ui_clientes import Ui_MainWindow as clientes
from window.form_orders.ui_mesas import Ui_MainWindow as mesas
from window.ui_unique import Ui_Unique as uniq
from PySide6.QtNetwork import ( QNetworkAccessManager)
from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QPixmap
import requests
import json
import sys

# Classe para gerenciar categorias
class AddCategory(QMainWindow, addcategorias):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        
        self.drop_modificar.hide() # Esconde o dropdown inicialmente
        self.btn_excluir.hide() # Esconde o botão de excluir inicialmente   

        self.modificar_botao.clicked.connect(self.mostrar_dropdown_categoria)
        self.adicionar_botao.clicked.connect(self.mostrar_input_categoria)
        self.btn_adicionar.clicked.connect(self.adicionar_categoria)
        self.btn_excluir.clicked.connect(self.excluir_categoria)

    # Função definida para adicionar categoria ao banco de dados
    def adicionar_categoria(self):
        nova_categoria = self.adicionar_cat_input.text().strip()
        if not nova_categoria:
            QMessageBox.warning(self, "Erro", "O campo de categoria não pode estar vazio.")
            return

        try:
            response = requests.post(
                "http://127.0.0.1:8000/products/category",
                json={"categoria": nova_categoria}
            )
            if response.status_code == 200:
                QMessageBox.information(self, "Sucesso", "Categoria adicionada com sucesso!")
                self.adicionar_cat_input.clear()
                self.preencher_dropdown()  # Atualiza o dropdown
            else:
                QMessageBox.critical(self, "Erro", "Falha ao adicionar categoria.") 
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao adicionar categoria: {str(e)}")

    # Função definida para mostrar o input de categoria e ocultar o dropdown
    def mostrar_input_categoria(self):
        self.adicionar_cat_input.show()
        self.btn_adicionar.show()

        if self.btn_excluir.isVisible():
            self.btn_excluir.hide()
            self.drop_modificar.hide()

    # Função definida para mostrar o dropdown de categorias e ocultar o input
    def mostrar_dropdown_categoria(self):
        if self.adicionar_cat_input.isVisible():
            self.adicionar_cat_input.hide()
            self.btn_adicionar.hide()

        self.btn_excluir.show()
        self.drop_modificar.show()
        self.preencher_dropdown()

    # Função definida para preencher o dropdown com categorias do servidor
    def preencher_dropdown(self):
        self.drop_modificar.clear()
        self.drop_modificar.addItem("")  # espaço em branco

        try:
            response = requests.get("http://127.0.0.1:8000/products/dropdown/categories")
            if response.status_code == 200:
                categories = response.json()
                for category in categories:
                    self.drop_modificar.addItem(category["categoria"])
            else:
                # Falha na requisição
                QMessageBox.critical(self, "Erro", "Falha ao buscar categorias")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro na busca das categorias: {str(e)}")# type: ignore      

    def excluir_categoria(self):
        categoria_selecionada = self.drop_modificar.currentText()
        if not categoria_selecionada:
            QMessageBox.warning(self, "Erro", "Nenhuma categoria selecionada para exclusão.")
            return

        try:
            response = requests.delete(f"http://127.0.0.1:8000/products/category/{categoria_selecionada}")
            if response.status_code == 200:
                QMessageBox.information(self, "Sucesso", "Categoria excluída com sucesso!")
                self.preencher_dropdown()  # Atualiza o dropdown
            else:
                QMessageBox.critical(self, "Erro", "Falha ao excluir categoria.")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao excluir categoria: {str(e)}")

# classe para gerenciar pedidos por mesa
class window_table(QMainWindow, pedido_mesa):
    janela_fechada = Signal()

    def __init__(self, name_button, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.label.setText(f"{name_button}")
        # Ao clicar no botão cancelar, Aciona a função de confirmação de exclusão localizada em scripts/aux_func.py
        self.btn_excluir.clicked.connect(lambda: exibir_confirmacao_exclusao(self))

    # Override do método closeEvent para emitir o sinal quando a janela for fechada
    def closeEvent(self, event):
        event.accept()

# classe para gerenciar clientes
class Clientes(QMainWindow, clientes):
    janela_fechada = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)# type: ignore

        # Ao clicar no botão buscar CEP, Aciona a função de buscar CEP localizada em scripts/aux_func.py
        self.btn_viacep.clicked.connect(lambda: buscar_cep(self))
        # Gerenciador de rede para requisições HTTP
        self.network_manager = QNetworkAccessManager(self)
        # Ao clicar no botão salvar, Aciona a função de salvar dados clientes localizada em scripts/aux_func.py
        self.cad_clientes.clicked.connect(lambda: salvar_dados_clientes(self))
        # Ao clicar no botão cancelar, Aciona a função de confirmação de exclusão localizada em scripts/aux_func.py
        self.cancelar.clicked.connect(lambda: exibir_confirmacao_exclusao(self))

# classe para gerenciar produtos
class AddProdutos(QMainWindow, addprodutos):
    janela_fechada = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # Esconde o botão do windows de fechar(X) a janela
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)# type: ignore

        # Gerenciador de rede para requisições HTTP
        self.network_manager = QNetworkAccessManager(self)
        # Limpa e preenche o dropdown de categorias
        self.categoria_combo.clear()
        self.categoria_combo.addItem("")

        # Realiza a requisição para obter as categorias do servidor e preencher o dropdown
        try:
            response = requests.get("http://127.0.0.1:8000/products/dropdown/categories")
            if response.status_code == 200:
                categories = response.json()
                for category in categories:
                    self.categoria_combo.addItem(category["categoria"])
            else:
                # Falha na requisição
                QMessageBox.critical(self, "Erro", "Falha ao buscar categorias")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro na busca das categorias: {str(e)}")
        
        # Ao clicar no botão selecionar imagem, Aciona a função de inserir imagem localizada em scripts/aux_func.py
        self.selecionar_imagem.clicked.connect(lambda: inserir_imagem(self))
        # Ao clicar no botão salvar, Aciona a função de salvar dados produtos localizada em scripts/aux_func.py
        self.add_produto.clicked.connect(lambda: salvar_dados_produtos(self))
        # Ao clicar no botão adicionar categoria, Aciona a função de abrir a janela de categorias localizada em scripts/aux_func.py
        self.add_categoria.clicked.connect(self.abrir_categoria)
        # Ao clicar no botão cancelar, Aciona a função de confirmação de exclusão localizada em scripts/aux_func.py
        self.cancelar.clicked.connect(lambda: exibir_confirmacao_exclusao(self))

    def abrir_categoria(self):
        self.categoria_window = AddCategory(parent=self)# type: ignore
        self.categoria_window.show()# type: ignore

class Produtos(QMainWindow, produtos):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        try:
            response = requests.get("http://127.0.0.1:8000/products/desktop/table")
            response.raise_for_status()  # Levanta um erro para códigos de status HTTP ruins
            products = response.json()


            self.table_products.setRowCount(len(products))

            keys = ["cod_sistema", "cod_pdv", "categoria", "nome", "preco_custo", "preco_venda", "medida", "estoque", "estoque_min", "sit_estoque", "descricao", "ficha_tecnica", "status_venda", "imagem_url"]

            self.table_products.setColumnCount(len(keys))
            self.table_products.setHorizontalHeaderLabels(keys)

            for row_idx, product in enumerate(products):
                for col_idx, key in enumerate(keys):
                    item = QTableWidgetItem(str(product.get(key, "")))
                    self.table_products.setItem(row_idx, col_idx, item)

        except requests.RequestException as e:
            QMessageBox.critical(self, "Erro", f"Erro ao buscar produtos: {str(e)}")

        # Ao clicar no botão adicionar produto, abre a janela de adicionar produtos
        self.add_products.clicked.connect(self.abrir_add_produto)

    def abrir_add_produto(self):
        self.add_produto_window = AddProdutos(parent=self)# type: ignore
        self.add_produto_window.show()# type: ignore

# classe para gerenciar mesas
class Mesas(QMainWindow, mesas):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.estilos_originais = {}

        for botao in self.findChildren(QPushButton):
            if botao.objectName().startswith("Mesa_"):
                botao.clicked.connect(self.abrir_mesas_cor_atualiza)

    def abrir_mesas_cor_atualiza(self):

        # A linha abaixo já retorna o objeto do botão que foi clicado.
        botao_clicado = self.sender()

        # A variável 'name_button' é apenas para fins de depuração ou identificação,
        # mas não deve ser usada para aplicar o estilo.
        name_button = botao_clicado.objectName()

        # Mude a cor do botão clicado chamando o método diretamente no objeto.
        if isinstance(botao_clicado, QPushButton):
            botao_clicado.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                    stop: 0 #000000, stop: 1 #000000);
                color: white;
                border: 2px solid green;
                padding: 12px 24px;
                border-radius: 8px;
                font-weight: bold;
                font-size: 14px;
            }""")

        # 2. Criar e abrir a nova janela
        self.window_table = window_table(name_button=name_button, parent=self)
        self.window_table.show()

        self.window_table.janela_fechada.connect(
            lambda: self.restaurar_cor(botao_clicado.objectName())
        )

    def restaurar_cor(self, nome_do_botao):

        # 5. Restaurar a cor original do botão
        botao_a_restaurar = self.findChild(QPushButton, nome_do_botao)

        # 5. Restaura a cor original do botão, se ele ainda existir

        # Verifica se o botão ainda existe
        if botao_a_restaurar is not None:
            botao_a_restaurar.setStyleSheet("""
                QPushButton {
                    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                        stop: 0 #000000, stop: 1 #000000);
                    color: white;
                    border: 1px solid red;
                    padding: 12px 24px;
                    border-radius: 8px;
                    font-weight: bold;
                    font-size: 14px;
                }

                QPushButton:hover {
                    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                        stop: 0 #4e4e4e, stop: 1 #4e4e4e);
                }

                QPushButton:pressed {
                    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                        stop: 0 #1a5fb4, stop: 1 #4a00e0);
                }
            """)
            print(f"Cor do botão {botao_a_restaurar.objectName()} restaurada para um estilo fixo.")

# classe principal da aplicação            
class Uniq(QMainWindow, uniq):
    def __init__(self):
        # inicializa a classe pai
        super().__init__()
        # instancia a interface do uniq
        self.setupUi(self)
        
       # Inicializa as janelas como None
        self.clientes_window = None
        self.mesas_window = None
        self.produtos_window = None


        # Ao clicar nos botões, abre as respectivas janelas
        # janela clientes
        self.btn_clientes.clicked.connect(self.abrir_clientes)
        # janela mesas
        self.btn_mesas.clicked.connect(self.abrir_mesas)
        # janela produtos
        self.btn_produtos.clicked.connect(self.abrir_produtos)

    # Funções para abrir a janela filhas de mesas, clientes e produtos
    # considerando que a janela Uniq é a janela pai, que ao fechada, fecha as janelas filhas
    def abrir_mesas(self):
        self.mesas_window = Mesas(parent=self)
        self.mesas_window.show()

    def abrir_clientes(self):
        self.clientes_window = Clientes(parent=self)
        self.clientes_window.show()

    def abrir_produtos(self):
        self.produtos_window= Produtos(parent=self)
        self.produtos_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Uniq()
    window.show()
    sys.exit(app.exec())