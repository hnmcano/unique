from windows.form_config.impressoras_ui import Ui_MainWindow as impressoras_ui
from core.app_context import app_context as APPContext
from PySide6.QtWidgets import QMainWindow
from datetime import datetime, timedelta
import win32print


# =========================
# CONFIG PAPEL
# =========================
def tamanho_papel(tamanho: str) -> int:
    if not tamanho:
        return 48

    tamanhos = {
        "80mm": 48,
        "60mm": 42,
        "58mm": 36,
        "a4": 80,
        "a5": 60
    }

    return tamanhos.get(str(tamanho).lower(), 48)


# =========================
# IMPRESSORAS
# =========================
def get_printers():
    printers = win32print.EnumPrinters(
        win32print.PRINTER_ENUM_LOCAL | win32print.PRINTER_ENUM_CONNECTIONS
    )
    return [p[2] for p in printers]


# =========================
# FORMATADORES
# =========================
def formatar_telefone(telefone: str) -> str:
    telefone = str(telefone or "")

    if len(telefone) >= 10:
        return f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"
    return telefone


def formatar_cep(cep: str) -> str:
    cep = str(cep or "")

    if len(cep) == 8:
        return f"{cep[:5]}-{cep[5:]}"
    return cep


def formatar_data(data_iso: str) -> str:
    try:
        return (
            datetime.fromisoformat(data_iso) - timedelta(hours=3)
        ).strftime("%d/%m/%Y %H:%M:%S")
    except Exception:
        return ""


# =========================
# BUILDER DE CUPOM
# =========================
class CupomBuilder:
    def __init__(self, largura):
        self.largura = largura
        self.linhas = []

        if largura == 36:
            self.col_qtd = 3
            self.col_preco = 8
            self.col_item = largura - self.col_qtd - self.col_preco - 2
        else:
            self.col_qtd = 4
            self.col_preco = 9
            self.col_item = largura - self.col_qtd - self.col_preco - 2

    def add(self, texto=""):
        self.linhas.append(str(texto))

    def centro(self, texto=""):
        self.linhas.append(f"{str(texto):^{self.largura}}")

    def sep(self):
        self.linhas.append("-" * self.largura)

    def linha_item(self, qtd, nome, preco):
        nome = str(nome)[:self.col_item]
        self.linhas.append(
            f"{str(qtd):<{self.col_qtd}}"
            f"{nome:<{self.col_item}}"
            f"{preco:<{self.col_preco}.2f}"
        )

    def resultado(self):
        return self.linhas


def formatar_nome_produto(nome, tamanho=None):
    if not nome:
        return ""

    ignorar = {"de", "da", "do", "das", "dos", "e"}

    palavras = nome.strip().split()

    # Se for só uma palavra
    if len(palavras) == 1:
        return f"{nome} ({tamanho})" if tamanho else nome

    ultima_palavra = palavras[-1]

    iniciais = ""
    for p in palavras[:-1]:
        if p.lower() not in ignorar:
            iniciais += p[0].upper() + "."

    nome_formatado = f"{iniciais} {ultima_palavra}"

    if tamanho:
        nome_formatado += f" ({tamanho})"

    return nome_formatado

# =========================
# GERAR CUPOM
# =========================
def imprimir_cupom_pedido(self,data, tamanho):
    largura = tamanho_papel(tamanho)

    if largura == 36:
        espaco = 15
    else:
        espaco = 30

    cupom = CupomBuilder(largura)

    entrega = data.get("endereco_entrega", {}) or {}
    cliente = data.get("cliente", {}) or {}

    data_formatada = formatar_data(data.get("data_criacao"))

    v_total = float(data.get("valor_total", 0) or 0)
    v_taxa = float(entrega.get("taxa_entrega", 0) or 0)
    v_subtotal = v_total - v_taxa

    # =========================
    # CABEÇALHO
    # =========================
    cupom.add()
    cupom.centro("UNIQUE SYSTEMS")
    cupom.add(f"Pedido: {data.get('id_pedido','')}")
    cupom.add(f"Data: {data_formatada}")
    cupom.sep()

    # =========================
    # ENTREGA
    # =========================
    cupom.centro("DADOS DE ENTREGA")
    cupom.add(f"CEP: {formatar_cep(entrega.get('cep'))}")
    cupom.add(f"Endereço: {entrega.get('endereco','')} Nº: {entrega.get('numero','')}")
    cupom.add(f"Bairro: {entrega.get('bairro','')}")
    cupom.add(f"Comp: {entrega.get('complemento','')}")
    cupom.add("Previsão: 50 a 70 minutos")
    cupom.sep()

    # =========================
    # CLIENTE
    # =========================
    cupom.centro("DADOS DO CLIENTE")
    cupom.add(f"Nome: {cliente.get('nome','')}")
    cupom.add(f"Telefone: {formatar_telefone(cliente.get('telefone'))}")
    cupom.sep()

    # =========================
    # ITENS
    # =========================
    cupom.add(
        f"{'QTD ':<{cupom.col_qtd}}"
        f"{'ITEM':<{cupom.col_item}}"
        f"{'PREÇO':<{cupom.col_preco}}"
    )

    for item in data.get("itens", []) or []:
        produto = item.get("produtos", {}) or {}

        nome_base = produto.get("nome", "")
        tamanho = item.get("tamanho", "") or ""

        nome = formatar_nome_produto(nome_base, tamanho)

        # 🔥 AQUI ESTÁ O CORRETO
        preco_unitario = float(item.get("valor_unitario", 0) or 0)

        qtd = item.get("quantidade", 1)

        total = preco_unitario * qtd

        cupom.linha_item(qtd, nome, total)

    cupom.sep()

    # =========================
    # TOTAIS
    # =========================
    cupom.add(f"{'SUB-TOTAL:':<{espaco}} R$ {v_subtotal:>10.2f}")
    cupom.add(f"{'TAXA ENTREGA:':<{espaco}} R$ {v_taxa:>10.2f}")
    cupom.add(f"{'TOTAL:':<{espaco}} R$ {v_total:>10.2f}")
    cupom.sep()

    # =========================
    # PAGAMENTO
    # =========================
    metodo = data.get("metodo_pagamento", "")
    cupom.add(f"PAGAMENTO: {metodo}")

    if metodo == "dinheiro":
        valor_pago = float(str(data.get('opcoes_pagamento', '0')).replace(',', '.') or 0)
        troco = max(0, valor_pago - v_total)

        cupom.add(f"{'VALOR RECEBIDO:':<{espaco}} R$ {valor_pago:>10.2f}")
        cupom.add(f"{'TROCO:':<{espaco}} R$ {troco:>10.2f}")
    else:
        cupom.add(f"BANDEIRA: {data.get('opcoes_pagamento','')}")

    cupom.sep()

    # =========================
    # OBS
    # =========================
    obs = entrega.get("observacoes", "")
    if obs:
        cupom.add("OBSERVAÇÕES:")
        cupom.add(obs)

    if cliente.get("cpf"):
        cupom.add(f"CPF NA NOTA: {cliente.get('cpf')}")

    cupom.add("\n\n")

    return cupom.resultado()


# =========================
# IMPRESSÃO RAW
# =========================
def imprimir_raw_windows(nome, conteudo):
    if isinstance(conteudo, list):
        texto = "\n".join(str(x) for x in conteudo if x is not None) + "\n"
    else:
        texto = str(conteudo)

    comando_corte = "\x1d\x56\x00"
    avanco = "\n\n\n\n\n"

    hPrinter = win32print.OpenPrinter(nome)

    try:
        win32print.StartDocPrinter(hPrinter, 1, ("Cupom", None, "RAW"))
        win32print.StartPagePrinter(hPrinter)

        final = texto + avanco + comando_corte
        win32print.WritePrinter(hPrinter, final.encode("cp850", errors="replace"))

        win32print.EndPagePrinter(hPrinter)
        win32print.EndDocPrinter(hPrinter)

    finally:
        win32print.ClosePrinter(hPrinter)


# =========================
# UI
# =========================
class impressoras(QMainWindow, impressoras_ui):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)

        self.ListImpressoras.addItems(get_printers())
        self.tamanho.addItems(["80mm", "60mm", "58mm", "A4", "A5"])

        self.TestarImp.clicked.connect(self.testar_impressao)
        self.AplicarAlteracoes.clicked.connect(self.salvar_config)

    def testar_impressao(self):
        nome = self.ListImpressoras.currentText()

        imprimir_raw_windows(
            nome,
            ["=== TESTE DE IMPRESSÃO ===", "Sistema OK", ""]
        )

    def salvar_config(self):
        impressora = self.ListImpressoras.currentText()
        tamanho_nome = self.tamanho.currentText()

        padrao = self.checkBox.isChecked()

        APPContext.api_client.post("/impressoras/default", {
            "impressora": impressora,
            "padrao": padrao,
            "tamanho": tamanho_nome
        })