from typing import (
    TypeVar,
    Any,
)

from pydantic import BaseModel

from source.dto.base_dto import BaseModelDto


T_entities = TypeVar("T_entities", bound=list[dict[str, Any]])
T_media = TypeVar("T_media", bound=list[dict[str, Any]])
T_keyboard = TypeVar("T_keyboard", bound=list[list[dict[str, Any]]])


class Media(BaseModel):
    file_id: str
    type: str
    message_id: int


class Button(BaseModel):
    text: str
    url: str


class Attachments(BaseModel):
    entities: T_entities | None = []
    media: list[Media] | None = []
    keyboard: list[list[Button]] | None = []


class TemplateDto(BaseModelDto):
    id: int
    title: str
    text: str
    attachments: Attachments
