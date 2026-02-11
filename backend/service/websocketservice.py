from fastapi import APIRouter, WebSocket, WebSocketDisconnect, status
import json


router = APIRouter()

clientes_conectados: list[WebSocket] = []

@router.websocket("")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clientes_conectados.append(websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        clientes_conectados.remove(websocket)

async def notificar_todos(evento: dict):
    for ws in clientes_conectados:
        await ws.send_text(json.dumps(evento))
        