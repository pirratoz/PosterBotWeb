from datetime import datetime

from source.dto.base_dto import BaseModelDto


class PublicationDto(BaseModelDto):
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
