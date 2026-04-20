
from PySide6.QtWidgets import (QMainWindow, QWidget, QHBoxLayout, QVBoxLayout,
    QTableWidget, QTableWidgetItem, QPushButton, QMessageBox, QHeaderView
)
from PySide6.QtCore import Qt
from windows.form_establishment.taxa_entregas_ui import Ui_MainWindow
from core.app_context import app_context as APPContext

class TaxasEntregas(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, fretes=None):
        super().__init__(parent)
        self.setupUi(self)

        # dados iniciais
        self.fretes = fretes

        print(self.fretes)

        # inicializações
        self.init_tabela()
        self.preencher_tabela()
        self.init_botoes()

    # =========================
    # 📊 TABELA
    # =========================
    def init_tabela(self):
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels([
            'KM Mín.', 'KM Máx.', 'Valor (R$)', 'Ativo', 'ID'
        ])

        # esconder coluna ID
        self.table.setColumnHidden(4, True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.table.itemChanged.connect(self.on_table_changed)

        # usar layout já existente
        if self.centralwidget.layout() is None:
            self.layout_principal = QVBoxLayout(self.centralwidget)
        else:
            self.layout_principal = self.centralwidget.layout()

        self.layout_principal.addWidget(self.table)

    def preencher_tabela(self):
        """Preencher tabela com dados"""
        self.table.setRowCount(len(self.fretes))
        
        for row, frete in enumerate(self.fretes):
            # KM Mínimo
            item_min = QTableWidgetItem(str(frete['km_minimo']))
            self.table.setItem(row, 0, item_min)
            
            # KM Máximo
            item_max = QTableWidgetItem(str(frete['km_maximo']))
            self.table.setItem(row, 1, item_max)
            
            # Valor
            item_valor = QTableWidgetItem(f"{frete['valor']:.2f}")
            self.table.setItem(row, 2, item_valor)
            
            # Ativo
            item_ativo = QTableWidgetItem()
            item_ativo.setCheckState(Qt.Checked if frete['ativo'] else Qt.Unchecked)
            self.table.setItem(row, 3, item_ativo)

    # =========================
    # 🔘 BOTÕES
    # =========================
    def init_botoes(self):
        layout_botoes = QHBoxLayout()

        self.btn_adicionar = QPushButton('➕ Adicionar Faixa')
        self.btn_adicionar.clicked.connect(self.adicionar_faixa)
        layout_botoes.addWidget(self.btn_adicionar)

        self.btn_salvar = QPushButton('💾 Salvar')
        self.btn_salvar.clicked.connect(self.salvar_faixas)
        self.btn_salvar.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-weight: bold;
                border: none;
                padding: 8px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        layout_botoes.addWidget(self.btn_salvar)

        self.btn_remover = QPushButton('🗑️ Remover')
        self.btn_remover.clicked.connect(self.remover_faixa)
        layout_botoes.addWidget(self.btn_remover)

        self.layout_principal.addLayout(layout_botoes)

    # =========================
    # ➕ ADICIONAR
    # =========================
    def adicionar_faixa(self):
        row = self.table.rowCount()
        self.table.insertRow(row)

        self.table.setItem(row, 0, QTableWidgetItem("0"))
        self.table.setItem(row, 1, QTableWidgetItem("5"))
        self.table.setItem(row, 2, QTableWidgetItem("5.00"))

        item_ativo = QTableWidgetItem()
        item_ativo.setCheckState(Qt.Checked)
        self.table.setItem(row, 3, item_ativo)

    # =========================
    # 🗑️ REMOVER
    # =========================
    def remover_faixa(self):
        row = self.table.currentRow()

        if row < 0:
            QMessageBox.warning(self, "Aviso", "Selecione uma faixa para remover")
            return

        self.table.removeRow(row)

    # =========================
    # 💾 SALVAR
    # =========================
    def salvar_faixas(self):
        try:
            self.fretes_atualizados = []

            for row in range(self.table.rowCount()):
                km_min = float(self.table.item(row, 0).text())
                km_max = float(self.table.item(row, 1).text())
                valor = float(self.table.item(row, 2).text())
                ativo = self.table.item(row, 3).checkState() == Qt.Checked

                if km_max <= km_min:
                    raise ValueError(f"Faixa inválida: {km_min} - {km_max}")

                if valor < 0:
                    raise ValueError(f"Valor inválido: {valor}")

                self.fretes_atualizados.append({
                    "km_minimo": km_min,
                    "km_maximo": km_max,
                    "valor": valor,
                    "ativo": ativo
                })

            print(self.fretes_atualizados)
            response = APPContext.api_client.put("/estabelecimento/desktop/taxas-km", self.fretes_atualizados)

            QMessageBox.information(self, "Sucesso", "Faixas salvas com sucesso!")
            
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao salvar: {str(e)}")

    # =========================
    # 🔄 ATUALIZAÇÃO AUTOMÁTICA
    # =========================
    def on_table_changed(self):
        # Aqui você pode integrar com o mapa depois
        pass