from datetime import datetime, time, date
from pydantic import BaseModel

from .customer import Customer
from .parking_spot import ParkingBase

class Reservation(BaseModel):
    id_reservation: str
    start_date: datetime
    end_date: datetime
    status: bool
    id_customer: str
    id_spot: str
    customer: Customer

    class Config:
        orm_mode = True


class ShowReservation(Reservation):
    parking_spot: ParkingBase

    class Config:
        orm_mode = True
    

class ReservationCreate(BaseModel):
    start_date: date
    end_date: date
    id_spot: str
    day : list[str]
    start_time: list[time]
    end_time: list[time]

    class Config:
        orm_mode = True
    

class ReservationPaginated(BaseModel):
    results: list[Reservation]
    current_page: int
    total_pages: int
    total_elements: int
    element_per_page: int

    class Config:
        orm_mode = True
