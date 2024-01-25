from fastapi import (
    HTTPException,
    status,
)

from source.usecases.base_uc import BaseUseCase
from source.repositories import ModerRepository
from source.scheme import (
    ModerResponse,
    ModerCreateRequest,
)


class ModerCreateUseCase(BaseUseCase):
    def __init__(self,
        moder_repo: ModerRepository
    ) -> None:
        self.moder_repo = moder_repo
    
    async def execute(self, info: ModerCreateRequest) -> ModerResponse:
        moder = await self.moder_repo.get_moder_by_id(info.id)
        
        if moder:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="moder already exists"
            )
        
        moder = await self.moder_repo.create(
            moder_id=info.id,
            fullname=info.fullname,
            username=info.username
        )

        return ModerResponse(**moder.model_dump())
