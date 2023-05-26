from datetime import datetime, time, date
from pydantic import BaseModel

from .customer import Customer
from .parking_spot import ParkingBase

class Reservation(BaseModel):
    id_reservation: str
    start_date: date
    end_date: date
    id_customer: str
    create_at: datetime
    customer: Customer

    class Config:
        orm_mode = True
    

class ReservationCreate(BaseModel):
    start_date: date
    end_date: date
    id_price: str
    id_spot: str 
    day : list[str]
    start_time: list[time]
    end_time: list[time]

    class Config:
        orm_mode = True

class ReservationWithCustomer(BaseModel):
    id_reservation: str
    start_date: date
    end_date: date
    create_at: datetime
    customer:Customer
    
    class Config:
        orm_mode = True

class ReservationWithIdCustomer(BaseModel):
    reservation: ReservationWithCustomer
    id_spot: str
    status: str
    
    class Config:
        orm_mode = True


class ReservationPaginated(BaseModel):
    results: list[ReservationWithIdCustomer]
    current_page: int
    total_pages: int
    total_elements: int
    element_per_page: int

    class Config:
        orm_mode = True
