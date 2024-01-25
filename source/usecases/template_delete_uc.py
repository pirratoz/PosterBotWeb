from fastapi import (
    HTTPException,
    status,
)

from source.usecases.base_uc import BaseUseCase
from source.repositories import TemplateRepository
from source.scheme import TemplateResponse


class TemplateDeleteUseCase(BaseUseCase):
    def __init__(self,
        template_repo: TemplateRepository
    ) -> None:
        self.template_repo = template_repo

    async def execute(self, template_id: int) -> TemplateResponse:
        template = await self.template_repo.get_template_by_id(template_id)

        if not template:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="template not found"
            )

        await self.template_repo.delete_template_by_id(template_id)

        return TemplateResponse(**template.model_dump())
