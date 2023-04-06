from sqlalchemy import Column, String, Boolean, ForeignKey

from data import Base


class ParkingSpot(Base):
    __tablename__ = 'parking_spot'
    id_site = Column(String(4), primary_key=True)
    state = Column(Boolean(), nullable=False)
    description = Column(String(200), nullable=False)
    parking = Column(String(4), ForeignKey('parking.id_parking'))
    price = Column(String(4), ForeignKey('hourly_rate.id_price'))
