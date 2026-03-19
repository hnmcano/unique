import win32print
from escpos.printer import Win32Raw

def get_printers():
    printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL | win32print.PRINTER_ENUM_CONNECTIONS)

    lista = []
    for p in printers:
        nome = p[2]
        lista.append(nome)

    return lista

def testar_impressao():
        printers = get_printers()
        printers = printers[0]
        
        print(printers)

        # try:
        #     p = Win32Raw(printers)
        #     p.text("=== TESTE DE IMPRESSAO ===\n")
        #     p.text("Sistema OK\n")
        #     p.cut()
        #     return True
        # except Exception as e:
        #     print(e)
        #     return False
        

if __name__ == "__main__":
    testar_impressao()




    