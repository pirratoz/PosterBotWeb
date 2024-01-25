from pydantic import BaseModel


class ModerResponse(BaseModel):
    id: int
    title: str


class ModerManyResponse(BaseModel):
    moders: list[ModerResponse]
