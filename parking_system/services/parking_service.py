from sqlalchemy.orm import joinedload
from sqlalchemy.orm import Session
from schemas.parking_spot import ParkingRegister
from schemas.business_hours import BussinesUpdate, BussinesHours
from data.models.business_hours import BusinessHours
from data.models.assignment_rate import AssignmentRate
from data.models.parking_spot import ParkingSpot
from .utils import generate_id


class ParkingService:
    def __init__(self, session: Session):
        self.session = session

    def get_parking_and_price(self, id_rate: str):
        parking_spot = (self.session.query(AssignmentRate)
                        .options(
            joinedload(AssignmentRate.parking_spot),
            joinedload(AssignmentRate.price)
        )
            .filter(AssignmentRate.id_assignment_rate == id_rate).first()
        )

        return parking_spot
    

    def get_parking_spots(self):
        result_query = self.session.query(ParkingSpot).all()
        
        return result_query

    def register_parking_spot(self, parking: ParkingRegister):
        id_parking = generate_id()
        db_parking_spot = ParkingSpot(id_spot=id_parking,id_hour=parking.id_hours, name=parking.name,
                                      section=parking.section, type=parking.type, 
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
    
    def get_hour_and_parking():

        pass

    def update_hour(self, id: str, hour: BussinesUpdate, get_hour):
        self.session.query(BusinessHours).filter(
            BusinessHours.id_hour == id).update({'openning_time': hour.openning_time,
                                                'clousing_time': hour.clousing_time, 
                                                'days': hour.days})
        self.session.commit()
        self.session.refresh(get_hour)

        return get_hour
