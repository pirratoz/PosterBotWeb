from sqlalchemy import String
from sqlalchemy.dialects.postgresql import (
    BIGINT,
    JSON,
    ARRAY,
)
from sqlalchemy.orm import (
    mapped_column,
    relationship,
    Mapped,
)

from source.models.base_model import BaseModel
from source.dto import (
    T_keyboard,
    T_entities,
    T_media,
)


class Template(BaseModel):
    __tablename__ = "templates"
    
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    title: Mapped[str] = mapped_column(String)
    
    text: Mapped[str] = mapped_column(String)
    entities: Mapped[T_entities] = mapped_column(ARRAY(JSON))
    media: Mapped[T_media] = mapped_column(ARRAY(JSON))
    keyboard: Mapped[T_keyboard] = mapped_column(ARRAY(JSON, dimensions=2))

    publications = relationship("Publication", backref="templates", cascade="all, delete-orphan")
