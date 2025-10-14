from fastapi import FastAPI
from routers import product, users

app = FastAPI(title="My First FastAPI project", version="1.0.0")

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(product.router, prefix="/products", tags=["products"])

