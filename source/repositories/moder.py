from sqlalchemy import (
    select,
    insert,
    delete,
)

from source.repositories.base_repo import BaseRepository
from source.models import Moder
from source.dto import ModerDto


class ModerRepository(BaseRepository):
    async def get_moder_by_id(self, moder_id: int) -> ModerDto | None:
        stmt = select(Moder).where(Moder.id == moder_id)
        item = (await self.session.execute(stmt)).scalar_one_or_none()
        return ModerDto.one_from_orm(item)

    async def delete_moder_by_id(self, moder_id: int) -> None:
        stmt = delete(Moder).where(Moder.id == moder_id)
        await self.session.execute(stmt)

    async def get_all_moders(self) -> list[ModerDto]:
        stmt = select(Moder)
        items = (await self.session.execute(stmt)).scalars().all()
        return ModerDto.many_from_orm(items)
    
    async def create(self, *, moder_id: int, fullname: str, username: str) -> ModerDto | None:
        stmt = insert(Moder).values(id=moder_id, fullname=fullname, username=username)
        await self.session.execute(stmt)
        return await self.get_moder_by_id(moder_id)
