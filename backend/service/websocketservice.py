from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from jose import jwt, JWTError
from core.config import settings
import json


router = APIRouter()

clientes_conectados: dict[str, list[WebSocket]] = {}

@router.websocket("")
async def websocket_endpoint(websocket: WebSocket, token: str):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        estabelecimento_id = payload.get("estabelecimento_id")

        if not estabelecimento_id:
            await websocket.close(code=1008)
            return

    except JWTError:
        await websocket.close(code=1008)
        return
    

    await websocket.accept()

    if estabelecimento_id not in clientes_conectados:
        clientes_conectados[estabelecimento_id] = []

    clientes_conectados[estabelecimento_id].append(websocket)

    try:
        while True:
            data = await websocket.receive_text()
    except WebSocketDisconnect:
        clientes_conectados[estabelecimento_id].remove(websocket)

async def notificar_todos(estabelecimento_id: str, evento: dict):

    if estabelecimento_id not in clientes_conectados:
        return

    for cliente in clientes_conectados[estabelecimento_id]:
        await cliente.send_text(json.dumps(evento))

        