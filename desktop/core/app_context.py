class AppContext:
    def __init__(self):
        self.token = None
        self.api_client = None
        self.websocket_client = None
        self.pedido_store = None
        self.impressora_store = None
        self.horarios_store = None

app_context = AppContext()