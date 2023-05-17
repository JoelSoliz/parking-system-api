from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.dependencies import get_current_user, get_db_session
from schemas.pay import PayAndReservation
from schemas.pay import Pay  as P
from services.pay import PayService


pay_router = APIRouter(prefix="/pay")

@pay_router.post("/", response_model=P, tags=["Pay"])
def payment(pay: PayAndReservation, session: Session=Depends(get_db_session)):
    pay_service = PayService(session)


    return pay_service.register_payment(pay)