from sqlalchemy import Column, String, Text, Enum, ForeignKey
from sqlalchemy.orm import relationship
from data import Base


class ParkingSpot(Base):
    __tablename__ = 'parking_spot'
    id_spot = Column(String(4), primary_key=True)
    name = Column(String(20), nullable=False)
    coordinate = Column(Text, nullable=False)
    section = Column(String(20), nullable=False)
    type_spot = Column(String(4), ForeignKey('parking_type.id_spot_type'))

    reservation_assignment = relationship("ReservationAssignment", back_populates="parking_spots")
    assignment_rate = relationship('AssignmentRate', back_populates='parking_spot')
    parking_type = relationship("ParkingType", back_populates="parking_spot")
    
    
    def __repr__(self):
        return f"<ParkingSpot(id_spot='{self.id_spot}', name='{self.name}', section='{self.section}', type_spot='{self.type_spot}')>"
