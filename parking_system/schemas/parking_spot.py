from pydantic import BaseModel


class ParkingBase(BaseModel):
    name: str
    address: str

class Parking(ParkingBase):
    id_parking: str
