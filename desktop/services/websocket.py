from PySide6.QtCore import *
import websocket
import json

from config.config import settings

class WebSocketService(QThread):
    mensagem_recebida = Signal(dict)
    status = Signal(str)

    def __init__(self, token):
        super().__init__()
        self.token = token
        self.status_atual = "desconectado"

    def run(self):
        while True:
            try:
                
                url = f"{settings.WS_URL}/ws?token={self.token}"
                self.ws = websocket.WebSocketApp(
                    url,
                    on_message=self.on_message,
                    on_open=self._on_open,
                    on_error=self._on_error,
                    on_close=self._on_close,
                )
                self.ws.run_forever()
            except Exception as e:
                print("Erro ao conectar ao WS:", e)


    def on_message(self, ws, message: str):
        try:
            evento = json.loads(message)
            self.mensagem_recebida.emit(evento)
        except Exception as e:
            print("Erro ao processar WS:", e)
    
    def _on_open(self, ws):
        self.ws = ws
        self.status_atual = "conectado"

        self.status.emit("conectado")
        print("WS CONECTADO")


    def _on_error(self, ws, error):
        print("WS ERRO:", error)

    def _on_close(self, ws, *args):
        self.status_atual = "desconectado"

        self.status.emit("desconectado")
        print("WS FECHADO")

class PedidoStore:
    def __init__(self):
        self.pedidos = []

    def listar(self):
        return self.pedidos

    def adicionar(self, pedido):
        self.pedidos.append(pedido)

    def remover(self, pedido):
        self.pedidos.remove(pedido)