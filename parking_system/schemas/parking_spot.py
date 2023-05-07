from typing import List

from pydantic import BaseModel
from .hourly_rate import HourlyRate
from .business_hours import BussinesHours


class ParkingBase(BaseModel):
    name: str
    section: str
    coordinate: str
    type: str
    
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
