from sqlalchemy import Column, String, DateTime, Time, ForeignKey

from data import Base

class Reservation(Base):
    __tablename__ = 'reservation'
    id_reservation = Column(String(4), primary_key=True)
    start_date = Column(DateTime(), nullable=False)
    end_date = Column(DateTime(), nullable=False)
    start_time= Column(Time(), nullable=False)
    end_time = Column(Time(), nullable=False)
    days_of_use = Column(String(20), nullable=False)
    id_customer = Column(String(4), ForeignKey('customer.id_customer'))
    id_site = Column(String(4), ForeignKey('parking_space.id_site'))
