from windows.form_config.impressoras_ui import Ui_MainWindow as impressoras_ui
from core.app_context import app_context as APPContext
from PySide6.QtWidgets import QMainWindow
import win32print
import threading
from escpos.printer import Win32Raw


def get_printers():
    printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL | win32print.PRINTER_ENUM_CONNECTIONS)

    lista = []
    for p in printers:
        nome = p[2]
        lista.append(nome)

    return lista

def imprimir_raw_windows(nome, texto):
        hPrinter = win32print.OpenPrinter(nome)

        try:
            hJob = win32print.StartDocPrinter(hPrinter, 1, ("Cupom", None, "RAW"))
            win32print.StartPagePrinter(hPrinter)

            win32print.WritePrinter(hPrinter, texto.encode("cp850"))

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