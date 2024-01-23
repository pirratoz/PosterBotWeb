from pydantic_settings import SettingsConfigDict
from pydantic import PostgresDsn

from source.configs.base_config import BaseConfig


class PostgresqlConfig(BaseConfig):
    model_config = SettingsConfigDict(
        env_prefix="PG_"
    )

    HOST: str
    PORT: int
    USER: str
    PASS: str
    NAME: str

    @property
    def DSN(self) -> str:
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            host=self.HOST,
            port=self.PORT,
            username=self.USER,
            password=self.PASS,
            path=self.NAME
        ).unicode_string()
