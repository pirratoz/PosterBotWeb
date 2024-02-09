from pydantic import BaseModel

from source.dto import T_entities
from source.scheme.request.template_create import (
    Button,
    Media,
)


class Attachments(BaseModel):
    entities: T_entities | None = []
    media: list[Media] | None = []
    keyboard: list[list[Button]] | None = []


class TemplateResponse(BaseModel):
    id: int
    title: str
    text: str
    attachments: Attachments


class TemplateManyResponse(BaseModel):
    templates: list[TemplateResponse]
