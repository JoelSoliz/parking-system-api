from sqlalchemy import Column, String, Boolean, Text, ForeignKey, Enum
from sqlalchemy.orm import relationship
from data import Base


class ParkingSpot(Base):
    __tablename__ = 'parking_spot'
    id_spot = Column(String(4), primary_key=True)
    name = Column(String(4), nullable=False)
    coordinate = Column(Text, nullable=False)
    section = Column(String(20), nullable=False)
    type = Column(Enum('Previlegiado', 'Regular', 'Común'), nullable=False)
    id_hour = Column(String(4), ForeignKey('business_hours.id_hour'))

    business_hours = relationship("BusinessHours", back_populates="parking_spots")
    reservation_assignment = relationship("ReservationAssignment", back_populates="parking_spots")
    assignment_rate = relationship('AssignmentRate', back_populates='parking_spot')
    
