from pydantic import BaseModel


class CustomerBase(BaseModel):
    email: str

class CreateCustomer(CustomerBase):
    id_assignment: str
    name: str
    last_name: str
    ci: int
    password: str
    phone: str
    address: str

    class Config:
        orm_mode = True

class Customer(CustomerBase):
    id_customer: str
    name: str
    last_name: str
    ci: int
    password: str
    phone: str
    address: str

    class Config:
        orm_mode = True

class CustomerPaginated(BaseModel):
    results: list[Customer]
    current_page: int
    total_pages: int
    total_elements: int
    element_per_page: int

    class Config:
        orm_mode = True
 