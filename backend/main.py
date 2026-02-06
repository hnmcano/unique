from fastapi import FastAPI
from routers import clientes, produtos, carrinhos, pedidos, caixa, estabelecimento, categorias, mesas
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="My First FastAPI project", version="1.0.0")
origins = [
    "http://localhost:5173",
    "http://localhost:8000",
    "http://127.0.0.1:5173",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
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
