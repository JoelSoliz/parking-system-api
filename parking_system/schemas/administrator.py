from pydantic import BaseModel

from .user import User


class Administrator(User):
    id_administrator: str

    class Config:
        orm_mode = True
