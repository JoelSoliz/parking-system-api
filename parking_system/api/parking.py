from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from api.dependencies import get_db_session, get_current_user
from schemas.parking_spot import ParkingBase, ShowParking, ParkingRegister
from schemas.business_hours import BussinesUpdate, BussinesHours, BussinesUpdateA
from schemas.assignment_rate import AssignmentBase
from schemas.hourly_rate import SpotAndType
from services.parking_service import ParkingService
from services.employee import EmployeeService
from services.administrator import AdministratorService
from data.models.employee import Employee
from data.models.administrator import Administrator


parking_router = APIRouter(prefix="/parking")


@parking_router.get("/{id}", response_model=AssignmentBase, tags=["Parking"])
def get_parking_spot(
    id: str,
    session: Session = Depends(get_db_session),
):
    parking_service = ParkingService(session)
    db_parking_spot = parking_service.get_parking_and_price(id)
    if not db_parking_spot:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Parking spot not found"
        )

    return db_parking_spot


@parking_router.get("/", response_model=list[ShowParking], tags=["Parking"])
def get_parking_spots(session: Session = Depends(get_db_session)):
    parking_spot = ParkingService(session)

    return parking_spot.get_parking_spots()

@parking_router.get("/hours/", response_model=list[BussinesUpdate], tags=["Parking"])
def get_bussines_hours(session: Session = Depends(get_db_session)):
    db_bussiness_hour = ParkingService(session)
    return db_bussiness_hour.get_hours()

@parking_router.get("/spot/type", response_model=list[SpotAndType], tags=["Parking"])
def get_type_spot(type: str, session: Session = Depends(get_db_session)):
    parking_service = ParkingService(session)
    return parking_service.get_spot_section(type) 

@parking_router.put("/{id}", response_model=BussinesHours, tags=["Parking"])
def update_hour_parking(
    id: str,
    hour: BussinesUpdateA = Depends(),
    session: Session = Depends(get_db_session),
    _: Administrator = Depends(get_current_user),
):
    parking_service = ParkingService(session)
    get_hour = parking_service.get_hour(id)
    if not get_hour:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Bussines Hour {id} not found. "
        )
    parking_service.update_hour(id, hour, get_hour)

    return get_hour


@parking_router.post("/", response_model=ParkingBase, tags=["Parking"])
def register_parking(
    parking: ParkingRegister,
    session: Session = Depends(get_db_session),
    administrator: Administrator = Depends(get_current_user),
):
    parking_service = ParkingService(session)
    administrator_service = AdministratorService(session)
    db_administrator = administrator_service.get_administrator_by_email(administrator.email)
    if isinstance(db_administrator, bool) or not db_administrator:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You don't have permission to register new parking spot.",
        )

    return parking_service.register_parking_spot(parking)


@parking_router.post("/register-hour", response_model=BussinesHours, tags=["Parking"])
def register_business_hour(
    business: BussinesUpdate,
    session: Session = Depends(get_db_session),
    administrator: Administrator = Depends(get_current_user),
):
    parking_service = ParkingService(session)
    administrator_service = AdministratorService(session)
    db_administrator = administrator_service.get_administrator_by_email(administrator.email)
    if isinstance(db_administrator, bool) or not db_administrator:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You don't have permission to register business hour.",
        )

    return parking_service.register_business_hour(business)
