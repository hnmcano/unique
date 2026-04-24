from windows.form_delivery.add_produtos_ui import Ui_MainWindow as addProdutosPedido
from core.app_context import app_context as APPContext
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt

import json


# =========================
# 🔥 DIALOG DE TAMANHO
# =========================
class SelecionarTamanhoDialog(QDialog):
    def __init__(self, tamanhos, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Selecionar tamanho")
        self.setFixedWidth(300)

        self.tamanho_escolhido = None

        layout = QVBoxLayout()

        titulo = QLabel("Escolha o tamanho")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(titulo)

        for t in tamanhos:
            nome = t.get("tamanho")
            preco = float(t.get("valor", 0) or 0)

            btn = QPushButton(f"{nome} - R$ {preco:.2f}")
            btn.setFixedHeight(45)

            btn.setStyleSheet("""
                QPushButton {
                    background-color: #2c3e50;
                    color: white;
                    font-size: 14px;
                    border-radius: 8px;
                }
                QPushButton:hover {
                    background-color: #34495e;
                }
            """)

            btn.clicked.connect(lambda _, tamanho=t: self.selecionar(tamanho))

            layout.addWidget(btn)

        btn_cancelar = QPushButton("Cancelar")
        btn_cancelar.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border-radius: 8px;
                height: 35px;
            }
        """)
        btn_cancelar.clicked.connect(self.reject)

        layout.addWidget(btn_cancelar)

        self.setLayout(layout)

    def selecionar(self, tamanho):
        self.tamanho_escolhido = tamanho
        self.accept()
        return self.tamanho_escolhido


# =========================
# 🧱 MAIN CLASS
# =========================
class AdicionarProdutoMesa(QMainWindow, addProdutosPedido):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.data = data
        print(self.data)

        columns = ["nome", "preco", ""]
        self.buscar_produtos(data, columns)

        produtos = APPContext.api_client.get("/pedidos/desktop/add-produto")
        self.atualizar_tabela(produtos, data)

    # =========================
    # 🔍 FILTRO
    # =========================
    def filtrar_produtos(self, text):
        for row in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(row, 0)
            if text.lower() in item.text().lower():
                self.tableWidget.showRow(row)
            else:
                self.tableWidget.hideRow(row)

    # =========================
    # 🔥 SELEÇÃO DE TAMANHO
    # =========================
    def selecionar_tamanho(self, tamanhos):
        dialog = SelecionarTamanhoDialog(tamanhos, self)

        if dialog.exec():
            return dialog.tamanho_escolhido

        return None

    # =========================
    # ➕ ADICIONAR PRODUTO
    # =========================
    def adicionar_produto(self, row, data):
        try:
            produto = self.tableWidget.item(row, 0).data(Qt.UserRole)
            pedido_id = data["id_mesa"]

            tamanhos = produto.get("tamanhos", [])

            tamanho_selecionado = None
            preco = float(produto.get("preco_venda", 0) or 0)

            # 🔥 Se tiver tamanho → abrir modal
            if tamanhos:
                tamanho_selecionado = self.selecionar_tamanho(tamanhos)
                print("tamanho selecionado:", tamanho_selecionado)

                if not tamanho_selecionado:
                    return  # cancelou

                preco = float(tamanho_selecionado.get("valor", preco) or preco)

            data_json = {
                "mesa_id": f"{pedido_id}",
                "produto_id": f"{produto['id']}",
                "quantidade": 1,
                "valor_unitario": f"{preco}",
                "tamanho": f"{tamanho_selecionado}"
            }

            print("esquema:", data_json)

            # envia tamanho se existir
            if tamanho_selecionado:
                data_json["tamanho"] = tamanho_selecionado.get("tamanho")

            APPContext.api_client.put(
                "/mesas/adicionar-produto",
                data_json
            )

            QMessageBox.information(self, "Sucesso", "Produto adicionado com sucesso!")

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao adicionar produto: {str(e)}")

    # =========================
    # 🧱 CONFIG TABELA
    # =========================
    def buscar_produtos(self, data, columns=None):
        self.FilterProducts.setPlaceholderText("Digite para filtrar produtos...")
        self.FilterProducts.textChanged.connect(self.filtrar_produtos)

        self.tableWidget.setColumnCount(len(columns))
        self.tableWidget.setHorizontalHeaderLabels(columns)

        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)

        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableWidget.setSelectionMode(QTableWidget.SingleSelection)
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)

    # =========================
    # 📦 ATUALIZAR TABELA
    # =========================
    def atualizar_tabela(self, produtos=None, data=None):

        if isinstance(produtos, str):
            produtos = json.loads(produtos)

        self.tableWidget.setRowCount(len(produtos))

        for i, prod in enumerate(produtos):

            # 🔥 indica se tem tamanho
            nome = prod["nome"]
            if prod.get("tamanhos"):
                nome += " (*)"

            item_nome = QTableWidgetItem(nome)
            item_nome.setData(Qt.UserRole, prod)
            item_nome.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            self.tableWidget.setItem(i, 0, item_nome)

            preco = float(prod.get("preco_venda", 0) or 0)
            item_preco = QTableWidgetItem(f"{preco:.2f}")
            item_preco.setTextAlignment(Qt.AlignCenter)
            self.tableWidget.setItem(i, 1, item_preco)

            btn_adicionar = QPushButton("+")
            btn_adicionar.setStyleSheet("""
                QPushButton {
                    background-color: green; 
                    border: none; 
                    color: white; 
                    font-size: 20px; 
                    max-width: 30px; 
                    height: 30px;
                    border-radius: 5px;
                }
                QPushButton:hover {
                    background-color: darkgreen;
                }
            """)

            btn_adicionar.clicked.connect(
                lambda _, row=i: self.adicionar_produto(row, data=data)
            )

            self.tableWidget.setCellWidget(i, 2, btn_adicionar)