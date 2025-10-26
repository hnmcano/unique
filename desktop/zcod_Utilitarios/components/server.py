from flask import Flask, request, jsonify
import win32print
import win32ui
import win32con
import threading
import time
import logging
from datetime import datetime

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("ticket_server.log"),
        logging.StreamHandler()
    ]
)

class TicketServer:
    def __init__(self):
        self.app = Flask(__name__)
        self.server_thread = None
        self.is_running = False
        self.setup_routes()

    def setup_routes(self):
        @self.app.route("/imprimir_ticket", methods=["POST"])
        def api_imprimir():
            data = request.get_json()
            if not data:
                return jsonify({"status":"erro","mensagem":"Nenhum dado enviado"}), 400

            # Monta o ticket
            linhas = self.montar_ticket(data)

            try:
                resultado = self.imprimir_ticket(linhas)
                return jsonify({"status":"sucesso","mensagem":resultado})
            except Exception as e:
                return jsonify({"status":"erro","mensagem":str(e)}), 500

        @self.app.route("/health", methods=["GET"])
        def health_check():
            return jsonify({
                "status": "online",
                "service": "ticket_printer",
                "timestamp": datetime.now().isoformat()
            })

        @self.app.route("/shutdown", methods=["POST"])
        def shutdown():
            if self.is_running:
                self.stop_server()
                return jsonify({"status": "shutting_down"})
            return jsonify({"status": "already_stopped"})

    def montar_ticket(self, data):
        linhas = []
        linhas.append(data.get("nome_loja","MenuDino"))
        linhas.append(f"Pedido: {data.get('pedido','')}  Data: {data.get('data','')}")
        linhas.append("")

        entrega = data.get("entrega", {})
        linhas.append("Dados de Entrega (Entregar no endereço)")
        linhas.append(f"CEP: {entrega.get('cep','')}")
        linhas.append(f"Endereço: {entrega.get('endereco','')}")
        linhas.append(f"Bairro: {entrega.get('bairro','')}")
        linhas.append(f"Complemento: {entrega.get('complemento','')}")
        linhas.append(f"Ref: {entrega.get('ref','')}")
        linhas.append(f"Cidade: {entrega.get('cidade','')}")
        linhas.append(f"Previsão de Entrega: {entrega.get('previsao_entrega','')}")
        linhas.append("")

        cliente = data.get("cliente", {})
        linhas.append("Dados do Cliente")
        linhas.append(f"Nome: {cliente.get('nome','')}")
        linhas.append(f"E-mail: {cliente.get('email','')}")
        linhas.append(f"Telefone(s): {cliente.get('telefone','')}")
        linhas.append("")

        linhas.append("Itens do Pedido")
        linhas.append("Qtd  Item                              Preço")
        for item in data.get("itens", []):
            qtd = str(item.get("quantidade",""))
            nome = item.get("nome","")
            preco = item.get("preco","")
            linha_item = f"{qtd:<4}{nome:<32}{preco:>6}"
            linhas.append(linha_item)
        linhas.append("")

        linhas.append(f"Sub-Total:           {data.get('subtotal','')}")
        linhas.append(f"Taxa de Entrega:     {data.get('taxa_entrega','')}")
        linhas.append("------------------------------")
        linhas.append(f"Total:               {data.get('total','')}")
        linhas.append("")

        linhas.append("Forma de Pagamento")
        linhas.append(data.get("pagamento",""))
        linhas.append("")

        linhas.append("Observações")
        linhas.append(data.get("observacoes",""))
        if data.get("cpf"):
            linhas.append(f"Incluir CPF na Nota Fiscal, CPF: {data['cpf']}")

        return linhas

    def imprimir_ticket(self, linhas):
        printer_name = win32print.GetDefaultPrinter()
        hprinter = win32print.OpenPrinter(printer_name)

        printer_dc = win32ui.CreateDC()
        printer_dc.CreatePrinterDC(printer_name)
        printer_dc.SetMapMode(win32con.MM_TWIPS)

        printer_dc.StartDoc("Ticket")
        printer_dc.StartPage()

        fonte = win32ui.CreateFont({
            "name": "Consolas",
            "height": 180
        })
        printer_dc.SelectObject(fonte)

        y = -100
        largura_papel = 576
        altura_fonte = 180
        espaco_entre_linhas = altura_fonte + 50

        for linha in linhas:
            linha = linha.strip()
            if not linha:
                y -= espaco_entre_linhas
                continue
            largura_texto, _ = printer_dc.GetTextExtent(linha)
            x = max((largura_papel - largura_texto)//2, 50)
            printer_dc.TextOut(x, y, linha)
            y -= espaco_entre_linhas

        printer_dc.EndPage()
        printer_dc.EndDoc()
        printer_dc.DeleteDC()
        win32print.ClosePrinter(hprinter)
        return "Ticket enviado para impressão!"

    def run_server(self):
        """Executa o servidor em uma thread separada"""
        try:
            logging.info("Iniciando servidor Flask na porta 5000...")
            self.is_running = True
            self.app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False)
        except Exception as e:
            logging.error(f"Erro no servidor: {e}")
            self.is_running = False

    def start_server(self):
        """Inicia o servidor em background"""
        if not self.is_running:
            self.server_thread = threading.Thread(target=self.run_server, daemon=True)
            self.server_thread.start()
            time.sleep(2)  # Dar tempo para o servidor iniciar
            return True
        return False

    def stop_server(self):
        """Para o servidor"""
        self.is_running = False
        # O Flask não tem um método nativo para parar, então dependemos da thread
        logging.info("Servidor sendo parado...")

    def check_server_status(self):
        """Verifica se o servidor está respondendo"""
        try:
            import requests
            response = requests.get("http://localhost:5000/health", timeout=2)
            return response.status_code == 200
        except:
            return False

# Instância global do servidor
ticket_server = TicketServer()

if __name__ == "__main__":
    print("Iniciando servidor de tickets...")
    print("Servidor rodando em: http://localhost:5000")
    print("Pressione Ctrl+C para parar")

    ticket_server.run_server()# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass
