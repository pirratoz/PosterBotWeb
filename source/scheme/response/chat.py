from pydantic import BaseModel


class ChatResponse(BaseModel):
    id: int
    title: str


class ChatManyResponse(BaseModel):
    chats: list[ChatResponse]
