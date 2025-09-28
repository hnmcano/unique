import sys
import requests
from PySide6.QtWidgets import (QApplication, QPushButton, QMainWindow, QMessageBox, QFileDialog)
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Signal, Qt
from window.ui_clientes import Ui_MainWindow as clientes
from window.ui_uniq import Ui_MainWindow as uniq
from window.ui_mesas import Ui_MainWindow as mesas
from window.ui_produtos import Ui_MainWindow as produtos
from window.window_pedidos.ui_pedido_mesa import Ui_MainWindow as pedido_mesa
from models.models import inicializar_banco, adicionar_novo_usuario, adicionar_novo_produto


# Defina a JanelaSecundaria aqui (código acima)
class window_table(QMainWindow, pedido_mesa):
    janela_fechada = Signal()

    def __init__(self, name_button, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # 3. Chame a função para inicializar o banco de dados.
        inicializar_banco()

        self.label.setText(f"{name_button}")
        self.btn_excluir.clicked.connect(self.exibir_confirmacao_exclusao)

    def closeEvent(self, event):
        # Remove a emissão do sinal aqui, pois a lógica agora está no QMessageBox
        event.accept()

    def exibir_confirmacao_exclusao(self):
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Question)
        msg_box.setWindowTitle("Confirmar Exclusão")
        msg_box.setText("Tem certeza de que deseja fechar esta janela?")
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        # A resposta é armazenada aqui, o código é bloqueado até o usuário interagir
        resposta = msg_box.exec()

        if resposta == QMessageBox.Yes:
            # Se o usuário confirmar, emita o sinal e feche a janela
            self.janela_fechada.emit()
            self.close()
        # Se a resposta for QMessageBox.No, o diálogo simplesmente fecha e nada acontece

# Classe para a tela de clientes (secundária)
class Clientes(QMainWindow, clientes):
    def __init__(self, parent=None):
        # 1. Chame o __init__ do QMainWindow para configurar a janela.
        # O 'parent' é a janela que a criou (opcional).
        super().__init__(parent)

        # 2. Chame o setupUi() para construir a interface.
        # A classe 'clientes' é a que tem o método setupUi.
        self.setupUi(self)

        # 3. Chame a função para inicializar o banco de dados.
        inicializar_banco()

        self.btn_viacep.clicked.connect(self.buscar_cep)

        # 4. Conecte os sinais aos seus métodos.
        # Agora você pode acessar os widgets diretamente.
        self.cad_clientes.clicked.connect(self.salvar_dados)

    def salvar_dados(self):
        # O self.nome_input é acessível diretamente
        Cliente = self.nome_input.text()
        email = self.email_input.text()
        telefone = self.telefone_input.text()
        cep = self.cepinput.text()
        endereco = self.endereco_input.text()
        bairro = self.bairro_input.text()
        cidade= self.cidade_input.text()
        complemento = self.complemento_input.text()
        referencia = self.referencia_input.text()

        try:
            adicionar_novo_usuario(Cliente, email, telefone, cep, endereco, bairro, cidade, complemento, referencia)
            QMessageBox.information(self, "Sucesso", "Usuário adicionado com sucesso!")
            # Limpa os campos após salvar
            self.nome_input.clear()
            self.email_input.clear()
            self.telefone_input.clear()
            self.cepinput.clear()
            self.endereco_input.clear()
            self.bairro_input.clear()
            self.cidade_input.clear()
            self.complemento_input.clear()
            self.referencia_input.clear()
        except ValueError:
            QMessageBox.warning(self, "Erro", "A informação está incorreta.")
        except Exception as e:
            QMessageBox.critical(self, "Erro de BD", f"Ocorreu um erro: {e}")

    def buscar_cep(self):
        """Busca CEP usando ViaCEP"""
        try:
            cep = self.cepinput.text().replace("-", "").replace(".", "").strip()
            if len(cep) != 8:
                QMessageBox.warning(self, "CEP Inválido", "Digite um CEP válido com 8 dígitos")
                return

            response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
            if response.status_code == 200:
                data = response.json()
                if "erro" not in data:
                    self.endereco_input.setText(data.get("logradouro", ""))
                    self.bairro_input.setText(data.get("bairro", ""))
                    self.cidade_input.setText(f"{data.get('localidade', '')}/{data.get('uf', '')}")
                    self.resultado_cep.setText("CEP encontrado!")
                else:
                    QMessageBox.warning(self, "CEP não encontrado", "O CEP informado não foi encontrado")
            else:
                QMessageBox.critical(self, "Erro", "Falha ao buscar CEP")

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro na busca do CEP: {str(e)}")

class Produtos(QMainWindow, produtos):
    def __init__(self, parent=None):
        # 1. Chame o __init__ do QMainWindow para configurar a janela.
        # O 'parent' é a janela que a criou (opcional).
        super().__init__(parent)

        # 2. Chame o setupUi() para construir a interface.
        # A classe 'clientes' é a que tem o método setupUi.
        self.setupUi(self)

        # 3. Chame a função para inicializar o banco de dados.
        inicializar_banco()

        self.add_produto.clicked.connect(self.salvar_produto)
        self.selecionar_imagem.clicked.connect(self.inserir_imagem)

    def salvar_produto(self):
        cod_pdv = self.cod_pdv_input.text()
        cod_sistema = self.cod_sistema_input.text()
        categoria = self.categoria_input.text()
        nome = self.nome_input.text()
        preco_custo = self.preco_custo_input.text()
        preco_venda = self.preco_venda_input.text()
        medida = self.Medida_input.text()
        estoque = self.Estoque_input.text()
        estoque_min = self.estoque_min_input.text()
        sit_estoque = self.sit_estoque_input.text()
        ficha_tec = self.ficha_tec_input.text()
        status_venda = self.status_venda_input.text()

        try:
            adicionar_novo_produto(cod_pdv, cod_sistema, categoria, nome,
                                            preco_custo, preco_venda, medida, estoque,
                                                estoque_min, sit_estoque,ficha_tec, status_venda)
            QMessageBox.information(self, "Sucesso", "Produto adicionado com sucesso!")
            self.cod_pdv_input.clear()
            self.cod_sistema_input.clear()
            self.categoria_input.clear()
            self.nome_input.clear()
            self.preco_custo_input.clear()
            self.preco_venda_input.clear()
            self.Medida_input.clear()
            self.Estoque_input.clear()
            self.estoque_min_input.clear()
            self.sit_estoque_input.clear()
            self.ficha_tec_input.clear()
            self.status_venda_input.clear()
        except ValueError:
            QMessageBox.warning(self, "Erro", "A informação está incorreta.")
        except Exception as e:
            QMessageBox.critical(self, "Erro de BD", f"Ocorreu um erro: {e}")

    def inserir_imagem(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Selecionar Imagem", "", "Arquivos de Imagem (*.png *.jpg *.jpeg *.bmp *.gif)")
        if file_path:
            # Agora sim, imprima o caminho do arquivo para depuração
            print(f"Caminho do arquivo selecionado: {file_path}")
            pixmap = QPixmap(file_path)
            if not pixmap.isNull():
                self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), aspectMode=Qt.KeepAspectRatio))
                self.image_label.setText("")  # Remove o texto quando a imagem é carregada
            else:
                self.image_label.setText("Erro ao carregar a imagem.")

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


# Classe para a tela principal
class Uniq(QMainWindow, uniq):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # O self.ticket_window é declarado aqui, mas a instância é criada no método
        self.clientes_window = None
        self.mesas_window = None
        self.produtos_window = None

        # Conecta o botão para abrir a janela de tickets
        self.btn_clientes.clicked.connect(self.abrir_clientes)
        self.btn_mesas.clicked.connect(self.abrir_mesas)
        self.btn_produtos.clicked.connect(self.abrir_produtos)

    def abrir_mesas(self):
        self.mesas_window = Mesas(parent=self)
        self.mesas_window.show()

    def abrir_clientes(self):
        # A nova tela é criada aqui, e 'self' (a janela principal) é o pai.
        # Isso garante que a janela de tickets será fechada quando a janela principal for.
        self.clientes_window = Clientes(parent=self)
        self.clientes_window.show()

    def abrir_produtos(self):
        # A nova tela é criada aqui, e 'self' (a janela principal) é o pai.
        # Isso garante que a janela de tickets será fechada quando a janela principal for.
        self.produtos_window= Produtos(parent=self)
        self.produtos_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Uniq()
    window.show()
    sys.exit(app.exec())
