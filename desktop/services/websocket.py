from PySide6.QtCore import *
import websocket
import json



class WebSocketService(QThread):
    mensagem_recebida = Signal(dict)

    def run(self):
        print("Conectando ao WS...")
        self.ws = websocket.WebSocketApp(
            "ws://localhost:8000/ws",
            on_message=self.on_message,
            on_open=self._on_open,
            on_error=self._on_error,
            on_close=self._on_close,
        )
        self.ws.run_forever()

    def on_message(self, ws, message: str):
        try:
            evento = json.loads(message)
            print("Evento recebido:", evento)
            self.mensagem_recebida.emit(evento)
        except Exception as e:
            print("Erro ao processar WS:", e)
    
    def _on_open(self, ws):
        print("WS CONECTADO")

    def _on_error(self, ws, error):
        print("WS ERRO:", error)

    def _on_close(self, ws, *args):
        print("WS FECHADO")