from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from jose import jwt, JWTError
from core.config import settings
from typing import Dict, List
import json

from uuid import UUID

router = APIRouter()

# estabelecimento_id -> lista de conexões
clientes_conectados: Dict[str, List[WebSocket]] = {}


def estabelecimento_esta_online(estabelecimento_id: str) -> bool:
    return (estabelecimento_id in clientes_conectados and len(clientes_conectados[estabelecimento_id]) > 0)

    
@router.websocket("")
async def websocket_endpoint(websocket: WebSocket, token: str):

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        estabelecimento_id = str(payload.get("estabelecimento_id"))

        if not estabelecimento_id:
            await websocket.close(code=1008)
            return

    except JWTError:
        await websocket.close(code=1008)
        return

    await websocket.accept()

    # adiciona conexão
    if estabelecimento_id not in clientes_conectados:
        clientes_conectados[estabelecimento_id] = []

    clientes_conectados[estabelecimento_id].append(websocket)

    try:
        while True:
            await websocket.receive_text()

    except WebSocketDisconnect:

        # remove conexão
        if estabelecimento_id in clientes_conectados:
            if websocket in clientes_conectados[estabelecimento_id]:
                clientes_conectados[estabelecimento_id].remove(websocket)

            # se não houver mais conexões, remove chave
            if len(clientes_conectados[estabelecimento_id]) == 0:
                del clientes_conectados[estabelecimento_id]


async def notificar_todos(estabelecimento_id: str, evento: dict):

    if estabelecimento_id not in clientes_conectados:
        return

    conexoes_ativas = clientes_conectados.get(estabelecimento_id, [])
    conexoes_para_remover = []

    for cliente in conexoes_ativas:
        try:
            await cliente.send_text(json.dumps(evento))
        except Exception:
            conexoes_para_remover.append(cliente)

    # Remove conexões quebradas
    for cliente in conexoes_para_remover:
        conexoes_ativas.remove(cliente)

    # Se não sobrar nenhuma conexão, remove o estabelecimento
    if len(conexoes_ativas) == 0:
        del clientes_conectados[estabelecimento_id]
        