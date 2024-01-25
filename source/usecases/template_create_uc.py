from source.usecases.base_uc import BaseUseCase
from source.repositories import TemplateRepository
from source.scheme import (
    TemplateResponse,
    TemplateCreateRequest,
)


class TemplateCreateUseCase(BaseUseCase):
    def __init__(self,
        template_repo: TemplateRepository
    ) -> None:
        self.template_repo = template_repo
    
    async def execute(self, info: TemplateCreateRequest) -> TemplateResponse:        
        template = await self.template_repo.create(template=info)
        return TemplateResponse(**template.model_dump())
