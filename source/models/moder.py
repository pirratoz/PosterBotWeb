from sqlalchemy import (
    BIGINT,
    String,
)
from sqlalchemy.orm import (
    mapped_column,
    Mapped,
)

from source.models.base_model import BaseModel


class Moder(BaseModel):
    __tablename__ = "moders"

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    fullname: Mapped[str] = mapped_column(String)
    username: Mapped[str] = mapped_column(String)
