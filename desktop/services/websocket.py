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

class PedidoStore(QObject):
    pedido_adicionado = Signal(dict)
    pedido_removido = Signal(dict)
    pedido_atualizado = Signal(dict)

    def __init__(self):
        super().__init__()
        self.pedidos = []

    def adicionar(self, pedido):
        self.pedidos.append(pedido)
        self.pedido_adicionado.emit(pedido)

    def remover(self, pedido):
        if pedido in self.pedidos:
            self.pedidos.remove(pedido)
            self.pedido_removido.emit(pedido)

    def atualizar(self, pedido_atualizado):
        for i, p in enumerate(self.pedidos):
            if p["id"] == pedido_atualizado["id"]:
                self.pedidos[i] = pedido_atualizado
                self.pedido_atualizado.emit(pedido_atualizado)
                break

    def listar(self):
        return self.pedidos

    def contar_pendentes(self):
        return sum(1 for p in self.pedidos if p["status"] == "PENDENTE")