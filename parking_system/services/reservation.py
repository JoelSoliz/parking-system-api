import math
from sqlalchemy import desc, func
from sqlalchemy.orm import Session, joinedload

from data.models import Reservation


class ReservationService:
    def __init__(self, session: Session):
        self.session = session

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
                "results": [customer.__dict__ for customer in results],
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
