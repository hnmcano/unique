from windows.form_config.impressoras_ui import Ui_MainWindow as impressoras_ui
from core.app_context import app_context as APPContext
from PySide6.QtWidgets import QMainWindow
from datetime import datetime, timedelta
import win32print


def get_printers():
    printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL | win32print.PRINTER_ENUM_CONNECTIONS)

    lista = []
    for p in printers:
        nome = p[2]
        lista.append(nome)

    return lista

def imprimir_cupom_pedido(self, data):
    linhas = []
    largura_total = 48

    data_pedido = (datetime.fromisoformat(data.get("data_criacao", "")) - timedelta(hours=3)).strftime("%d/%m/%Y %H:%M:%S")

    def add_centralizado(texto):
        linhas.append(f"{str(texto or ''):^{largura_total}}")

    def add(texto):
        linhas.append(str(texto) if texto is not None else "")

    add("\n") 

    add_centralizado("UNIQUE SYSTEMS")
    add(f"Pedido: {data.get('id_pedido',''):<15}")
    add(f"Data: {str(data_pedido or ''):<15}")
    add("-" * largura_total)

    entrega = data.get("endereco_entrega", {}) or {}
    add_centralizado("DADOS DE ENTREGA")
    add(f"CEP: {str(entrega.get('cep',''))[0:5] + '-' + str(entrega.get('cep',''))[5:9]}")
    add(f"Endereço: {entrega.get('endereco','')}   Nº: {entrega.get('numero','')}")
    add(f"Bairro: {entrega.get('bairro','')}")
    add(f"Comp: {entrega.get('complemento','')}")
    add(f"Previsão: 50 a 70 minutos")
    add("-" * largura_total)

    cliente = data.get("cliente", {}) or {}
    add_centralizado("DADOS DO CLIENTE")
    add(f"Nome: {cliente.get('nome','')}")
    add(f"Telefone: {'(' + str(cliente.get('telefone',''))[0:2] + ') ' + str(cliente.get('telefone',''))[2:7] + '-' + str(cliente.get('telefone',''))[7:]}")
    add("-" * largura_total)

    add(f"{'QTD':<4} {'ITEM':<33} {'PREÇO':>9}")
    
    for item in data.get("itens", []) or []:
        qtd = item.get("quantidade", 1)
        produto = item.get("produtos", {})
        nome = str(produto.get("nome", ""))[:32] 
        preco = float(produto.get("preco_venda", 0) or 0)
        add(f"{str(qtd):<4} {nome:<33} {preco:>9.2f}")

    add("-" * largura_total)
    
    v_total = float(data.get('valor_total', 0) or 0)
    v_taxa = float(entrega.get('taxa_entrega', 0) or 0)
    v_subtotal = v_total - v_taxa
    
    add(f"{'SUB-TOTAL:':<30} R$ {v_subtotal:>14.2f}")
    add(f"{'TAXA DE ENTREGA:':<30} R$ {v_taxa:>14.2f}")
    add(f"{'TOTAL:':<30} R$ {v_total:>14.2f}")
    add("-" * largura_total)

    # Pagamento
    add(f"PAGAMENTO: {data.get('metodo_pagamento', ''):<20}")

    if data.get("metodo_pagamento") == "dinheiro":
        valor_pago = float(str(data.get('opcoes_pagamento', '0')).replace(',', '.') or 0)
        troco = valor_pago - v_total
        add(f"{'VALOR RECEBIDO:':<30} R$ {valor_pago:>14.2f}")
        add(f"{'TROCO:':<30} R$ {max(0, troco):>14.2f}")
    else:
        add(f"BANDEIRA:  {data.get('opcoes_pagamento', ''):<20}")

    add("-" * largura_total)

    obs = entrega.get("observacoes", "")
    if obs:
        add("OBSERVAÇÕES:")
        add(obs)
    
    if cliente.get("cpf"):
        add(f"CPF NA NOTA: {cliente.get('cpf')}")

    add("\n\n") 
    
    return linhas

def imprimir_raw_windows(nome, conteudo):
    # 1. Transforma a lista em string única
    if isinstance(conteudo, list):
        texto_final = "\n".join(str(item) for item in conteudo if item is not None) + "\n"
    else:
        texto_final = conteudo

    comando_corte = "\x1d\x56\x00" 
    avanco_papel = "\n\n\n\n\n" 

    hPrinter = win32print.OpenPrinter(nome)
    try:
        hJob = win32print.StartDocPrinter(hPrinter, 1, ("Cupom", None, "RAW"))
        win32print.StartPagePrinter(hPrinter)

        # Enviamos o texto + avanço + comando de corte
        corpo_do_cupom = texto_final + avanco_papel + comando_corte
        
        win32print.WritePrinter(hPrinter, corpo_do_cupom.encode("cp850"))

        win32print.EndPagePrinter(hPrinter)
        win32print.EndDocPrinter(hPrinter)
    finally:
        win32print.ClosePrinter(hPrinter)

class impressoras(QMainWindow, impressoras_ui):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)

        printers = get_printers()
        self.ListImpressoras.addItems(printers)

        self.TestarImp.clicked.connect(self.testar_impressao)
        self.AplicarAlteracoes.clicked.connect(self.atualizar_impressora)

    def testar_impressao(self):
        nome = self.ListImpressoras.currentText()

        imprimir_raw_windows(
            nome,
            "=== TESTE DE IMPRESSAO ===\nSistema OK\n\n\n"
        )

    def atualizar_impressora(self):
        impressora = self.ListImpressoras.currentText()

        if self.checkBox.isChecked():
            padrao = True
        else:
            padrao = False

        APPContext.api_client.post("/impressoras/default", {"impressora": impressora, "padrao": padrao})