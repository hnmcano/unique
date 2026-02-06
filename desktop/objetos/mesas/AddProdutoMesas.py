from scripts.produtos import buscar_produtos
from telas.form_orders.add_produtos_ui import Ui_MainWindow as addProdutosMesa
from PySide6.QtWidgets import ( QMainWindow)


class AdicionarProdutoMesa(QMainWindow, addProdutosMesa):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        columns = ["id", "nome", "preco"]


        buscar_produtos(self, columns)

    def filtrar_produtos(self, text):
        for row in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(row, 1)
            if text.lower() in item.text().lower():
                self.tableWidget.showRow(row)
            else:
                self.tableWidget.hideRow(row)
