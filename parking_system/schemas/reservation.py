from typing import Optional
from datetime import datetime, time
from pydantic import BaseModel

from .customer import Customer


class Reservation(BaseModel):
    id_reservation: str
    start_date: datetime
    end_date: datetime
    start_time: time
    end_time: time
    status: bool
    id_customer: str
    id_spot: str
    customer: Customer

    class Config:
        orm_mode = True

class ReservationCreate(BaseModel):
    start_date: datetime
    end_date: datetime
    start_time: time
    end_time: time
    id_spot: str

class ReservationPaginated(BaseModel):
    results: list[Reservation]
    current_page: int
    total_pages: int
    total_elements: int
    element_per_page: int

    class Config:
        orm_mode = True
