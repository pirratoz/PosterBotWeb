from pydantic import BaseModel


class ChatDeletedResponse(BaseModel):
    id: int
    title: str
