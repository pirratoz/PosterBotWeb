from source.usecases.base_uc import BaseUseCase
from source.repositories import TemplateRepository
from source.scheme import (
    TemplateManyResponse,
    TemplateResponse,
)


class TemplateGetAllUseCase(BaseUseCase):
    def __init__(self,
        template_repo: TemplateRepository
    ) -> None:
        self.template_repo = template_repo
    
    async def execute(self) -> TemplateManyResponse:
        templates = await self.template_repo.get_all_templates()
        return TemplateManyResponse(templates=[
            TemplateResponse(**template.model_dump()) for template in templates
        ])
