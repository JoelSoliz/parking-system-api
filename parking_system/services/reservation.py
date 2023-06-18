from datetime import date, datetime
import math
from sqlalchemy import desc, func, and_, or_, asc
from sqlalchemy.orm import Session, joinedload
from fastapi import HTTPException, status

from send_email import send
from schemas.reservation import ReservationCreate
from schemas.assignment_reservation import AssignmentUpdate
from data.models.reservation import Reservation
from data.models.reservation_assignment import ReservationAssignment
from data.models.week_day import WeekDay
from data.models.customer import Customer
from .utils import generate_id
from .employee import EmployeeService as employee


class ReservationService:
    def __init__(self, session: Session):
        self.session = session

    def get_reservation(self, id_reservation: str):
        reservation = self.session.query(Reservation).options(
            joinedload(Reservation.weekdays),
            joinedload(Reservation.reservation_assignment).joinedload(
                ReservationAssignment.parking_spots),
            joinedload(Reservation.customer)    
        ).filter(Reservation.id_reservation == id_reservation).first()
        if not reservation:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Reservation not found"
            )
        data = {
            "customer": reservation.customer,
            "reservations": reservation,
            "parkings_spots": reservation.reservation_assignment[0].parking_spots,
            "status": reservation.reservation_assignment[0].status,
            "employee": employee.get_employee(self, reservation.reservation_assignment[0].assisted_by),
            "days": reservation.weekdays
        }

        return data
    
    def get_reservation_date(self, id_spot: str, start_date: date, end_date: date):
        reservations = self.session.query(Reservation).join(ReservationAssignment).filter(
            and_(or_(and_(start_date >= Reservation.start_date, 
                          start_date <= Reservation.end_date), 
                          and_(end_date >= Reservation.start_date, end_date <= Reservation.end_date)),
                 ReservationAssignment.status == 'Occupied',
                 ReservationAssignment.id_spot == id_spot)).options(
            joinedload(Reservation.weekdays)).all()

        b = {}
        for reservation in reservations:
            b.update(
                {f"{wd.day}-{str(wd.start_time)}-{str(wd.end_time)}": wd.__dict__ for wd in reservation.weekdays})
        
        data = {
            "week_days": list(b.values())
        }

        return data

    def get_reservations(self, current_page, page_count=7, status = None):
        result_query = self.session.query(Reservation, ReservationAssignment.id_spot, 
                                          ReservationAssignment.status).join(
            ReservationAssignment)
        
        if status:
            result_query = result_query.filter(and_(Reservation.start_date >= date.today(),
                                     ReservationAssignment.status==status))
        else :
            result_query = result_query.filter(Reservation.start_date >= date.today())

        results = (
            result_query.options(joinedload(Reservation.customer),
            joinedload(Reservation.reservation_assignment))
            .order_by(asc(Reservation.create_at))
            .offset((current_page - 1) * page_count)
            .limit(page_count)
        )
        count_data = result_query.count()
        b= [{"reservation": {"id_reservation": resultado[0].id_reservation, 
                             "start_date": resultado[0].start_date, 
                             "end_date": resultado[0].end_date, 
                             "customer":resultado[0].customer, 
                             "create_at":resultado[0].create_at}, 
                             "id_spot": resultado[1], "status": resultado[2]} for resultado in results]
        if count_data:
            data = {
                "results": b,
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
                                     id_customer=id_customer, id_price = reservation.id_price,
                                     start_date=reservation.start_date,
                                     end_date=reservation.end_date,
                                     )

        self.session.add(db_reservation)
        self.register_days(id_reservation, reservation.start_time,
                           reservation.end_time, reservation.day)
        self.register_assignment_reservation(reservation.id_spot,
                                             id_reservation
                                             )

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

    def register_assignment_reservation(self, id_spot, id_reservation: str):
        id = generate_id()
        db_assignment = ReservationAssignment(id_assignment=id, status='Reserved',
                                              id_spot=id_spot, id_reservation=id_reservation)

        self.session.add(db_assignment)

        return db_assignment

    def get_reservation_assignment(self, id_reservation: str):
        assignment = self.session.query(Reservation).join(ReservationAssignment).filter(
            ReservationAssignment.id_reservation == id_reservation).first()
        
       
        return assignment.reservation_assignment[0]


    # def update_reservation_assignment(self, id: str, reservation: AssignmentUpdate, get_assignment):
    #     self.session.query(ReservationAssignment).filter(
    #         ReservationAssignment.id_reservation == id).update({'status': reservation.status,
    #                                                            'id_spot': reservation.id_spot,
    #                                                            'id_assignment_rate': reservation.id_assignment_rate})
    #     self.session.commit()
    #     self.session.refresh(get_assignment)

    #     return get_assignment
    
    def update_reservation_assignment(self, id: str, reservation: AssignmentUpdate, get_assignment):
        self.session.query(ReservationAssignment).filter(
            ReservationAssignment.id_reservation == id).update({'status': reservation.status,
                                                               'id_spot': reservation.id_spot,
                                                               'id_assignment_rate': reservation.id_assignment_rate})
        self.session.commit()
        self.session.refresh(get_assignment)

        return get_assignment

    def get_email(self, id_reservation):
        query_email = self.session.query(Reservation).filter(
            Reservation.id_reservation==id_reservation).first()
        
        return [query_email.customer.email]
        
    def reservation_id_accepted(self, id_reservation, id_employee, get_assignment):
        self.session.query(ReservationAssignment).filter(
            ReservationAssignment.id_reservation==id_reservation
        ).update({
            ReservationAssignment.status:'Occupied',
            ReservationAssignment.assisted_by:id_employee,
            ReservationAssignment.assisted_datetime: datetime.now()
            }
        )
        
        self.session.commit()
        self.session.refresh(get_assignment)
        send(self.get_email(id_reservation), 
             "¡Nos complace informarle que su solicitud de reserva ha sido aceptada! Queremos agradecerle por elegir nuestros servicios y estamos encantados de poder atenderle.", 
             "Parking Spot")

        return get_assignment
    
    def reservation_id_rejected(self, id_reservation, id_employee,get_assignment):
        self.session.query(ReservationAssignment).filter(
            ReservationAssignment.id_reservation==id_reservation
        ).update({
            ReservationAssignment.status:'Available',
            ReservationAssignment.assisted_by:id_employee,
            ReservationAssignment.assisted_datetime: datetime.now()
            }
        )
        self.session.commit()
        self.session.refresh(get_assignment)
        send(self.get_email(id_reservation), 
             "Estimado usuario: Me pongo en contacto con respecto a su solicitud de reserva reciente.Lamentablemente, debo informarle que su solicitud de reserva ha sido rechazada.", 
             "Parking Spot")

        return get_assignment
