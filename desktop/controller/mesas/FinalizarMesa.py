from windows.form_orders.finalizar_mesa_ui import Ui_MainWindow
from PySide6.QtWidgets import *
from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QFont
from core.app_context import app_context as APPContext

class FinalizarMesa(QMainWindow, Ui_MainWindow):
    mensagem_recebida = Signal(dict)

    def __init__(self, parent=None, data=None):
        super().__init__()
        self.setupUi(self)
        self.data = data
        self.pagamentos_adicionados = []

        if data["numero"] < 10:
            self.cliente_label.setText(f"MESA 0{data['numero']}")
        else:
            self.cliente_label.setText(f"MESA {data['numero']}")

        self.label.setText("💰 Total: ")
        self.total_label.setText(f"R$ {data['pedido']['valor_total']:.2f}")
        
        self.total_label.setFont(QFont("Arial", 13, QFont.Bold))
        self.total_label.setStyleSheet("color: white;")

        # 🔥 CRIAR A BARRA DE DIFERENÇA
        self.criar_barra_diferenca()

        # 🔥 CRIAR A ÁREA DE PAGAMENTOS
        self.criar_area_pagamentos()

        self.finaliza_pedido.clicked.connect(lambda: self.finalizar_pedido_confirmacao(data))

    def criar_barra_diferenca(self):
        """Cria a barra mostrando Total, Pago e Diferença"""
        # Container da barra
        barra_widget = QWidget()
        barra_layout = QHBoxLayout(barra_widget)
        barra_layout.setContentsMargins(15, 10, 15, 10)
        barra_layout.setSpacing(30)

        # Estilo da barra
        barra_widget.setStyleSheet("""
            QWidget {
                background-color: black;
            }
        """)
        
        # Pago
        self.label_pago = QLabel()
        self.label_pago.setFont(QFont("Arial", 13, QFont.Bold))
        self.label_pago.setStyleSheet("color: #28a745;")
        
        # Diferença
        self.label_diferenca = QLabel()
        self.label_diferenca.setFont(QFont("Arial", 13, QFont.Bold))
        self.label_diferenca.setStyleSheet("color: #dc3545;")

        barra_layout.addWidget(self.label_pago)
        barra_layout.addStretch()
        barra_layout.addWidget(self.label_diferenca)

        self.barra_diferenca_widget = barra_widget
        
        # Atualizar valores iniciais
        self.atualizar_barra_diferenca()

    def criar_area_pagamentos(self):
        """Cria a área para adicionar pagamentos com input e botão"""
        # Container principal
        container = QWidget()
        container_layout = QVBoxLayout(container)
        container_layout.setContentsMargins(10, 10, 10, 10)
        container_layout.setSpacing(10)

        # ===== 1️⃣ ÁREA DE INPUT (TOPO) =====
        area_input = QWidget()
        area_input_layout = QHBoxLayout(area_input)
        area_input_layout.setSpacing(10)

        # Combo de forma de pagamento
        self.combo_pagamento = QComboBox()
        self.combo_pagamento.addItems([
            "PIX - Transferência",
            "CRÉDITO - Cartão de Crédito",
            "DÉBITO - Cartão de Débito",
            "DINHEIRO - Dinheiro em Espécie"
        ])
        self.combo_pagamento.setStyleSheet("""
            QComboBox {
                color: white;
                border: 1px solid #f00000;
                padding: 5px;
                border-radius: 5px;
                font-weight: bold;
                font-size: 12px;
                min-height: 25px;
            }
            QComboBox:hover {
                border: 1px solid #f00000;
            }
            QComboBox::drop-down {
                border: none;
            }
            QComboBox::down-arrow {
                color: #FFD700;
            }
        """)

        # Input de valor
        self.input_valor_pagamento = QLineEdit()
        self.input_valor_pagamento.setPlaceholderText("Valor (ex: 50.00)")
        self.input_valor_pagamento.setStyleSheet("""
            QLineEdit {
                background-color: black;
                color: white;
                border: 1px solid #f00000;
                padding: 5px;
                border-radius: 5px;
                font-weight: bold;
                font-size: 12px;
                min-height: 25px;
                min-width: 100px;
            }
            QLineEdit:focus {
                border: px solid red;
            }
        """)

        # Botão Adicionar (bonito e grande)
        btn_adicionar = QPushButton("➕ ADICIONAR")
        btn_adicionar.setStyleSheet("""
            QPushButton {
                background-color: #f00000;
                color: white;
                border: none;
                padding: 5px 12px;
                border-radius: 5px;
                font-weight: bold;
                font-size: 12px;
                min-height: 25px;
                margin: 0px;
            }
            QPushButton:hover {
                background-color: #FFD700;
            }
            QPushButton:pressed {
                background-color: #FFD700;
            }
        """)
        btn_adicionar.clicked.connect(self.adicionar_pagamento_dialog)

        area_input_layout.addWidget(QLabel("Forma:"), 0)
        area_input_layout.addWidget(self.combo_pagamento, 2)
        area_input_layout.addWidget(QLabel("Valor:"), 0)
        area_input_layout.addWidget(self.input_valor_pagamento, 1)
        area_input_layout.addWidget(btn_adicionar, 0)

        # Estilo da área de input
        area_input.setStyleSheet("""
            QWidget {
                background-color: black;
                border-radius: 5px;
                padding: 2px;
            } 
            QLabel {
                color: white;
                font-weight: bold;
            }
        """)

        container_layout.addWidget(area_input, 0)

        # ===== 2️⃣ TABELA DE PAGAMENTOS (MEIO) =====
        # Wrapper com scroll
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("""
            QScrollArea {
                background-color: transparent;
                border: none;
            }
            QScrollBar:vertical {
                background-color: #1a1a1a;
                width: 10px;
                border-radius: 5px;
            }
            QScrollBar::handle:vertical {
                background-color: #FFD700;
                border-radius: 5px;
            }
        """)

        tabela_widget = QWidget()
        self.layout_pagamentos = QVBoxLayout(tabela_widget)
        self.layout_pagamentos.setSpacing(5)
        self.layout_pagamentos.setContentsMargins(0, 0, 0, 0)
        self.layout_pagamentos.addStretch()

        scroll_area.setWidget(tabela_widget)
        container_layout.addWidget(scroll_area, 1)

        # ===== 3️⃣ BARRA DE DIFERENÇA (EMBAIXO) =====
        self.criar_barra_diferenca()
        container_layout.addWidget(self.barra_diferenca_widget, 0)

        # Substituir o widget_5 pelo novo container
        if hasattr(self, 'widget_5'):
            parent = self.widget_5.parent()
            parent_layout = parent.layout()
            
            # Encontrar índice do widget_5
            for i in range(parent_layout.count()):
                if parent_layout.itemAt(i).widget() == self.widget_5:
                    parent_layout.removeWidget(self.widget_5)
                    self.widget_5.deleteLater()
                    parent_layout.insertWidget(i, container)
                    break

    def adicionar_pagamento_dialog(self):
        """Valida e adiciona o pagamento quando clica no botão"""
        try:
            valor_texto = self.input_valor_pagamento.text().replace("R$", "").replace(",", ".").strip()
            valor = float(valor_texto)
            
            if valor <= 0:
                QMessageBox.warning(self, "Erro", "Digite um valor válido maior que zero!")
                return
            
            valor_total = self.data['pedido']['valor_total']
            
            # Calcular quanto já foi pago
            total_pago = sum(p['valor'] for p in self.pagamentos_adicionados)
            
            if valor + total_pago > valor_total:
                QMessageBox.warning(
                    self, 
                    "Erro", 
                    f"Valor excede o total! Máximo disponível: R$ {valor_total - total_pago:.2f}"
                )
                return
            
            # Pegar o tipo de pagamento
            tipo_completo = self.combo_pagamento.currentText()
            tipo = tipo_completo.split(" - ")[0]
            bandeira = tipo_completo.split(" - ")[1]
            
            # Adicionar o pagamento
            self.adicionar_pagamento(tipo, bandeira, valor)
            
            # Limpar input
            self.input_valor_pagamento.clear()
            self.input_valor_pagamento.setFocus()
            
            # Atualizar barra
            self.atualizar_barra_diferenca()
            
        except ValueError:
            QMessageBox.warning(self, "Erro", "Digite um valor numérico válido!")

    def adicionar_pagamento(self, tipo, bandeira, valor):
        """Adiciona uma linha de pagamento com botão de deletar"""
        linha = QWidget()
        layout = QHBoxLayout(linha)
        layout.setContentsMargins(10, 8, 10, 8)
        layout.setSpacing(10)

        # Esquerda - Tipo e Bandeira
        widget_esquerda = QWidget()
        layout_esquerda = QVBoxLayout(widget_esquerda)
        layout_esquerda.setSpacing(2)
        
        label_tipo = QLabel(tipo)
        label_tipo.setFont(QFont("Arial", 12, QFont.Bold))
        label_bandeira = QLabel(bandeira)
        label_bandeira.setFont(QFont("Arial", 10))
        
        layout_esquerda.addWidget(label_tipo)
        layout_esquerda.addWidget(label_bandeira)

        # Direita - Valor e Botão Deletar
        label_valor = QLabel(f"R$ {valor:.2f}")
        label_valor.setFont(QFont("Arial", 12, QFont.Bold))
        label_valor.setAlignment(Qt.AlignRight)
        
        # Botão de deletar
        btn_deletar = QPushButton("🗑️")
        btn_deletar.setFixedSize(40, 40)
        btn_deletar.setStyleSheet("""
            QPushButton {
                background-color: #dc3545;
                color: white;
                border: none;
                border-radius: 5px;
                font-size: 18px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #c82333;
            }
        """)
        btn_deletar.clicked.connect(lambda: self.remover_pagamento(linha))

        # Montar a linha
        layout.addWidget(widget_esquerda, 1)
        layout.addStretch()
        layout.addWidget(label_valor, 0)
        layout.addWidget(btn_deletar, 0)

        # Estilo da linha
        linha.setStyleSheet("""
            QWidget {
                border-radius: 5px;
                background-color: #2a2a2a;
                padding: 2px;
            }
            QLabel {
                color: white;
                background: transparent;
                border: none;
            }
        """)

        # Inserir antes do stretch
        self.layout_pagamentos.insertWidget(self.layout_pagamentos.count() - 1, linha)
        
        # Armazenar
        self.pagamentos_adicionados.append({
            'tipo': tipo,
            'bandeira': bandeira,
            'valor': valor
        })

    def remover_pagamento(self, widget):
        """Remove um pagamento da lista"""
        self.layout_pagamentos.removeWidget(widget)
        widget.deleteLater()
        
        self.pagamentos_adicionados = [p for p in self.pagamentos_adicionados if p['widget'] != widget]
        
        self.atualizar_barra_diferenca()

    def atualizar_barra_diferenca(self):
        """Atualiza os valores na barra de diferença"""
        valor_total = self.data['pedido']['valor_total']
        valor_pago = sum(p['valor'] for p in self.pagamentos_adicionados)
        valor_diferenca = valor_total - valor_pago

        self.label_pago.setText(f"✅ Pago: R$ {valor_pago:.2f}")
        
        if valor_diferenca > 0:
            self.label_diferenca.setText(f"❌ Falta: R$ {valor_diferenca:.2f}")
        else:
            self.label_diferenca.setText(f"✅ Completo!")
            self.label_diferenca.setStyleSheet("color: #28a745;")

    def finalizar_pedido_confirmacao(self, data):
        # Validar se tem pagamentos
        if not self.pagamentos_adicionados:
            QMessageBox.warning(self, "Aviso", "Adicione pelo menos uma forma de pagamento!")
            return
        
        # Validar se a soma dos pagamentos equals total
        total_pago = sum(p['valor'] for p in self.pagamentos_adicionados)
        if abs(total_pago - data['pedido']['valor_total']) > 0.01:
            QMessageBox.warning(
                self, 
                "Aviso", 
                f"Soma dos pagamentos (R$ {total_pago:.2f}) deve ser igual ao total (R$ {data['pedido']['valor_total']:.2f})!"
            )
            return
        
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Question)
        msg_box.setWindowTitle("Confirmar Finalização")
        
        resumo = "Pagamentos:\n"
        for pag in self.pagamentos_adicionados:
            resumo += f"  • {pag['tipo']} - R$ {pag['valor']:.2f}\n"
        resumo += "\nTem certeza que gostaria de finalizar esse pedido?"
        
        msg_box.setText(resumo)
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        resposta = msg_box.exec()

        if resposta == QMessageBox.Yes:
            try:
                response = APPContext.api_client.put(f"mesas/finalizar-pedido-mesa/{data["id_mesa"]}", 
                                        {
                                            "pedido_id": data["pedido"]["id_pedido_mesa"], 
                                            "status_antigo": data["pedido"]["status"], 
                                            "status_novo": "FINALIZADO",
                                            "pagamentos": self.pagamentos_adicionados
                                            })
                
                QMessageBox.information(self, "Sucesso", "Pedido Finalizado com sucesso!")
                self.close()

            except Exception as e:
                QMessageBox.critical(self, "Erro", f"Falha ao Finalizar pedido. {str(e)}")
                return
