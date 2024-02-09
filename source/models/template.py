from typing import Any

from sqlalchemy import String
from sqlalchemy.dialects.postgresql import (
    BIGINT,
    JSON,
)
from sqlalchemy.orm import (
    mapped_column,
    relationship,
    Mapped,
)

from source.models.base_model import BaseModel


class Template(BaseModel):
    __tablename__ = "templates"
    
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    title: Mapped[str] = mapped_column(String)
    
    text: Mapped[str] = mapped_column(String)
    attachments: Mapped[dict[str, Any]] = mapped_column(JSON)

    publications = relationship("Publication", backref="templates", cascade="all, delete-orphan")
