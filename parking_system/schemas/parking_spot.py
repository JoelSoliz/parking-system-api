from typing import List

from pydantic import BaseModel
from .hourly_rate import HourlyRate
from .business_hours import BussinesHours 


class ParkingBase(BaseModel):
    name: str
    status: bool
    section: str
    coordinate: str
    
    class Config:
        orm_mode = True
    

class Parking(ParkingBase):
    id_spot: str

    class Config():
        orm_mode = True

class ParkingRegister(Parking):
    price: str
    id_hours: str

    class Config:
        orm_mode = True
        

class ShowParking(Parking):
    hourly_rate: HourlyRate
    business_hours: BussinesHours

    class Config:
        orm_mode = True

class ParkingPaginated(ParkingBase):
    parking_spots: str

    class Config:
        orm_mode = True
