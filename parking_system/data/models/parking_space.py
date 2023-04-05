from sqlalchemy import Column, String, Boolean, ForeignKey

from data import Base

class Parking_space(Base):
    __tablename__ = 'parking_space'
    id_site = Column(String(4), primary_key=True)
    state = Column(Boolean(), nullable=False)
    description = Column(String(200), nullable=False)
    id_parking = Column(String(4), ForeignKey('parking.id_parking'))
    id_price = Column(String(4), ForeignKey('hourly_rate.id_price'))
