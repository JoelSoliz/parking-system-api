from datetime import datetime
from pydantic import BaseModel

from .user import User, UserCreate


class EmployeeBase(BaseModel):
    hire_date: datetime
    salary: float


class CreateEmployee(UserCreate, EmployeeBase):
    class Config:
        orm_mode = True


class Employee(User, EmployeeBase):
    id_employee: str
    registered_by: str

    class Config:
        orm_mode = True


class EmployeePaginated(BaseModel):
    results: list[Employee]
    current_page: int
    total_pages: int
    total_elements: int
    element_per_page: int

    class Config:
        orm_mode = True
