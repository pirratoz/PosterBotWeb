from source.usecases.base_uc import BaseUseCase
from source.repositories import ModerRepository
from source.scheme import (
    ModerManyResponse,
    ModerResponse,
)


class ModerGetAllUseCase(BaseUseCase):
    def __init__(self,
        moder_repo: ModerRepository
    ) -> None:
        self.moder_repo = moder_repo
    
    async def execute(self) -> ModerManyResponse:
        moders = await self.moder_repo.get_all_moders()
        return ModerManyResponse(moders=[
            ModerResponse(**moder.model_dump()) for moder in moders
        ])
