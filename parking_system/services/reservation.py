from datetime import date, datetime
import math
from sqlalchemy import desc, func, and_, or_
from sqlalchemy.orm import Session, joinedload
from fastapi import HTTPException, status

from schemas.reservation import ReservationCreate
from schemas.assignment_reservation import AssignmentUpdate, ReservationWithParkingAndAssignment, AssignmentBase
from data.models.reservation import Reservation
from data.models.reservation_assignment import ReservationAssignment
from data.models.week_day import WeekDay
from data.models.parking_spot import ParkingSpot
from .utils import generate_id


class ReservationService:
    def __init__(self, session: Session):
        self.session = session

    def get_reservation(self, id_reservation: str):
        reservation = self.session.query(Reservation).options(
            joinedload(Reservation.weekdays),
            joinedload(Reservation.reservation_assignment).joinedload(
                ReservationAssignment.parking_spots),
        ).filter(Reservation.id_reservation == id_reservation).first()
        if not reservation:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Reservation not found"
            )

        data = {
            "reservations": reservation,
            "parkings_spots": reservation.reservation_assignment[0].parking_spots,
            "status": reservation.reservation_assignment[0].status,
            "days": reservation.weekdays
        }

        return data

    def get_reservation_date(self, id_spot: str, start_date: date, end_date: date):
        reservations = self.session.query(Reservation).join(ReservationAssignment).filter(
            and_(or_(and_(start_date >= Reservation.start_date, start_date <= Reservation.end_date), and_(end_date >= Reservation.start_date, end_date <= Reservation.end_date)),
                 ReservationAssignment.status == 'Occupied',
                 ReservationAssignment.id_spot == id_spot)).options(joinedload(Reservation.weekdays)).all()

        b = {}
        for reservation in reservations:
            b.update(
                {f"{wd.day}-{str(wd.start_time)}-{str(wd.end_time)}": wd.__dict__ for wd in reservation.weekdays})
        print(b)
        data = {
            "week_days": list(b.values())
        }

        return data

    def get_reservations(self, current_page, page_count=10):
        result_query = self.session.query(Reservation).filter(
            Reservation.start_date >= date.today())
        results = (
            result_query.options(joinedload(Reservation.customer), 
                                 joinedload(Reservation.reservation_assignment))
            .order_by(desc(func.timediff(Reservation.end_date, Reservation.start_date)))
            .offset((current_page - 1) * page_count)
            .limit(page_count)
            .all()
        )
        count_data = result_query.count()

        if count_data:
            data = {
                "results": [employee.__dict__ for employee in results],
                "id_spot": [spot.id_spot for result in results for spot in result.reservation_assignment],
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
        db_reservation = Reservation(id_reservation=id_reservation,
                                     id_customer=id_customer,
                                     start_date=reservation.start_date,
                                     end_date=reservation.end_date,
                                     )

        self.session.add(db_reservation)
        self.register_days(id_reservation, reservation.start_time,
                           reservation.end_time, reservation.day)
        self.register_assignment_reservation(reservation.id_spot,
                                             id_reservation,
                                             reservation.id_assignment_rate)

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

    def register_assignment_reservation(self, id_spot, id_reservation: str, id_assignment: str):
        id = generate_id()
        db_assignment = ReservationAssignment(id_assignment=id, status='Reserved',
                                              id_spot=id_spot, id_reservation=id_reservation,
                                              id_assignment_rate=id_assignment)

        self.session.add(db_assignment)

        return db_assignment

    def get_reservation_assignment(self, id_reservation: str):
        assignment = self.session.query(Reservation).join(ReservationAssignment).filter(
            ReservationAssignment.id_reservation == id_reservation).first()
        
       
        return assignment.reservation_assignment[0]


    def update_reservation_assignment(self, id: str, reservation: AssignmentUpdate, get_assignment):
        self.session.query(ReservationAssignment).filter(
            ReservationAssignment.id_assignment == id).update({'status': reservation.status,
                                                               'id_spot': reservation.id_spot,
                                                               'id_assignment_rate': reservation.id_assignment_rate})
        self.session.commit()
        self.session.refresh(get_assignment)

        return get_assignment
    
    def reservation_id_accepted(self, id_reservation, get_assignment):
        self.session.query(ReservationAssignment).filter(
            ReservationAssignment.id_reservation==id_reservation
        ).update({
            ReservationAssignment.status:'Occupied'
            }
        )
        self.session.commit()
        self.session.refresh(get_assignment)

        return get_assignment
    
    def reservation_id_rejected(self, id_reservation, get_assignment):
        self.session.query(ReservationAssignment).filter(
            ReservationAssignment.id_reservation==id_reservation
        ).update({
            ReservationAssignment.status:'Available'
            }
        )
        self.session.commit()
        self.session.refresh(get_assignment)

        return get_assignment
