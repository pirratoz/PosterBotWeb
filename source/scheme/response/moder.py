from pydantic import BaseModel


class ModerResponse(BaseModel):
    id: int
    fullname: str
    username: str


class ModerManyResponse(BaseModel):
    moders: list[ModerResponse]
