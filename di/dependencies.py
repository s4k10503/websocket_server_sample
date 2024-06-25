from fastapi import FastAPI
from domain.interfaces import IWebSocketService, IWebSocketHandler
from application.websocket_service import WebSocketService
from presentation.websocket_handler import WebSocketHandler


def setup_dependencies(app: FastAPI):
    @app.on_event("startup")
    async def startup_event():
        app.dependency_overrides[IWebSocketService] = WebSocketService
        app.dependency_overrides[IWebSocketHandler] = WebSocketHandler
