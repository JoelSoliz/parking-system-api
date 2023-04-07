from sqlalchemy import Column, String, Boolean, ForeignKey

from data import Base


class ParkingSpot(Base):
    __tablename__ = 'parking_spot'
    id_spot = Column(String(4), primary_key=True)
    name = Column(String(4), nullable=False)
    address = Column(String(4), nullable=False)
    state = Column(Boolean(), nullable=False)
    description = Column(String(200), nullable=False)
    price = Column(String(4), ForeignKey('hourly_rate.id_price'))
    id_hour = Column(String(4), ForeignKey('business_hours.id_hour'))
