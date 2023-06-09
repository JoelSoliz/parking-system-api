from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session

from .dependencies import get_current_user, get_db_session
from schemas.vehicle import VehicleCreate
from services.customer import Customer
from services.vehicle import VehicleService

vehicle_router = APIRouter(prefix="/vehicle")


@vehicle_router.post("/", response_model=VehicleCreate, tags=["Vehicle"])
def register_vehicle(
    vehicle: VehicleCreate = Depends(),
    photo: UploadFile = File(default=None),
    session: Session = Depends(get_db_session),
    customer: Customer = Depends(get_current_user),
):
    vehicle_service = VehicleService(session)
    if photo:
        photo = photo.file.read()

    return vehicle_service.register_vehicle(customer.id_customer, photo, vehicle)
