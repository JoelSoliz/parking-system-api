from datetime import datetime
from pydantic import BaseModel

from .customer import Customer
from .parking_spot import Parking
from .hourly_rate import HourlyRateBase

class PayBase(BaseModel):
    amount: float

    class Config:
        orm_mode = True

class PayDateTime(PayBase):
    payment_datetime: datetime
    
    class Config:
        orm_mode = True

class Pay(PayDateTime):
    id_pay: str

    class Config:
        orm_mode = True

class PayAndReservation(PayBase):
    reservation: str
    
    class Config:
        orm_mode = True

class PayWithCustomer(BaseModel):
    customer: Customer
    pay: Pay
    id_spot: str

    class Config:
        orm_mode = True

class Result(BaseModel):
    results: list[PayWithCustomer]
    current_page: int
    total_pages: int
    total_elements: int
    element_per_page: int

    class Config:
        orm_mode = True

class LatePayment(BaseModel):
    customer: Customer
    spot: Parking
    price: HourlyRateBase

    class Config:
        orm_mode = True

class PaginatedLatePayment(BaseModel):
    results: list[LatePayment]

    class Config:
        orm_mode = True