from datetime import date, datetime
from typing import Union
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from api.dependencies import get_db_session, get_current_user
from data.models import Administrator, Employee, Customer
from schemas.reservation import ReservationPaginated, Reservation, ReservationCreate
from schemas.assignment_reservation import ReservationAndParkingSpot, AssignmentBase, AssignmentUpdate, DaysAndDate
from services.reservation import ReservationService


reservation_router = APIRouter(prefix="/reservation")


@reservation_router.get("/{id}", response_model=ReservationAndParkingSpot, tags=["Reservation"])
def get_reservation(id: str, session: Session = Depends(get_db_session),
                    user: Union[Administrator, Employee] = Depends(get_current_user)):
    reservation_service = ReservationService(session)
    if not isinstance(user, Administrator) and not isinstance(user, Employee):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You don't have permission to see reservation.",
        )
    db_reservation = reservation_service.get_reservation(id)
    
    return db_reservation

@reservation_router.get("/spot/{id}", response_model=DaysAndDate, tags=["Reservation"])
def get_reservation_date(id_spot:str, start_date: date, end_date: date, session: Session = Depends(get_db_session)):
    reservation_service = ReservationService(session)
    resultado = reservation_service.get_reservation_date(id_spot, start_date, end_date)

    return resultado

@reservation_router.get("/", response_model=ReservationPaginated, tags=["Reservation"])
def get_reservations(
    current_page: int,
    session: Session = Depends(get_db_session),
    user: Union[Administrator, Employee] = Depends(get_current_user),
):
    role_service = ReservationService(session)
    if not isinstance(user, Administrator) and not isinstance(user, Employee):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You don't have permission to list reservations.",
        )

    return role_service.get_reservations(current_page)

@reservation_router.post("/reservation", response_model=Reservation, tags=["Reservation"])
def register_reservation(reservation: ReservationCreate, 
                         session: Session = Depends(get_db_session), 
                         user: Customer = Depends(get_current_user)):
    reservation_service = ReservationService(session)
    
    return reservation_service.register_reservation( user.id_customer, reservation)

@reservation_router.put('/{id}', response_model=AssignmentBase, tags=["Reservation"])
def reservation_accepted(id:str, session: Session = Depends(get_db_session),
                         user: Employee = Depends(get_current_user)):
    reservation_service = ReservationService(session)
    get_assignment = reservation_service.get_reservation_assignment(id)
    if not get_assignment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Reservation Assignment {id} not found. "
        )
    reservation_service.reservation_id_accepted(id, user.id_employee, get_assignment)

    return get_assignment

@reservation_router.put('/rejected/{id}', response_model=AssignmentBase, tags=["Reservation"])
def reservation_rejected(id:str, session: Session = Depends(get_db_session),
                         user: Employee = Depends(get_current_user)):
    reservation_service = ReservationService(session)
    get_assignment = reservation_service.get_reservation_assignment(id)
    if not get_assignment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Reservation Assignment {id} not found. "
        )
    reservation_service.reservation_id_rejected(id, user.id_employee, get_assignment)

    return get_assignment

