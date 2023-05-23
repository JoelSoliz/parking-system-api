from datetime import datetime, time

from pydantic import BaseModel

class BussinesHours(BaseModel):
    openning_time: time
    clousing_time: time
    days: str
    id_hour: str

    class Config:
        orm_mode = True

class BussinesUpdateA(BaseModel):
    openning_time: time
    clousing_time: time

    class Config:
        orm_mode = True

class BussinesUpdate(BussinesUpdateA):
    days: str

    class Config:
        orm_mode = True