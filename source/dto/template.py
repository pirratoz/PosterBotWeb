from typing import Any

from source.dto.base_dto import BaseModelDto


class TemplateDto(BaseModelDto):
    id: int
    from_chat_id: int
    media: dict[str, Any]
