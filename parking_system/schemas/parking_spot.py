from datetime import date, time

from pydantic import BaseModel

from .business_hours import BussinesHours


class ParkingBase(BaseModel):
    name: str
    section: str
    coordinate: str
    type_spot: str
    
    class Config:
        orm_mode = True
    

class Parking(ParkingBase):
    id_spot: str

    class Config():
        orm_mode = True

class ParkingRegister(Parking):
    id_hours: str

    class Config:
        orm_mode = True
        

class ShowParking(ParkingBase):

    business_hours: BussinesHours
    # assignment_rate: AssignmentBase

    class Config:
        orm_mode = True

class ReservationDates(BaseModel):
    start_date: date
    end_date: date

    class Config:
        orm_mode = True

class Days(BaseModel):
    day: str
    start_time: time
    end_time: time

    class Config:
        orm_mode = True

class Reservations(BaseModel):
    reservation: ReservationDates
    days: list[Days]

    class Config:
        orm_mode = True

class ParkingDate(BaseModel):
    parking: ParkingBase
    reservations: list[Reservations]
    

    class Config:
        orm_mode = True
