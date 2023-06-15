import math
from datetime import datetime, timedelta


# from services.send_email import send
from sqlalchemy.orm import Session, joinedload
from sqlalchemy.sql import desc, select, and_, exists
from fastapi import HTTPException, status

from .utils import generate_id

from schemas.pay import PayAndReservation
from data.models.pay import Pay
from data.models.reservation import Reservation
from data.models.reservation_assignment import ReservationAssignment
from data.models.customer import Customer
from data.models.user import User

class PayService:
    def __init__(self, session: Session):
        self.session = session

    def register_payment(self, pay: PayAndReservation):
        id_pay = generate_id()
        if self.get_reservation_assigment(pay.reservation):
            payment_registered = Pay(id_pay = id_pay, reservation = pay.reservation, 
                        amount = pay.amount) 
            self.session.add(payment_registered)
            self.session.commit()
            self.session.refresh(payment_registered)
            return payment_registered
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="Unfortunately, it is not possible to process the payment at this time. Your booking request has not been accepted yet or may have been rejected."
            )
        
    
    def get_reservation_assigment(self, id_reservation: str):
        accept_reservation = self.session.query(ReservationAssignment).filter(
            and_(ReservationAssignment.id_reservation == id_reservation, 
                 ReservationAssignment.status=='Occupied')
        ).first()
        return accept_reservation

    def receive_payments(self, current_page, page_size=5, name=None, date = None):
        query = self.session.query(Pay).join(Reservation).join(Reservation.reservation_assignment).options(
            joinedload(Pay.reservations).joinedload(Reservation.customer)
        ).order_by(desc(Pay.payment_datetime))

        if name:
            customer_subquery = select(Reservation.id_customer).join(Customer).filter(Customer.name == name).subquery()
            query = query.filter(Reservation.id_customer.in_(customer_subquery))
        
        if date:
            query = query.filter(Pay.payment_datetime.like(f"%{date}%"))

        count_data = query.count()
    
        offset_value = (current_page - 1) * page_size
        query = query.limit(page_size).offset(offset_value)
        
        results=[{"pay":{"id_pay": pay.id_pay, 
                      "amount": pay.amount, 
               "payment_datetime": pay.payment_datetime},
               "customer": pay.reservations.customer, 
               "id_spot": pay.reservations.reservation_assignment[0].id_spot} 
               for pay in query]
        
        if count_data:
            data = {
                "results": results,
                "current_page": current_page,
                "total_pages": math.ceil(count_data / page_size),
                "total_elements": count_data,
                "element_per_page": page_size,
            }
        else:
            data = {
                "results": [],
                "current_page": 0,
                "total_pages": 0,
                "total_elements": 0,
                "element_per_page": 0,
            }

        return data
    
    def collect_overdue_payments(self, current_page, page_size=20):
        subquery = self.session.query(Pay.reservation_id).subquery()
        query_pay = self.session.query(Reservation).join(ReservationAssignment).options(
            joinedload(Reservation.customer),
            joinedload(Reservation.pays)
        ).filter(
            and_(datetime.now()+timedelta(minutes=60) > ReservationAssignment.assisted_datetime,
                 ReservationAssignment.status=='Occupied',~exists().where(Pay.reservation_id == Reservation.id).correlate(Reservation)))
        
        offset_value = (current_page - 1) * page_size
        query = query_pay.limit(page_size).offset(offset_value)
        print(query.count)

        if query.count() >= 1 :
            results = [{'customer':query.customer, 'price': query.price,
                        'spot': query.reservation_assignment[0].parking_spots} for query in query]
            print(results)
            return {'results': results}
        else:
            return{'results': []}
        