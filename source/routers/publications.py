from fastapi.responses import JSONResponse
from fastapi import (
    APIRouter,
    Depends,
    status,
)

from source.repositories import PublicationRepository
from source.dependencies import (
    SessionReadOnly,
    Session,
)
from source.scheme import (
    PublicationCreateRequest,
    PublicationManyResponse,
    PublicationResponse,
)
from source.usecases import (
    PublicationGetAllActiveUseCase,
    PublicationGetForChatUseCase,
    PublicationGetByIdUseCase,
    PublicationCreateUseCase,
    PublicationDeleteUseCase,
)


publications = APIRouter()


@publications.get("/")
async def get_all_active_publications(session: SessionReadOnly = Depends()) -> PublicationManyResponse:
    publications = await PublicationGetAllActiveUseCase(
        PublicationRepository(session)
    ).execute()
    return JSONResponse(publications.model_dump(), status_code=status.HTTP_200_OK)


@publications.get("/{chat_id}")
async def get_all_publications_for_chat(chat_id: int, session: SessionReadOnly = Depends()) -> PublicationManyResponse:
    publications = await PublicationGetForChatUseCase(
        PublicationRepository(session)
    ).execute(chat_id)
    return JSONResponse(publications.model_dump(), status_code=status.HTTP_200_OK)


@publications.get("/{publication_id}")
async def get_publication(publication_id: int, session: SessionReadOnly = Depends()) -> PublicationResponse:
    publication = await PublicationGetByIdUseCase(
        PublicationRepository(session)
    ).execute(publication_id)
    return JSONResponse(publication.model_dump(), status_code=status.HTTP_200_OK)


@publications.post("/")
async def create_publication(data: PublicationCreateRequest, session: Session = Depends()) -> PublicationResponse:
    publication = await PublicationCreateUseCase(
        PublicationRepository(session)
    ).execute(data)
    return JSONResponse(publication.model_dump(), status_code=status.HTTP_201_CREATED)


@publications.delete("/{publication_id}")
async def delete_publication(publication_id: int, session: Session = Depends()) -> PublicationResponse:
    publication = await PublicationDeleteUseCase(
        PublicationRepository(session)
    ).execute(publication_id)
    return JSONResponse(publication.model_dump(), status_code=status.HTTP_200_OK)
