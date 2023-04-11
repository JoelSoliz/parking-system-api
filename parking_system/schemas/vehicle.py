from pydantic import BaseModel


class VehicleBase(BaseModel):
    license_plate: str
    vehicle_type: str
    color: str


class VehicleCreate(VehicleBase):
    class Config:
        orm_mode = True


class Vehicle(VehicleBase):
    id_vehicle: str
    id_customer: str

    class Config:
        orm_mode = True
