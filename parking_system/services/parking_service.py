import math

from sqlalchemy.orm import joinedload
from sqlalchemy.orm import Session
from schemas.parking_spot import ParkingRegister
from schemas.business_hours import BussinesUpdate, BussinesHours
from data.models.business_hours import BusinessHours
from data.models.parking_spot import ParkingSpot
from .utils import generate_id


class ParkingService:
    def __init__(self, session: Session):
        self.session = session

    def get_parking_spot(self, id_spot: str):
        parking_spot = (self.session.query(ParkingSpot)
                        .options(
            joinedload(ParkingSpot.hourly_rate),
            joinedload(ParkingSpot.business_hours)
        )
            .filter(ParkingSpot.id_spot == id_spot)
        )

        return parking_spot.first()

    def get_parking_spots(self):
        result_query = self.session.query(ParkingSpot).all()

        return result_query

    def register_parking_spot(self, parking: ParkingRegister):
        id_parking = generate_id()
        db_parking_spot = ParkingSpot(id_spot=id_parking, price=parking.price,
                                      id_hour=parking.id_hours, name=parking.name,
                                      section=parking.section, status=parking.status,
                                      coordinate=parking.coordinate)

        self.session.add(db_parking_spot)
        self.session.commit()
        self.session.refresh(db_parking_spot)

        return db_parking_spot
    
    def register_business_hour(self, business_hours: BussinesHours):
        id_hour = generate_id()
        db_business_hour = BusinessHours(id_hour = id_hour, openning_time = business_hours.openning_time,
                                         clousing_time = business_hours.clousing_time,
                                         days = business_hours.days)
        self.session.add(db_business_hour)
        self.session.commit()
        self.session.refresh(db_business_hour)

        return db_business_hour


    def get_hour(self, id_hour: str):
        db_get_hour = self.session.query(BusinessHours).filter(
            BusinessHours.id_hour == id_hour).first()
        return db_get_hour

    def update_hour(self, id: str, hour: BussinesUpdate, get_hour):
        self.session.query(BusinessHours).filter(
            BusinessHours.id_hour == id).update({'openning_time': hour.openning_time,
                                             'clousing_time': hour.clousing_time, 
                                             'days': hour.days})
        self.session.commit()
        self.session.refresh(get_hour)

        return get_hour
