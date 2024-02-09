from sqlalchemy import (
    select,
    insert,
    delete,
    update,
)

from source.repositories.base_repo import BaseRepository
from source.scheme import TemplateCreateRequest
from source.models import Template
from source.dto import TemplateDto


class TemplateRepository(BaseRepository):
    async def get_template_by_id(self, template_id: int) -> TemplateDto | None:
        stmt = select(Template).where(Template.id == template_id)
        item = (await self.session.execute(stmt)).scalar_one_or_none()
        return TemplateDto.one_from_orm(item)

    async def delete_template_by_id(self, template_id: int) -> None:
        stmt = delete(Template).where(Template.id == template_id)
        await self.session.execute(stmt)

    async def get_all_templates(self) -> list[TemplateDto]:
        stmt = select(Template)
        items = (await self.session.execute(stmt)).scalars().all()
        return TemplateDto.many_from_orm(items)

    async def create(self, *, template: TemplateCreateRequest) -> TemplateDto | None:
        stmt = insert(Template).values(
            **template.model_dump()
        ).returning(Template.id)
        result_id = (await self.session.execute(stmt)).one()[0]
        return await self.get_template_by_id(result_id)

    async def update(self, template_id: int, *, template: TemplateCreateRequest) -> TemplateDto | None:
        stmt = update(Template).where(
            Template.id == template_id
        ).values(
            **template.model_dump()
        )
        await self.session.execute(stmt)
        return await self.get_template_by_id(template_id)
