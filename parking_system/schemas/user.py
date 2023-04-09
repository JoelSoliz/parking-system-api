from pydantic import BaseModel


class UserBase(BaseModel):
    email: str

class UserLogin(UserBase):
    password: str
    class Config:
        orm_mode = True

class User(UserBase):
    id_user: str
    name: str
    last_name: str

    class Config:
        orm_mode = True

class UserToken(BaseModel):
    access_token: str
    token_type: str
    