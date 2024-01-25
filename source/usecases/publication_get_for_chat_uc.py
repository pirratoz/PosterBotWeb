from source.usecases.base_uc import BaseUseCase
from source.repositories import PublicationRepository
from source.scheme import (
    PublicationManyResponse,
    PublicationResponse,
)


class PublicationGetForChatUseCase(BaseUseCase):
    def __init__(self,
        publication_repo: PublicationRepository
    ) -> None:
        self.publication_repo = publication_repo
    
    async def execute(self, chat_id: int) -> PublicationManyResponse:
        publications = await self.publication_repo.get_all_publications_for_chat(chat_id)
        return PublicationManyResponse(publications=[
            PublicationResponse(**publication.model_dump()) for publication in publications
        ])
