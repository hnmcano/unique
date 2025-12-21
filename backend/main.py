from fastapi import FastAPI
from routers import clientes, produtos, carrinhos, pedidos, caixa
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="My First FastAPI project", version="1.0.0")
origins = [
    "http://localhost:5173",
    "https://catalogo.unqsystems.com.br",           # Seu domínio principal (React)
    "https://backend-fastapi-8gr09ege2-hnmcanos-projects.vercel.app" # URL reserva da Vercel
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


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)