from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.dependencies import get_current_user, get_db_session
from schemas.pay import PayAndReservation
from schemas.pay import Pay, PayWithCustomer, Result, LatePayment, PaginatedLatePayment
from services.pay import PayService
from data.models.customer import Customer


pay_router = APIRouter(prefix="/pay")

@pay_router.post("/", response_model=Pay, tags=["Pay"])
def payment(pay: PayAndReservation, session: Session=Depends(get_db_session),
            _: Customer = Depends(get_current_user)):
    pay_service = PayService(session)

    return pay_service.register_payment(pay)

@pay_router.get("/", response_model=Result, tags=["Pay"])
def get_payments(current_page: int, session: Session=Depends(get_db_session), name = None, date = None):
    pay_servece = PayService(session)
    return pay_servece.receive_payments(current_page, name=name, date=date)

@pay_router.get("/lates/", response_model=PaginatedLatePayment, tags=["Pay"])
def get_payments_late(current_page: int, session:Session=Depends(get_db_session)):
    pay_servece = PayService(session)
    
    return pay_servece.collect_overdue_payments(current_page)
