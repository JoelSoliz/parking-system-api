from datetime import datetime

from pydantic import BaseModel

from .customer import Customer

class ClaimBase(BaseModel):
    subject: str
    description: str
    request: str
    registration_date: datetime
    
    class Config:
        orm_mode = True

class ClaimDate(ClaimBase):
    registration_date: datetime

class Claim(ClaimDate):
    id_claim: str

class Claims(BaseModel):
    registration_date: datetime
    subject: str

    class Config:
        orm_mode = True

class ClaimWithCustomer(BaseModel):
    customer: Customer
    claim: ClaimBase
    
    class Config:
        orm_mode = True

class ClaimPaginated(BaseModel):
    result: list[ClaimWithCustomer]
    current_page: int
    total_pages: int
    total_elements: int
    element_per_page: int

    class Config:
        orm_mode = True