from abc import ABC

from sqlalchemy import text
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)

from source.configs import PostgresqlConfig


class DatabaseConnector:
    def __init__(self) -> None:
        self.engine = create_async_engine(url=PostgresqlConfig().URI)
        self.sessionmaker = async_sessionmaker(self.engine, expire_on_commit=False)

    async def get_session(self) -> AsyncSession:
        async with self.sessionmaker() as session:
            yield session
            await session.commit()

    async def get_session_read_only(self) -> AsyncSession:
        async with self.sessionmaker() as session:
            await session.execute(text("SET TRANSACTION READ ONLY"))
            yield session


class Session(ABC):
    ...


class SessionReadOnly(ABC):
    ...
