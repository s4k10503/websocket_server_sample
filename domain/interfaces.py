from fastapi import WebSocket
from abc import ABC, abstractmethod


class IWebSocketService(ABC):
    @abstractmethod
    def process_message(self, message: str) -> str:
        pass


class IWebSocketHandler(ABC):
    @abstractmethod
    async def websocket_endpoint(self, websocket: WebSocket):
        pass