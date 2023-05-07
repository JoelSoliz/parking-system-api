from pydantic import BaseModel
from .parking_spot import ParkingBase, ShowParking
from .hourly_rate import HourlyRateBase

class AssignmentBase(BaseModel):
    parking_spot: ParkingBase
    price: HourlyRateBase

    class Config:
        orm_mode = True

class WithParking(AssignmentBase):
    parking_spot: ShowParking