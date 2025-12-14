from scripts.produtos import (salvar_dados_produtos, inserir_imagem, exibir_confirmacao_exclusao, adicionar_categoria, preencher_dropdown_categoria, excluir_categoria)
from scripts.clientes import (salvar_dados_clientes)
from scripts.api_externa import (buscar_cep)
from PySide6.QtWidgets import (QApplication, QPushButton, QMainWindow, QMessageBox, QTableWidgetItem, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QGridLayout, QHeaderView, QTableWidget, QAbstractItemView)
from window.form_orders.pedido_mesa_ui import Ui_MainWindow as pedido_mesa
from window.form_products.add_categorias_ui import Ui_Category as addcategorias
from window.form_products.add_produtos_ui import Ui_MainWindow as addprodutos
from window.form_products.produtos_ui import Ui_MainWindow as produtos
from window.form_clients.clientes_ui import Ui_MainWindow as clientes
from window.form_orders.mesas_ui import Ui_MainWindow as mesas
from window.form_box.Caixa_ui import Ui_MainWindow as caixa
from window.form_delivery.delivery_ui import Ui_MainWindow as delivery
from window.unique_ui import Ui_Unique as uniq
from PySide6.QtNetwork import ( QNetworkAccessManager, QNetworkRequest, QNetworkReply)
from PySide6.QtCore import Signal, Qt, QObject
from PySide6.QtGui import QPixmap
import requests
import sys


class Caixa(QMainWindow, caixa):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.ValorCaixa.setText("0,00")

        self.validar_caixa()
        self.open_caixa.clicked.connect(self.iniciar_caixa)
        self.CloseCaixa.clicked.connect(self.fechar_caixa)

    def iniciar_caixa(self):
        valor_caixa = float(self.ValorCaixa.text().replace(",", "."))

        data_json = {
            "valor": valor_caixa
        }

        url = "http://127.0.0.1:8000/caixa/open_box"

        response = requests.post(url, json=data_json)

        if response.status_code == 200:
            QMessageBox.information(self, "Sucesso", "Caixa aberto com sucesso")
            self.CloseCaixa.setDisabled(False)
            self.CloseCaixa.setStyleSheet("""QPushButton {
                background: qlineargradient(
                    spread:pad,
                    x1:0, y1:0,
                    x2:1, y2:0,
                    stop:0 #393939,
                    stop:1 #7d7d7d
                );
                color: white;
                border: 2px solid #282828;
                border-radius: 6px;
                padding: 6px 12px;
            }

            QPushButton::hover{
                background: qlineargradient(
                    spread:pad,
                    x1:0, y1:0,
                    x2:1, y2:0,
                    stop:0 #7d7d7d,
                    stop:1 #393939
                );
            }""")
            self.StatusCaixa.setText("Caixa Aberto")
            self.StatusCaixa.setStyleSheet("background-color: green; color: white; font-weight: bold;")
        else:
            QMessageBox.critical(self, "Erro", f"{response.json().get('detail')}" )
        
        self.ValorCaixa.setText("0,00")

    def fechar_caixa(self):
        try:
            questionamento = QMessageBox.question(self, "Confirmação", "Deseja realmente fechar o caixa?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if questionamento == QMessageBox.No:
                return
            else:
                try:
                    url = "http://127.0.0.1:8000/caixa/close_box"
                    response = requests.get(url)

                    if response.status_code == 200:
                        self.StatusCaixa.setText("Caixa Fechado")
                        self.StatusCaixa.setStyleSheet("background-color: red; color: white; font-weight: bold;")
                        self.CloseCaixa.setDisabled(True)
                        self.CloseCaixa.setStyleSheet("background-color: rgb(91, 91, 91); color: black; font-weight: bold;")
                    else:
                        QMessageBox.critical(self, "Erro", f"{response.json().get('detail')}")
                except Exception as e:
                    QMessageBox.critical(self, "Erro", f"Erro ao fechar caixa: {str(e)}")

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao fechar caixa: {str(e)}")

    def validar_caixa(self):

        url = "http://127.0.0.1:8000/caixa/valid_box"
        response = requests.get(url)

        if response.status_code == 200:
            self.CloseCaixa.setDisabled(False)
            self.StatusCaixa.setText("Caixa Aberto")
            self.StatusCaixa.setStyleSheet("background-color: green; color: white; font-weight: bold;")
        else:
            self.CloseCaixa.setDisabled(True)
            self.CloseCaixa.setStyleSheet("background-color: rgb(91, 91, 91); color: black; font-weight: bold;")
            self.StatusCaixa.setText("Caixa Fechado")
            self.StatusCaixa.setStyleSheet("background-color: red; color: white; font-weight: bold;")
            
class WidgetProdutoDetalhe(QWidget):
    def __init__(self, id, nome, preco, estoque, descricao, parent=None):
        super().__init__(parent)

# Classe para adicionar categorias
class AddCategory(QMainWindow, addcategorias):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.drop_modificar.hide() # Esconde o dropdown inicialmente
        self.btn_excluir.hide() # Esconde o botão de excluir inicialmente

        self.modificar_botao.clicked.connect(self.mostrar_dropdown_categoria)
        self.adicionar_botao.clicked.connect(self.mostrar_input_categoria)
        self.btn_adicionar.clicked.connect(lambda: adicionar_categoria(self))
        self.btn_excluir.clicked.connect(self.excluir_categoria)

    # Função definida para adicionar categoria ao banco de dados

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
            response = requests.get("http://127.0.0.1:8000/produtos/dropdown/categories")
            if response.status_code == 200:
                categories = response.json() 

                for nome in categories:
                    self.drop_modificar.addItem(nome["nome"])
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
        
        excluir_categoria(self, categoria_selecionada)

        try:
            response = requests.delete(f"http://127.0.0.1:8000/produtos/category/{categoria_selecionada}")
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

        preencher_dropdown_categoria(self)
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

# classe para gerenciar produtos
class Produtos(QMainWindow, produtos):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


        self.FilterProducts.setPlaceholderText("Digite para filtrar produtos...")

        columns = ["ID", "Nome", "Preço de Custo", "Preço de venda","Estoqu min",  "Estoque"]

        quantidade_columns = len(columns)
        self.tableWidget.setColumnCount(quantidade_columns)
        self.tableWidget.setHorizontalHeaderLabels(columns)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Interactive)
        self.tableWidget.setSortingEnabled(True)
        header.setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableWidget.setSelectionMode(QTableWidget.SingleSelection)

        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        
        try:
            response = requests.get("http://127.0.0.1:8000/produtos/desktop/table")
            response.raise_for_status()  # Levanta um erro para códigos de status HTTP ruins
            products = response.json()

            self.tableWidget.setRowCount(len(products))
            linha_atual = 0

            for i in products:

                self.tableWidget.setRowHeight(linha_atual, 50)

                item_ordenavel_id = QTableWidgetItem(str(i["id"]))
                self.tableWidget.setItem(linha_atual, 0, item_ordenavel_id)

                item_ordenavel_nome = QTableWidgetItem(i["nome"])
                self.tableWidget.setItem(linha_atual, 1, item_ordenavel_nome)

                item_ordenavel_preco_venda = QTableWidgetItem(str(i["preco_venda"]))
                self.tableWidget.setItem(linha_atual, 2, item_ordenavel_preco_venda)

                item_ordenavel_estoque = QTableWidgetItem(str(i["estoque"]))
                self.tableWidget.setItem(linha_atual, 3, item_ordenavel_estoque)

                item_ordenavel_descricao = QTableWidgetItem(i["descricao"])
                self.tableWidget.setItem(linha_atual, 4, item_ordenavel_descricao)

                linha_atual += 1
                
            self.tableWidget.sortItems(0, Qt.AscendingOrder)

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
            """)
            print(f"Cor do botão {botao_a_restaurar.objectName()} restaurada para um estilo fixo.")

class Delivery(QMainWindow, delivery):
    resposta_delivery = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.FilterPedidos.setPlaceholderText("Pesquisar pedidos realizados.....")

        columns = ["id_pedido", "nome_cliente", "telefone", "data_pedido", "hora_pedido", "status", "valor_total"]

        quantidade_columns = len(columns)

        self.tableWidget.setColumnCount(quantidade_columns)
        self.tableWidget.setHorizontalHeaderLabels(columns)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Interactive)
        self.tableWidget.setShortcutEnabled(True)
        header.setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableWidget.setSelectionMode(QTableWidget.SingleSelection)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        try:
            response = requests.get("http://127.0.0.1:8000/pedidos/delivery/desktop")
            pedidos = response.json().get("detail")
            
            self.tableWidget.setRowCount(len(pedidos))
            linha_atual = 0

            for i in pedidos:
                self.tableWidget.setRowHeight(linha_atual, 50)

                print(i)

                item_ordenavel_id = QTableWidgetItem(str(i["id"]))
                self.tableWidget.setItem(linha_atual, 0, item_ordenavel_id)

                item_ordenavel_nome = QTableWidgetItem(i["nome"])
                self.tableWidget.setItem(linha_atual, 1, item_ordenavel_nome)

                item_ordenavel_telefone = QTableWidgetItem(str(i["telefone"]))
                self.tableWidget.setItem(linha_atual, 2, item_ordenavel_telefone)

                item_ordenavel_data_pedido = QTableWidgetItem(i["data_pedido"])
                self.tableWidget.setItem(linha_atual, 3, item_ordenavel_data_pedido)

                item_ordenavel_hora_pedido = QTableWidgetItem(str(i["hora_pedido"]))
                self.tableWidget.setItem(linha_atual, 4, item_ordenavel_hora_pedido)

                item_ordenavel_status = QTableWidgetItem(i["status"])
                self.tableWidget.setItem(linha_atual, 5, item_ordenavel_status)

                item_ordenavel_valor_total = QTableWidgetItem(str(i["valor_total"]))
                self.tableWidget.setItem(linha_atual, 6, item_ordenavel_valor_total)

                linha_atual += 1
            
            self.tableWidget.sortItems(0, Qt.AscendingOrder)
            
            print(response.json())
                    
        except requests.RequestException as e:
            QMessageBox.critical(self, "Erro", f"Erro ao buscar pedidos: {str(e)}")
        
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

        self.valid_caixa()

        # Ao clicar nos botões, abre as respectivas janelas
        # janela clientes
        self.btn_clientes.clicked.connect(self.abrir_clientes)
        # janela mesas
        self.btn_mesas.clicked.connect(self.abrir_mesas)
        # janela produtos
        self.btn_produtos.clicked.connect(self.abrir_produtos)

        self.btn_delivery.clicked.connect(self.abrir_delivery)

        self.btn_caixa.clicked.connect(self.abrir_caixa)

    # Funções para abrir a janela filhas de mesas, clientes e produtos
    def abrir_caixa(self):
        self.caixa_window = Caixa(parent=self)
        self.caixa_window.show()
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

    def abrir_delivery(self):
        self.delivery_window = Delivery(parent=self)
        self.delivery_window.show()

    def valid_caixa(self):

        url = "http://127.0.0.1:8000/caixa/valid_box"

        response = requests.get(url)

        if response.status_code == 200:
            QMessageBox.information(self, "Caixa Aberto", "Seu caixa esta aberto")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Uniq()
    window.show()
    sys.exit(app.exec())