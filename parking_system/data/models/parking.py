from sqlalchemy import Column, String

from data import Base

class Parking(Base):
    __tablename__ = 'parking'
    id_parking = Column(String(4), primary_key=True)
    name = Column(String(4), primary_key=True)
    address = Column(String(200), nullable=False)
