from pydantic import BaseModel

from .permission import Permission
from .role import Role


class UserBase(BaseModel):
    name: str
    last_name: str
    ci: int
    email: str
    phone: str


class UserLogin(BaseModel):
    email: str
    password: str

    class Config:
        orm_mode = True


class UserCreate(UserBase, UserLogin):
    class Config:
        orm_mode = True


class User(UserBase):
    id_user: str
    role: str
    user_permissions: list[Permission] | None = None
    role_info: Role | None = None

    class Config:
        orm_mode = True


class UserToken(BaseModel):
    access_token: str
    token_type: str
