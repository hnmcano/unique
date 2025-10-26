from fastapi import FastAPI
from routers import product, users
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="My First FastAPI project", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(product.router, prefix="/products", tags=["products"])