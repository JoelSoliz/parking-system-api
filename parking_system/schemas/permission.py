from pydantic import BaseModel


class PermissionBase(BaseModel):
    description: str

    class Config:
        orm_mode = True


class Permission(PermissionBase):
    id_permission: str

    class Config:
        orm_mode = True
