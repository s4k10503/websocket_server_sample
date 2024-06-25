from pydantic import BaseModel

class WebSocketMessage(BaseModel):
    content: str
