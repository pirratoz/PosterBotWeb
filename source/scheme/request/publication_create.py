from datetime import datetime

from pydantic import (
    BaseModel,
    validator,
)


class PublicationCreateRequest(BaseModel):
    template_id: int
    
    publish: datetime
    finish: datetime

    chat_id: int
    message_id: int | None
    
    pin: bool = False
    delete: bool = False

    published: bool = False
    deleted: bool = False

    pinned: bool = False
    archived: bool = False

    @validator("publish", "finish")
    def date_validator(cls, value: datetime) -> datetime:
        return value.replace(tzinfo=None)
