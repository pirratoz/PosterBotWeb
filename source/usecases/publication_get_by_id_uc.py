from fastapi import (
    HTTPException,
    status,
)

from source.usecases.base_uc import BaseUseCase
from source.repositories import PublicationRepository
from source.scheme import PublicationResponse


class PublicationGetByIdUseCase(BaseUseCase):
    def __init__(self,
        publication_repo: PublicationRepository
    ) -> None:
        self.publication_repo = publication_repo
    
    async def execute(self, publication_id: int) -> PublicationResponse:
        publication = await self.publication_repo.get_publication_by_id(publication_id)
        
        if not publication:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="publication not found"
            )

        return PublicationResponse(**publication.model_dump())
