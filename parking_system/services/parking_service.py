from sqlalchemy.orm import joinedload
from sqlalchemy.orm import Session
from schemas.parking_spot import ParkingRegister
from schemas.business_hours import BussinesUpdate, BussinesHours, BussinesUpdateA
from data.models.business_hours import BusinessHours
from data.models.assignment_rate import AssignmentRate
from data.models.parking_spot import ParkingSpot
from .utils import generate_id


class ParkingService:
    def __init__(self, session: Session):
        self.session = session


    def get_parking_and_price(self, id_spot: str):
        parking_spot = self.session.query(ParkingSpot).options(
            joinedload(ParkingSpot.assignment_rate)
        ).filter(ParkingSpot.id_spot == id_spot).first()
        parking_with_price = {
            "parking_spot": parking_spot,
            "prices": parking_spot.assignment_rate[0].price
        }

        return parking_with_price


    def get_parking_spots(self):
        result_query = self.session.query(ParkingSpot).all()
        
        return result_query

    def register_parking_spot(self, parking: ParkingRegister):
        id_parking = generate_id()
        db_parking_spot = ParkingSpot(id_spot=id_parking, name=parking.name,
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

    def get_hours(self):
        db_get_hour = self.session.query(BusinessHours).all()
        
        return db_get_hour

    def get_hour(self, id_hour: str):
        db_get_hour = self.session.query(BusinessHours).filter(
            BusinessHours.id_hour == id_hour).first()
        
        return db_get_hour


    def update_hour(self, id: str, hour: BussinesUpdateA, get_hour):
        self.session.query(BusinessHours).filter(
            BusinessHours.id_hour == id).update({'openning_time': hour.openning_time,
                                                'clousing_time': hour.clousing_time})
        self.session.commit()
        self.session.refresh(get_hour)

        return get_hour
    
    def get_spot_section(self, type: str):
        type_query = self.session.query(ParkingSpot).options(
            joinedload(ParkingSpot.assignment_rate)
        ).filter(ParkingSpot.type==type).all()
        print(type_query[0].assignment_rate[0].price)
        
        results = [{'spot':{'id_spot':type.id_spot, 'name': type.name, 
                      'coordinate': type.coordinate, 
                      'section': type.section, 'type': type.type},
                      'hourly_rate': type.assignment_rate[0].price} for type in type_query]
        return results
