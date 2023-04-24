from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from api.dependencies import get_db_session, get_current_user
from schemas.parking_spot import ParkingBase, ParkingPaginated, ShowParking, ParkingRegister
from services.parking_service import ParkingService
from services.employee import EmployeeService
from services.administrator import AdministratorService
from data.models.employee import Employee
from data.models.administrator import Administrator


parking_router = APIRouter(prefix='/parking')


@parking_router.get("/{id}", response_model=ShowParking, tags=["Parking"])
def get_parking_spot(id: str, session: Session = Depends(get_db_session),
                     employee: Employee = Depends(get_current_user)):
    parking_service = ParkingService(session)
    employee_service = EmployeeService(session)
    db_employee = employee_service.get_employee_by_email(employee.email)
    if isinstance(db_employee, bool) or not db_employee:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You don't have permission to list parking spot.",
        )

    return parking_service.get_parking_spot(id)


@parking_router.get("/", response_model=ParkingPaginated, tags=["Parking"])
def get_parking_spots(current_page: int, session: Session = Depends(get_db_session), 
                      employee:Employee = Depends(get_current_user)):
    parking_spot = ParkingService(session)
    employee_service = EmployeeService(session)
    db_employee = employee_service.get_employee_by_email(employee.email)
    if isinstance(db_employee, bool) or not db_employee:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You don't have permission to list parking spot.",
        )
    
    return parking_spot.get_parking_spots(current_page)

@parking_router.post("/", response_model=ParkingBase, tags=["Parking"])
def register_parking(parking: ParkingRegister, session: Session = Depends(get_db_session),
                     administrator: Administrator = Depends(get_current_user)):
    parking_service = ParkingService(session)
    administrator_service = AdministratorService(session)
    db_administrator = administrator_service.get_administrator_by_email(administrator.email)
    if isinstance(db_administrator, bool) or not db_administrator:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You don't have permission to register new parking spot.",
        )
    
    return parking_service.register_parking_spot(parking)