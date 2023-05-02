from pydantic import BaseModel
from .parking_spot import ParkingBase
from .reservation import Reservation

class AssignmentBase(BaseModel):
    status: str

    class Config:
        orm_mode = True

class Assignment(AssignmentBase):
    id_assignment: str

    class Config:
        orm_mode = True

class ReservationWithParkingAndAssignment(Assignment):
    id_spot: str
    id_reservation: str
    id_assignment_rate: str

    class Cofing:
        orm_mode = True

class AssignmentUpdate(AssignmentBase):
    id_spot: str
    id_assignment_rate: str

class ReservationAndParkingSpot(Assignment):
    reservations: Reservation
    parking_spots: ParkingBase

    class Config:
        orm_mode = True
