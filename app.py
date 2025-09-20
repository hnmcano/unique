import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QStackedWidget)
from window.ui_clientes import Ui_MainWindow as clientes
from window.ui_uniq import Ui_MainWindow as uniq
from window.ui_mesas import Ui_MainWindow as mesas
from models.models import inicializar_banco, adicionar_novo_usuario, listar_clientes

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

        teste = listar_clientes()

        print(teste)

        # 4. Conecte os sinais aos seus métodos.
        # Agora você pode acessar os widgets diretamente.
        self.cad_clientes.clicked.connect(self.salvar_dados)

    def salvar_dados(self):
        # O self.nome_input é acessível diretamente
        Cliente = self.nome_input.text()
        email = self.email_input.text()
        telefone = self.telefone_input.text()

        try:
            adicionar_novo_usuario(Cliente, email, telefone)
            QMessageBox.information(self, "Sucesso", "Usuário adicionado com sucesso!")
            # Limpa os campos após salvar
            self.nome_input.clear()
            self.email_input.clear()
            self.telefone_input.clear()
        except ValueError:
            QMessageBox.warning(self, "Erro", "A informação está incorreta.")
        except Exception as e:
            QMessageBox.critical(self, "Erro de BD", f"Ocorreu um erro: {e}")


class Mesas(QMainWindow, mesas):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)


# Classe para a tela principal
class Uniq(QMainWindow, uniq):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # O self.ticket_window é declarado aqui, mas a instância é criada no método
        self.clientes_window = None
        self.mesas_window = None

        # Conecta o botão para abrir a janela de tickets
        self.btn_clientes.clicked.connect(self.abrir_clientes)
        self.btn_mesas.clicked.connect(self.abrir_mesas)


    def abrir_mesas(self):
        self.mesas_window = Mesas(parent=self)
        self.mesas_window.show()

    def abrir_clientes(self):
        # A nova tela é criada aqui, e 'self' (a janela principal) é o pai.
        # Isso garante que a janela de tickets será fechada quando a janela principal for.
        self.clientes_window = Clientes(parent=self)
        self.clientes_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Uniq()
    window.show()
    sys.exit(app.exec())
