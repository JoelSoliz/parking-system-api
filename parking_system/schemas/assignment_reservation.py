from typing import Optional
from datetime import date, datetime, time

from pydantic import BaseModel
from .parking_spot import Parking
from .reservation import Reservation as Reserva
from .customer import Customer

class AssignmentBase(BaseModel):
    status: str

    class Config:
        orm_mode = True

class Assignment(AssignmentBase):
    id_assignment: str

    class Config:
        orm_mode = True

class ReservationBase(BaseModel):
    start_date: date
    end_date: date
    id_spot: str
    customer: Customer
    create_at: datetime


class Days(BaseModel):
    day: Optional[str] = None
    start_time: Optional[time] = None
    end_time: Optional[time] = None

    class Config:
        orm_mode = True


class ReservationWithParkingAndAssignment(Assignment):
    id_spot: str
    id_reservation: str
    id_assignment_rate: str

    class Config:
        orm_mode = True


class AssignmentUpdate(AssignmentBase):
    id_spot: str
    id_assignment_rate: str


class ReservationAndParkingSpot(BaseModel):
    reservations: Reserva
    parkings_spots: Parking
    status: str
    assisted_by: Optional[str] = None
    days: list[Days]

    class Config:
        orm_mode = True

class DaysAndDate(BaseModel):
    week_days: list[Days]
    
    class Config:
        orm_mode = True