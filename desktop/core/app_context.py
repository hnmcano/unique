

class AppContext:
    def __init__(self):
        self.token = None
        self.api_client = None
        self.websocket_client = None

app_context = AppContext()