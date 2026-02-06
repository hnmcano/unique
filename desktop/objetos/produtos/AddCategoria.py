from PySide6.QtWidgets import QMainWindow, QMessageBox
from telas.form_products.add_categorias_ui import Ui_Category as addcategorias

import requests

APIURLDESENV = "http://localhost:8000"

def excluir_categoria(parent=None, categoria_selecionada=None):

    try:
        response = requests.delete(f"{APIURLDESENV}/categorias/category/{categoria_selecionada}")
        if response.status_code == 200:
            QMessageBox.information(parent, "Sucesso", "Categoria excluida com sucesso!")
            parent.preencher_dropdown()  # Atualiza o dropdown
        else:
            QMessageBox.critical(parent, "Erro", "Falha ao excluir categoria.")
    except Exception as e:
        QMessageBox.critical(parent, "Erro", f"Erro ao excluir categoria: {str(e)}")

def adicionar_categoria(parent=None):
    nova_categoria = parent.adicionar_cat_input.text().strip()
    if not nova_categoria:
        QMessageBox.warning(parent, "Erro", "O campo de categoria não pode estar vazio.")
        return

    try:
        response = requests.post(
            f"{APIURLDESENV}/categorias/category",
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



class AddCategoria(QMainWindow, addcategorias):
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
            response = requests.get(f"{APIURLDESENV}/categorias/dropdown/categories")
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
            response = requests.delete(f"{APIURLDESENV}/categorias/category/{categoria_selecionada}")
            if response.status_code == 200:
                QMessageBox.information(self, "Sucesso", "Categoria excluída com sucesso!")
                self.preencher_dropdown()  # Atualiza o dropdown
            else:
                QMessageBox.critical(self, "Erro", "Falha ao excluir categoria.")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao excluir categoria: {str(e)}")
