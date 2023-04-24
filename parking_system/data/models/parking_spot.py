from sqlalchemy import Column, String, Boolean, Text, ForeignKey
from sqlalchemy.orm import relationship
from data import Base


class ParkingSpot(Base):
    __tablename__ = 'parking_spot'
    id_spot = Column(String(4), primary_key=True)
    name = Column(String(4), nullable=False)
    coordinate = Column(Text, nullable=False)
    status = Column(Boolean(), nullable=False)
    section = Column(String(20), nullable=False)
    price = Column(String(4), ForeignKey('hourly_rate.id_price'))
    id_hour = Column(String(4), ForeignKey('business_hours.id_hour'))

    business_hours = relationship("BusinessHours", back_populates="parking_spots")
    hourly_rate = relationship("HourlyRate", back_populates= "parking_spots")