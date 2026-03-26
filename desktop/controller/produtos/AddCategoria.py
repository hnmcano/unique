from PySide6.QtWidgets import QMainWindow, QMessageBox
from windows.form_products.add_categorias_ui import Ui_Category as addcategorias
from core.app_context import app_context as APPContext

from config.config import settings


def excluir_categoria(parent=None, categoria_selecionada=None):
    try:
        response = APPContext.api_client.delete(f"/categorias/category/{categoria_selecionada}")
        QMessageBox.information(parent, "Sucesso", "Categoria excluida com sucesso!")
        parent.preencher_dropdown()  # Atualiza o dropdown
    except Exception as e:
        QMessageBox.critical(parent, "Erro", f"Erro ao excluir categoria: {str(e)}")

def adicionar_categoria(parent=None):
    nova_categoria = parent.adicionar_cat_input.text().strip()
    if not nova_categoria:
        QMessageBox.warning(parent, "Erro", "O campo de categoria não pode estar vazio.")
        return

    try:
        response = APPContext.api_client.post("/categorias/category", {"nome": nova_categoria})
        QMessageBox.information(parent, "Sucesso", "Categoria adicionada com sucesso!")
        parent.adicionar_cat_input.clear()
        parent.preencher_dropdown()  # Atualiza o dropdown

    except Exception as e:
        QMessageBox.critical(parent, "Erro", f"Erro ao adicionar categoria: {str(e)}")

class AddCategoria(QMainWindow, addcategorias):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.preencher_dropdown()

        self.excluir_botao.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page)
        )

        self.adicionar_botao.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_2)
        )

        self.btn_adicionar.clicked.connect(lambda: adicionar_categoria(self))
        self.btn_excluir.clicked.connect(self.excluir_categoria)

    # Função definida para adicionar categoria ao banco de dados
    def preencher_dropdown(self):
        self.drop_modificar.clear()
        self.drop_modificar.addItem("")  # espaço em branco

        try:
            response = APPContext.api_client.get("/categorias/dropdown/categories")

            categories = response

            for nome in categories:
                self.drop_modificar.addItem(nome["nome"])

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro na busca das categorias: {str(e)}")# type: ignore

    def excluir_categoria(self):
        categoria_selecionada = self.drop_modificar.currentText()
        if not categoria_selecionada:
            QMessageBox.warning(self, "Erro", "Nenhuma categoria selecionada para exclusão.")
            return
        
        excluir_categoria(self, categoria_selecionada)

        try:
            response = APPContext.api_client.delete(f"/categorias/category/{categoria_selecionada}")
            QMessageBox.information(self, "Sucesso", "Categoria excluída com sucesso!")
            self.preencher_dropdown()  # Atualiza o dropdown
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao excluir categoria: {str(e)}")
