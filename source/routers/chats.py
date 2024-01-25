from fastapi.responses import JSONResponse
from fastapi import (
    APIRouter,
    Depends,
    status,
)

from source.repositories import ChatRepository
from source.usecases import (
    ChatCreateUseCase,
    ChatGetByIdUseCase,
    ChatDeleteUseCase,
    ChatGetAllUseCase,
)
from source.dependencies import (
    SessionReadOnly,
    Session,
)
from source.scheme import (
    ChatCreateRequest,
    ChatManyResponse,
    ChatResponse,
)


chats = APIRouter()


@chats.get("/{chat_id}")
async def get_chat(chat_id: int, session: SessionReadOnly = Depends()) -> ChatResponse:
    chat = await ChatGetByIdUseCase(
        ChatRepository(session)
    ).execute(chat_id)
    return JSONResponse(chat.model_dump(), status_code=status.HTTP_200_OK)


@chats.get("/")
async def get_all_chats(session: SessionReadOnly = Depends()) -> ChatManyResponse:
    chats = await ChatGetAllUseCase(
        ChatRepository(session)
    ).execute()
    return JSONResponse(chats.model_dump(), status_code=status.HTTP_200_OK)


@chats.post("/")
async def create_chat(data: ChatCreateRequest, session: Session = Depends()) -> ChatResponse:
    chat = await ChatCreateUseCase(
        ChatRepository(session)
    ).execute(data)
    return JSONResponse(chat.model_dump(), status_code=status.HTTP_201_CREATED)


@chats.delete("/{chat_id}")
async def delete_chat(chat_id: int, session: Session = Depends()) -> ChatResponse:
    content = await ChatDeleteUseCase(
        ChatRepository(session)
    ).execute(chat_id)
    return JSONResponse(content.model_dump(), status_code=status.HTTP_200_OK)
