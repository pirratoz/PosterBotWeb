from typing import Any

from pydantic import BaseModel

from source.dto.base_dto import BaseModelDto


class MediaIds(BaseModel):
    photo: list[int] | None = []
    video: list[int] | None = []


class Media(BaseModel):
    text_message_id: int
    media_ids: MediaIds
    keyboard: list[list[dict[str, Any]]] | None = []


class TemplateDto(BaseModelDto):
    id: int
    title: str
    from_chat_id: int
    media: Media
