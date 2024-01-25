from fastapi import (
    HTTPException,
    status,
)

from source.usecases.base_uc import BaseUseCase
from source.repositories import ChatRepository
from source.scheme import (
    ChatResponse,
    ChatCreateRequest,
)


class ChatCreateUseCase(BaseUseCase):
    def __init__(self,
        chat_repo: ChatRepository
    ) -> None:
        self.chat_repo = chat_repo
    
    async def execute(self, info: ChatCreateRequest) -> ChatResponse:
        chat = await self.chat_repo.get_chat_by_id(info.id)
        
        if chat:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="chat already exists"
            )
        
        chat = await self.chat_repo.create(
            chat_id=info.id,
            title=info.title
        )

        return ChatResponse(**chat.model_dump())
