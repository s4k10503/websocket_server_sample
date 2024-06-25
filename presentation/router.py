from fastapi import APIRouter, WebSocket, Depends
from domain.interfaces import IWebSocketHandler

router = APIRouter()


@router.websocket("/ws")
async def websocket_route(websocket: WebSocket, handler: IWebSocketHandler = Depends()):
    await handler.websocket_endpoint(websocket)
