from fastapi import FastAPI
from service import websocketservice
from routers import clientes, produtos, carrinhos, pedidos, caixa, estabelecimento, categorias, mesas, usuarios, impressoras, update
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="UniqueSystems - PDV", version="1.0.0")

Instrumentator().instrument(app).expose(app)

origins = [
    "http://hookahshisha.localhost:5173",
    "http://boahora.localhost:5173",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_origin_regex=r"https://.*\.uniqsystems\.com\.br",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(clientes.router, prefix="/clientes", tags=["clientes"])
app.include_router(produtos.router, prefix="/produtos", tags=["produtos"])
app.include_router(carrinhos.router, prefix="/carrinho", tags=["carrinho"])
app.include_router(pedidos.router, prefix="/pedidos", tags=["pedidos"])
app.include_router(caixa.router, prefix="/caixa", tags=["caixa"])
app.include_router(estabelecimento.router, prefix="/estabelecimento", tags=["estabelecimento"])
app.include_router(categorias.router, prefix="/categorias", tags=["categorias"])
app.include_router(mesas.router, prefix="/mesas", tags=["mesas"])
app.include_router(websocketservice.router, prefix="/ws", tags=["websocket"])
app.include_router(usuarios.router, prefix="/usuarios", tags=["usuarios"])
app.include_router(impressoras.router, prefix="/impressoras", tags=["impressoras"])
app.include_router(update.router, prefix="/update", tags=["update"])
