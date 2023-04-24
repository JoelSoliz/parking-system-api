from pydantic import BaseModel


class HourlyRate(BaseModel):

    week_day: str
    hourly_rate: float
    daily_rate: float
    weekly_rate: float
    monthly_rate: float
    annual_rate: float
    id_price: str
    
    class Config:
        orm_mode = True