from fastapi import FastAPI
from routers import user

app = FastAPI(title="My First FastAPI project", version="1.0.0")

app.include_router(user.router, prefix="/users", tags=["users"])

@app.get("/")
def app_root():
    return {"Bem vindo ao fastApi"}