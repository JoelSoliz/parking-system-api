from sqlalchemy.orm import Session

from .utils import generate_id

from schemas.pay import PayAndReservation
from data.models.pay import Pay

class PayService:
    def __init__(self, session: Session):
        self.session = session

    def register_payment(self, pay: PayAndReservation):
        id_pay = generate_id()
        payment_registered = Pay(id_pay = id_pay, reservation = pay.reservation, 
                       amount = pay.amount) 
        self.session.add(payment_registered)
        self.session.commit()
        self.session.refresh(payment_registered)

        return payment_registered