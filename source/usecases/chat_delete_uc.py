from fastapi import (
    HTTPException,
    status,
)

from source.usecases.base_uc import BaseUseCase
from source.repositories import ChatRepository
from source.scheme import ChatResponse


class ChatDeleteUseCase(BaseUseCase):
    def __init__(self,
        chat_repo: ChatRepository
    ) -> None:
        self.chat_repo = chat_repo

    async def execute(self, chat_id: int) -> ChatResponse:
        chat = await self.chat_repo.get_chat_by_id(chat_id)

        if not chat:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="chat not found"
            )

        await self.chat_repo.delete_chat_by_id(chat_id)

        return ChatResponse(**chat.model_dump())
