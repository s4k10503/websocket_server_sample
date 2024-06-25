from domain.interfaces import IWebSocketService
from domain.models import WebSocketMessage


class WebSocketService(IWebSocketService):
    def process_message(self, message: str) -> str:
        ws_message = WebSocketMessage(content=message)
        response = f"Received your message: {ws_message.content}"
        return response
