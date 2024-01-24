from sqlalchemy import (
    BIGINT,
    String,
)
from sqlalchemy.orm import (
    mapped_column,
    relationship,
    Mapped,
)

from source.models.base_model import BaseModel


class Chat(BaseModel):
    __tablename__ = "chats"

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    title: Mapped[str] = mapped_column(String)

    publications = relationship("Publication", backref="chats", cascade="all, delete-orphan")
