from typing import Union
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from api.dependencies import get_db_session, get_current_user
from data.models import Administrator, Employee, Customer
from schemas.reservation import ReservationPaginated, Reservation
from services.administrator import AdministratorService
from services.reservation import ReservationService


reservation_router = APIRouter(prefix="/reservation")


@reservation_router.get("/", response_model=ReservationPaginated, tags=["Reservation"])
def get_reservation(
    current_page: int,
    session: Session = Depends(get_db_session),
    user: Union[Administrator, Employee] = Depends(get_current_user),
):
    role_service = ReservationService(session)
    print(user)
    if not isinstance(user, Administrator) and not isinstance(user, Employee):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You don't have permission to list reservations.",
        )

    return role_service.get_reservations(current_page)

@reservation_router.post("/reservation", response_model=Reservation, tags=["Reservation"])
def register_reservation(id_spot:str, reservation: Reservation, session: Session = Depends(get_db_session), 
                         user: Customer = Depends(get_current_user)):
    reservation_service = ReservationService(session)
    
    return reservation_service.register_reservation(user.id_customer, id_spot, reservation)