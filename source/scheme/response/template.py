from pydantic import BaseModel

from source.dto import T_entities
from source.scheme.request.template_create import (
    Button,
    Media,
)


class TemplateResponse(BaseModel):
    id: int
    title: str
    text: str
    entities: T_entities
    media: list[Media]
    keyboard: list[list[Button]]


class TemplateManyResponse(BaseModel):
    templates: list[TemplateResponse]
