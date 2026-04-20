from PySide6.QtCore import *
from PySide6.QtWidgets import *
import websocket
import json

from config.config import settings
from core.app_context import app_context as APPContext

class WebSocketService(QThread):
    mensagem_recebida = Signal(dict)
    status = Signal(str)

    def __init__(self, token):
        super().__init__()
        self.token = token
        self.status_atual = "desconectado"

        # conecta apenas uma vez
        self.mensagem_recebida.connect(self.processar_evento)

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
                QMessageBox.critical(None, "Erro de Conexão", f"Não foi possível conectar ao servidor: {e}, tentando novamente em 5 segundos...")

    def on_message(self, ws, message: str):
        try:
            evento = json.loads(message) 
            self.mensagem_recebida.emit(evento)
            
        except Exception as e:
            print("WS ERRO:", e)

    def _on_open(self, ws):
        self.ws = ws
        self.status_atual = "conectado"
        self.status.emit("conectado")

    def _on_error(self, ws, error):
        print("WS ERRO:", error)

    def _on_close(self, ws, *args):
        self.status_atual = "desconectado"
        self.status.emit("desconectado")

    def processar_evento(self, evento):
        tipo = evento.get("tipo")
        dados = evento.get("dados")

        if tipo == "pedido_criado":
            APPContext.pedido_store.adicionar(dados)

        elif tipo == "pedido_em_delivery_atualizado":
            APPContext.pedido_store.atualizar(dados)

        elif tipo == "pedido_removido":
            APPContext.pedido_store.remover(dados)

        elif tipo == "horario_criado":
            APPContext.horarios_store.adicionar(dados)

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
        for p in self.pedidos:
            if p["id_pedido"] == pedido["id_pedido"]:
                self.pedidos.remove(p)
                self.pedido_removido.emit(p)
                break

    def atualizar(self, pedido_atualizado):
        print("O sinal esta chegando")
        for i, p in enumerate(self.pedidos):
            if p["id_pedido"] == pedido_atualizado["id_pedido"]:
                self.pedidos[i] = pedido_atualizado
                self.pedido_atualizado.emit(pedido_atualizado)
                break
            
    def listar(self):
        return self.pedidos

    def contar_pendentes(self):
        return sum(1 for p in self.pedidos if p["status"] == "PENDENTE")
    
class HorarioStore(QObject):

    horario_adicionado = Signal(dict)

    def __init__(self):
        super().__init__()
        self.horarios = []

    def adicionar(self, horario):
        self.horarios.append(horario)
        self.horario_adicionado.emit(horario)
    
    def listar(self):
        return self.horarios
    
class ProdutosStore(QObject):
    produtos_atualizados = Signal(dict)
    produto_adicionado = Signal(dict)
    def __init__(self):
        super().__init__()
        self.produtos = []

    def atualizar(self, produtos):
        if isinstance(produtos, dict):
            produtos = [produtos]

        for prod in produtos:
            prod_id = str(prod["id_produto"])  # força padrão

            encontrado = False
            for i, p in enumerate(self.produtos):
                if str(p["id_produto"]) == prod_id:
                    self.produtos[i] = prod
                    encontrado = True
                    break

            if not encontrado:
                self.produtos.append(prod)

        self.produtos_atualizados.emit(self.produtos)

    def adicionar(self, produto):
        self.produtos.append(produto)
        self.produto_adicionado.emit(self.produtos)

    def remover(self, produto):
        for p in self.produtos:
            if p["id_produto"] == produto["id_produto"]:
                self.produtos.remove(p)
                self.produtos_atualizados.emit(self.produtos)
                break

    def listar(self):
        return self.produtos