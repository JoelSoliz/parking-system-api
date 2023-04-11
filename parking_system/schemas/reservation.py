from datetime import datetime, time
from pydantic import BaseModel


class Reservation(BaseModel):
    id_reservation: str
    start_date: datetime
    end_date: datetime
    start_time: time
    end_time: time
    use_duration: str
    id_customer: str
    id_spot: str

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
