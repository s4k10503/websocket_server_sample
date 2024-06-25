from fastapi import WebSocket, Depends
from domain.interfaces import IWebSocketHandler, IWebSocketService
import logging


class WebSocketHandler(IWebSocketHandler):
    def __init__(self, service: IWebSocketService = Depends()):
        self.service = service

    async def websocket_endpoint(self, websocket: WebSocket):
        logging.debug("WebSocket connection request received")
        await websocket.accept()
        try:
            while True:
                data = await websocket.receive_text()
                logging.debug(f"Message received: {data}")
                response = self.service.process_message(data)
                await websocket.send_text(response)
        except Exception as e:
            print(f"WebSocket closed: {e}")
