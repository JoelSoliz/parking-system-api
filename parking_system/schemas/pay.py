from datetime import datetime
from pydantic import BaseModel

from .customer import Customer
from .parking_spot import Parking

class PayBase(BaseModel):
    amount: float

    class Config:
        orm_mode = True

class PayDateTime(PayBase):
    payment_datetime = datetime
    
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

