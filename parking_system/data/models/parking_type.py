from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from data import Base


class ParkingType(Base):
    __tablename__ = 'parking_type'
    id_spot_type = Column(String(4), primary_key=True)
    type = Column(String(20), nullable=False)
    
    parking_spot = relationship("ParkingSpot", back_populates="parking_type")
    