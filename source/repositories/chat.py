from sqlalchemy import (
    select,
    insert,
    delete,
)

from source.repositories.base_repo import BaseRepository
from source.models import Chat
from source.dto import ChatDto


class ChatRepository(BaseRepository):
    async def get_chat_by_id(self, chat_id: int) -> ChatDto | None:
        stmt = select(Chat).where(Chat.id == chat_id)
        item = (await self.session.execute(stmt)).scalar_one_or_none()
        return ChatDto.one_from_orm(item)

    async def delete_chat_by_id(self, chat_id: int) -> None:
        stmt = delete(Chat).where(Chat.id == chat_id)
        await self.session.execute(stmt)

    async def get_all_chat(self) -> list[ChatDto]:
        stmt = select(Chat)
        items = (await self.session.execute(stmt)).scalars().all()
        return ChatDto.many_from_orm(items)
    
    async def create(self, *, chat_id: int, title: str) -> ChatDto | None:
        stmt = insert(Chat).values(id=chat_id, title=title)
        await self.session.execute(stmt)
        return await self.get_chat_by_id(chat_id)
