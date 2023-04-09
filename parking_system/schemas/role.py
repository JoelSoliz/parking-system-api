from pydantic import BaseModel


class RoleBase(BaseModel):
    description: str
    class Config:
        orm_mode = True

class RoleCreate(RoleBase):
    id_role: str
    
    class Config:
        orm_mode = True
