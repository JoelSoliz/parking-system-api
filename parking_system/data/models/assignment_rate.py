from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from data import Base

class AssignmentRate(Base):
    __tablename__  = 'assignment_rate'
    id_assignment_rate = Column(String(4), primary_key=True)
    id_spot = Column(String(4), ForeignKey('parking_spot.id_spot'))
    id_price = Column(String(4), ForeignKey('hourly_rate.id_price'))

    parking_spot = relationship('ParkingSpot', back_populates='assignment_rate')
    price = relationship('HourlyRate', back_populates='assignment_rate')