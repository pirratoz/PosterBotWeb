from fastapi import (
    HTTPException,
    status,
)

from source.usecases.base_uc import BaseUseCase
from source.repositories import ModerRepository
from source.scheme import ModerResponse


class ModerGetByIdUseCase(BaseUseCase):
    def __init__(self,
        moder_repo: ModerRepository
    ) -> None:
        self.moder_repo = moder_repo
    
    async def execute(self, moder_id: int) -> ModerResponse:
        moder = await self.moder_repo.get_moder_by_id(moder_id)
        
        if not moder:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="moder not found"
            )

        return ModerResponse(**moder.model_dump())
