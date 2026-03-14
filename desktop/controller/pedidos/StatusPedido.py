from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from windows.form_delivery.status_pedido_ui import Ui_MainWindow as status_pedido
from core.app_context import app_context as APPContext


class StatusPedido(QMainWindow, status_pedido):
    def __init__(self, pedido, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pedido = pedido

        self.btn_em_producao.clicked.connect(lambda: self.atualizar_status(self.pedido, "EM PRODUÇÃO"))
        self.btn_finalizado.clicked.connect(lambda: self.atualizar_status(self.pedido, "FINALIZADO"))
        self.btn_pendente.clicked.connect(lambda: self.atualizar_status(self.pedido, "PENDENTE"))
        self.btn_pronto_retirada.clicked.connect(lambda: self.atualizar_status(self.pedido, "PRONTO PARA RETIRADA"))
        self.btn_saiu_para_entrega.clicked.connect(lambda: self.atualizar_status(self.pedido, "SAIU PARA ENTREGA"))

    def atualizar_status(self, pedido, str_status):
        response = APPContext.api_client.put(f"/pedidos/desktop/atualizar-status", 
                                                {"pedido_id": pedido["id_pedido"], 
                                                "status_antigo": pedido["status"], 
                                                "status_novo": str_status
                                                })

        self.close()

