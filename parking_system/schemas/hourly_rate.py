from datetime import date
from typing import Optional

from pydantic import BaseModel

from .parking_spot import ParkingBase

class HourlyRateBase(BaseModel):

    hourly_rate: float
    daily_rate: float
    weekly_rate: float
    monthly_rate: float
    annual_rate: float
    start_date: date
    end_date: Optional[date]
    
    class Config:
        orm_mode = True

class SpotAndType(BaseModel):
    hourly_rate: HourlyRateBase
    spot: ParkingBase


class HourlyRate(HourlyRateBase):
    id_price: str