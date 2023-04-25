from datetime import datetime

from pydantic import BaseModel

class BussinesHours(BaseModel):
    openning_time: datetime
    clousing_time: datetime
    days: str
    id_hour: str

    class Config:
        orm_mode = True

class BussinesUpdate(BaseModel):
    openning_time: datetime
    clousing_time: datetime
    days: str