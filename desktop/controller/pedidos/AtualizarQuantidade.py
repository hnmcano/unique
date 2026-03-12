from PySide6.QtWidgets import *
from windows.form_delivery.atualizar_quantidade_ui import Ui_MainWindow as EditarItem
from core.app_context import app_context as APPContext
from PySide6.QtCore import Signal


class AtualizarQuantidade_ui(QMainWindow, EditarItem):
    def __init__(self, parent=None, item=None, id=None):
        super().__init__(parent)
        self.setupUi(self)
        self.item = item.copy()
        self.id = id

        print(self.item)

        self.quantidade.setText(str(self.item["quantidade"]))

        self.btn_aumentar.clicked.connect(self.aumentar_quantidade)
        self.btn_diminuir.clicked.connect(self.diminuir_quantidade)
        self.btn_atualizar.clicked.connect(self.atualizar_quantidade)

    def aumentar_quantidade(self):
        self.item["quantidade"] += 1
        self.quantidade.setText(str(self.item["quantidade"]))

    def diminuir_quantidade(self):
        if self.item["quantidade"] > 1:
            self.item["quantidade"] -= 1
            self.quantidade.setText(str(self.item["quantidade"]))

    def atualizar_quantidade(self):
        try:
            response = APPContext.api_client.put(f"pedidos/desktop/atualizar-quantidade", {"pedido_id": self.id, 
                                                                                            "id_itens_pedido": self.item["id_itens_pedido"], 
                                                                                            "produto_id": self.item["produto_id"],
                                                                                            "quantidade": self.item["quantidade"]
                                                                                            })
            

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"{e}")
