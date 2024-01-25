from pydantic import BaseModel


class ChatCreateRequest(BaseModel):
    id: int
    title: str
