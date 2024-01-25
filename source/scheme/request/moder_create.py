from pydantic import BaseModel


class ModerCreateRequest(BaseModel):
    id: int
    fullname: str
    username: str
