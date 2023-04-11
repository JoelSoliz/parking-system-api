from pydantic import BaseModel

from .user import User


class Customer(User):
    id_customer: str

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
