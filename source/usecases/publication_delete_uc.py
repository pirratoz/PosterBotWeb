from fastapi import (
    HTTPException,
    status,
)

from source.usecases.base_uc import BaseUseCase
from source.repositories import PublicationRepository
from source.scheme import PublicationResponse


class PublicationDeleteUseCase(BaseUseCase):
    def __init__(self,
        publication_repo: PublicationRepository
    ) -> None:
        self.publication_repo = publication_repo

    async def execute(self, publication_id: int) -> PublicationResponse:
        template = await self.publication_repo.get_publication_by_id(publication_id)

        if not template:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="publication not found"
            )

        await self.publication_repo.delete_publication_by_id(publication_id)

        return PublicationResponse(**template.model_dump())
