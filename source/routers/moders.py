from fastapi.responses import JSONResponse
from fastapi import (
    APIRouter,
    Depends,
    status,
)

from source.repositories import ModerRepository
from source.dependencies import (
    SessionReadOnly,
    Session,
)
from source.scheme import (
    ModerCreateRequest,
    ModerManyResponse,
    ModerResponse,
)
from source.usecases import (
    ModerCreateUseCase,
    ModerDeleteUseCase,
    ModerGetAllUseCase,
    ModerGetByIdUseCase,
)


moders = APIRouter()


@moders.get("/")
async def get_all_moders(session: SessionReadOnly = Depends()) -> ModerManyResponse:
    moders = await ModerGetAllUseCase(
        ModerRepository(session)
    ).execute()
    return JSONResponse(moders.model_dump(), status_code=status.HTTP_200_OK)


@moders.get("/{moder_id}")
async def get_moder(moder_id: int, session: SessionReadOnly = Depends()) -> ModerResponse:
    moder = await ModerGetByIdUseCase(
        ModerRepository(session)
    ).execute(moder_id)
    return JSONResponse(moder.model_dump(), status_code=status.HTTP_200_OK)


@moders.post("/")
async def create_moder(data: ModerCreateRequest, session: Session = Depends()) -> ModerResponse:
    moder = await ModerCreateUseCase(
        ModerRepository(session)
    ).execute(data)
    return JSONResponse(moder.model_dump(), status_code=status.HTTP_201_CREATED)


@moders.delete("/{moder_id}")
async def delete_moder(moder_id: int, session: Session = Depends()) -> ModerResponse:
    moder = await ModerDeleteUseCase(
        ModerRepository(session)
    ).execute(moder_id)
    return JSONResponse(moder.model_dump(), status_code=status.HTTP_200_OK)
