from pydantic import BaseModel

from .permission import Permission


class RoleBase(BaseModel):
    description: str

    class Config:
        orm_mode = True


class Role(RoleBase):
    id_role: str
    role_permissions: list[Permission]

    class Config:
        orm_mode = True
