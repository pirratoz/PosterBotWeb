from pydantic import BaseModel

from source.dto import T_entities


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


class TemplateCreateRequest(BaseModel):
    title: str
    text: str
    attachments: Attachments
