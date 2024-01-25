from datetime import datetime

from sqlalchemy import (
    select,
    insert,
    delete,
)

from source.repositories.base_repo import BaseRepository
from source.scheme import PublicationCreateRequest
from source.models import Publication
from source.dto import PublicationDto


class PublicationRepository(BaseRepository):
    async def get_publication_by_id(self, publication_id: int) -> PublicationDto | None:
        stmt = select(Publication).where(Publication.id == publication_id)
        item = (await self.session.execute(stmt)).scalar_one_or_none()
        return PublicationDto.one_from_orm(item)

    async def delete_publication_by_id(self, template_id: int) -> None:
        stmt = delete(Publication).where(Publication.id == template_id)
        await self.session.execute(stmt)

    async def get_all_publications(self) -> list[PublicationDto]:
        stmt = select(Publication)
        items = (await self.session.execute(stmt)).scalars().all()
        return PublicationDto.many_from_orm(items)

    async def get_all_publications_active(self) -> list[PublicationDto]:
        stmt = select(Publication).where(Publication.archived == False)
        items = (await self.session.execute(stmt)).scalars().all()
        return PublicationDto.many_from_orm(items)

    async def get_all_publications_for_chat(self, chat_id: int) -> list[PublicationDto]:
        stmt = select(Publication).where(Publication.chat_id == chat_id)
        items = (await self.session.execute(stmt)).scalars().all()
        return PublicationDto.many_from_orm(items)

    async def get_publication_by_created_time(self, date: datetime) -> PublicationDto | None:
        stmt = select(Publication).where(Publication.created_at == date)
        item = (await self.session.execute(stmt)).scalar_one_or_none()
        return PublicationDto.one_from_orm(item)

    async def create(self, *, publication: PublicationCreateRequest) -> PublicationDto | None:
        stmt = insert(Publication).values(
            template_id=publication.template_id,
            publish=publication.publish,
            finish=publication.finish,
            chat_id=publication.chat_id,
            message_id=publication.message_id,
            pin=publication.pin,
            delete=publication.delete,
            published=publication.published,
            deleted=publication.deleted,
            pinned=publication.pinned,
            archived=publication.archived,
            created_at=publication.created_at
        ).returning(Publication.id)
        result_id = (await self.session.execute(stmt)).one()[0]
        return await self.get_publication_by_id(result_id)
