from datetime import datetime

from sqlalchemy import (
    BIGINT,
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import (
    mapped_column,
    Mapped,
)

from source.models.base_model import BaseModel


class Publication(BaseModel):
    __tablename__ = "publications"

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    template_id: Mapped[int] = mapped_column(BIGINT, ForeignKey("templates.id"))

    publish: Mapped[datetime] = mapped_column(DateTime)
    finish: Mapped[datetime] = mapped_column(DateTime)

    chat_id: Mapped[int] = mapped_column(BIGINT, ForeignKey("chats.id"))
    message_id: Mapped[int | None] = mapped_column(default=None, nullable=True)

    pin: Mapped[bool] = mapped_column(default=False)
    delete: Mapped[bool] = mapped_column(default=False)

    published: Mapped[bool] = mapped_column(default=False)
    deleted: Mapped[bool] = mapped_column(default=False)
    pinned: Mapped[bool] = mapped_column(default=False)
    archived: Mapped[bool] = mapped_column(default=False)
