from datetime import datetime
from pydantic import BaseModel


class EmployeeBase(BaseModel):
    email: str

class CreateEmployee(EmployeeBase):
    id_assignment: str
    name: str
    last_name: str
    ci: int
    password: str
    phone: str
    hire_date: datetime
    salary: float

    class Config:
        orm_mode = True

class Employee(EmployeeBase):
    id_employee: str
    name: str
    last_name: str
    ci: int
    password: str
    phone: str
    hire_date: datetime
    salary: float

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