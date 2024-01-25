from datetime import datetime

from pydantic import (
    BaseModel,
    validator,
)


class PublicationResponse(BaseModel):
    id: int
    template_id: int

    publish: datetime
    finish: datetime

    chat_id: int
    message_id: int | None

    pin: bool
    delete: bool

    published: bool
    deleted: bool
    pinned: bool
    archived: bool
    
    @validator("publish", "finish")
    def date_validator(cls, value: datetime) -> str:
        return str(value.replace(tzinfo=None))


class PublicationManyResponse(BaseModel):
    publications: list[PublicationResponse]
