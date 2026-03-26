from windows.form_delivery.finalizar_pedido_ui import Ui_MainWindow
from PySide6.QtWidgets import *
from core.app_context import app_context as APPContext
from PySide6.QtCore import Signal

def estilo_botao_metodos():
    estilo = """
        background-color: black;
        border: 2px solid white;
        padding: 5px;
        border-radius: 5px; 
    """
    return estilo

class FinalizarPedido(QMainWindow, Ui_MainWindow):
    mensagem_recebida = Signal(dict)

    def __init__(self, parent=None, data=None):
        super().__init__()
        self.setupUi(self)

        if data["metodo_pagamento"] == "pix":
            self.btnpix.setStyleSheet(estilo_botao_metodos())
        elif data["metodo_pagamento"] == "credito":
            self.btncredito.setStyleSheet(estilo_botao_metodos())
        elif data["metodo_pagamento"] == "debito":
            self.btndebito.setStyleSheet(estilo_botao_metodos())
        elif data["metodo_pagamento"] == "dinheiro":
            self.btndinheiro.setStyleSheet(estilo_botao_metodos())

        self.cliente_label.setText(data["cliente"]["nome"])
        self.total_label.setText(f"R$ {data['valor_total']:.2f}")
               
        self.layout_pagamentos = QVBoxLayout()
        self.widget_5.setLayout(self.layout_pagamentos)

        # adicionando exemplo
        self.adicionar_pagamento(data["metodo_pagamento"], data["opcoes_pagamento"], data["valor_total"])
        self.layout_pagamentos.addStretch()

        self.finaliza_pedido.clicked.connect(lambda: self.finalizar_pedido_confirmacao(data))

    def adicionar_pagamento(self, tipo, bandeira, valor):
        linha = QWidget()
        layout = QHBoxLayout(linha)

        widget_esquerda = QWidget()
        widget_direita = QWidget()

        layout_esquerda = QVBoxLayout(widget_esquerda)
        layout_direita = QVBoxLayout(widget_direita)

        label_tipo = QLabel(tipo)
        label_bandeira = QLabel(bandeira)
        label_valor = QLabel(f"R$ {valor:.2f}")
        Label_suporte = QLabel("")

        # esquerda
        layout_esquerda.addWidget(label_tipo)
        layout_esquerda.addWidget(label_bandeira)

        # direita
        layout_direita.addWidget(Label_suporte)
        layout_direita.addWidget(label_valor)

        # 🔥 ESSENCIAL (faltava isso)
        layout.addWidget(widget_esquerda)
        layout.addStretch()
        layout.addWidget(widget_direita)

        linha.setStyleSheet("""
            QWidget {
                border: 1px solid #ddd;
                border-radius: 2px;
                background: transparent;         
            }
        """)

        widget_esquerda.setStyleSheet("""
            QWidget {
                border: none;
                background: transparent;
            }

            QLabel {
                border: none;
                background: transparent;
                color: white;
                font-weight: bold;
                font-size: 14px;
            }
        """)

        widget_direita.setStyleSheet("""
            QWidget {
                border: none;
                background: transparent;
            }

            QLabel {
                border: none;
                background: transparent;
                color: white;
                font-weight: bold;
                font-size: 14px;
            }
        """)

        self.layout_pagamentos.addWidget(linha)

    def finalizar_pedido_confirmacao(self, data):
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Question) # type: ignore
        msg_box.setWindowTitle("Confirmar Finalização")
        msg_box.setText("Tem certeza que gostaria de finalizar esse pedido? Não será possivel alterar o pedido.")
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No) # type: ignore

        # A resposta é armazenada aqui, o código é bloqueado até o usuário interagir
        resposta = msg_box.exec()

        if resposta == QMessageBox.Yes: # type: ignore
            # Se o usuário confirmar, emita o sinal e feche a janela
            try:
                response = APPContext.api_client.put("pedidos/desktop/atualizar-status", 
                                        {
                                            "pedido_id": data["id_pedido"], 
                                            "status_antigo": data["status"], 
                                            "status_novo": "FINALIZADO"
                                            })
                
                QMessageBox.information(self, "Sucesso", "Pedido Finalizado com sucesso!")
                print("Pedido atualizado com sucesso")
                self.close() # type: ignore

            except Exception as e:
                QMessageBox.critical(self, "Erro", f"Falha ao Finalizar pedido. {str(e)}")
                return