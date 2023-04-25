import math
from sqlalchemy import desc, func
from sqlalchemy.orm import Session, joinedload

from schemas.reservation import ReservationCreate
from data.models.reservation import Reservation
from data.models.week_day import WeekDay
from .utils import generate_id


class ReservationService:
    def __init__(self, session: Session):
        self.session = session

    def get_reservation(self, id_reservation: str):
        reservation = (self.session.query(Reservation)
                    .options(
                        joinedload(Reservation.customer),
                        joinedload(Reservation.parking_spot)
                    )
                    .filter(Reservation.id_reservation == id_reservation)
        )

        return reservation.first()

    def get_reservations(self, current_page, page_count=10):
        result_query = self.session.query(Reservation)
        results = (
            result_query.filter(Reservation.start_date >= func.now())
            .options(joinedload(Reservation.customer))
            .order_by(desc(func.timediff(Reservation.end_date, Reservation.start_date)))
            .offset((current_page - 1) * page_count)
            .limit(page_count)
            .all()
        )
        count_data = result_query.count()

        if count_data:
            data = {
                "results": [employee.__dict__ for employee in results],
                "current_page": current_page,
                "total_pages": math.ceil(count_data / page_count),
                "total_elements": count_data,
                "element_per_page": page_count,
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
    
    def register_reservation(self, id_customer: str, reservation: ReservationCreate):
        id_reservation = generate_id()
        db_reservation = Reservation(id_reservation = id_reservation,
                                    id_spot = reservation.id_spot,
                                    id_customer = id_customer,
                                    start_date = reservation.start_date,
                                    end_date = reservation.end_date,
                                    )
        
        self.session.add(db_reservation)
        self.register_days(id_reservation, reservation.start_time, reservation.end_time, reservation.day)
        self.session.commit()
        self.session.refresh(db_reservation)

        return db_reservation
    
    def register_days(self, id_reservation, start_times, end_times, days):
        for start, end, day in zip(start_times, end_times, days):
            id_day = generate_id()
            db_day = WeekDay(
                id_day=id_day,
                id_reservation=id_reservation,
                day=day,
                start_time=start,
                end_time=end
            )
            self.session.add(db_day)
