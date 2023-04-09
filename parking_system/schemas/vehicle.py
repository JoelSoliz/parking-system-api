from pydantic import BaseModel


class VehicleBase(BaseModel):
    license_plate: str
    vehicle_type: str

class VehicleCreate(VehicleBase):
    color: str

    class Config:
        orm_mode = True

class Vehicle(VehicleBase):
    color: str
