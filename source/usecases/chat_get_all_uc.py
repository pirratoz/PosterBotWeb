from source.usecases.base_uc import BaseUseCase
from source.repositories import ChatRepository
from source.scheme import (
    ChatManyResponse,
    ChatResponse,
)


class ChatGetAllUseCase(BaseUseCase):
    def __init__(self,
        chat_repo: ChatRepository
    ) -> None:
        self.chat_repo = chat_repo
    
    async def execute(self) -> ChatManyResponse:
        chats = await self.chat_repo.get_all_chat()
        return ChatManyResponse(chats=[
            ChatResponse(**chat.model_dump()) for chat in chats
        ])
