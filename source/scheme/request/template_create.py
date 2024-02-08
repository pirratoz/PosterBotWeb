from pydantic import BaseModel

from source.dto import T_entities


class Media(BaseModel):
    file_id: str
    type: str
    message_id: int


class Button(BaseModel):
    text: str
    url: str


class TemplateCreateRequest(BaseModel):
    title: str
    text: str
    entities: T_entities
    media: list[Media]
    keyboard: list[list[Button]]
