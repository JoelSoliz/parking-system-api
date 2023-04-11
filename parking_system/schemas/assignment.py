from datetime import datetime
from pydantic import BaseModel


class AssignmentBase(BaseModel):
    assignment_date: datetime

    class Config:
        orm_mode = True


class AssignmentCreate(AssignmentBase):
    id_assignment: str

    class Config:
        orm_mode = True


class AssignmentWithRole(AssignmentBase):
    id_role: str
