import pytest
from application.websocket_service import WebSocketService
from domain.models import WebSocketMessage


@pytest.mark.asyncio
async def test_websocket_service():
    service = WebSocketService()
    message = "Hello, WebSocket!"
    response = service.process_message(message)
    expected_response = WebSocketMessage(content=message)
    assert response == f"Received your message: {expected_response.content}"

def test_websocket_service_invalid_message():
    service = WebSocketService()
    invalid_message = 12345  # Invalid message type
    try:
        response = service.process_message(invalid_message)
    except Exception as e:
        assert isinstance(e, TypeError)  # Expecting a TypeError because the input is not a string
