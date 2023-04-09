from sqlalchemy.orm import Session

from data.models.vehicle import Vehicle
from schemas.vehicle import VehicleCreate
from .utils import generate_id, get_hashed_password

class VehicleService():
    def __init__(self, session: Session):
        self.session = session

    def register_vehicle(self, id_customer, photo, vehicle: VehicleCreate):
        id_vehicle = generate_id()
        db_vehicle = Vehicle(id_vehicle=id_vehicle, id_customer=id_customer, 
                                license_plate=vehicle.license_plate, vehicle_type=vehicle.vehicle_type,
                                color=vehicle.color, photo=photo)
        self.session.add(db_vehicle)
        self.session.commit()   
        self.session.refresh(db_vehicle)
        return db_vehicle
