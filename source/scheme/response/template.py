from pydantic import BaseModel

from source.scheme.request.template_create import Media


class TemplateResponse(BaseModel):
    id: int
    title: str
    from_chat_id: int
    media: Media


class TemplateManyResponse(BaseModel):
    templates: list[TemplateResponse]
