from source.usecases.base_uc import BaseUseCase
from source.repositories import PublicationRepository
from source.scheme import (
    PublicationResponse,
    PublicationCreateRequest,
)


class PublicationCreateUseCase(BaseUseCase):
    def __init__(self,
        publication_repo: PublicationRepository
    ) -> None:
        self.publication_repo = publication_repo
    
    async def execute(self, info: PublicationCreateRequest) -> PublicationResponse:
        publication = await self.publication_repo.create(publication=info)
        return PublicationResponse(**publication.model_dump())
