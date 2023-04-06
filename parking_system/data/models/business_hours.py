from sqlalchemy import Column, String, DateTime, ForeignKey

from data import Base


class BusinessHours(Base):
    __tablename__ = 'bussiness_hours'
    id_hour = Column(String(4), primary_key=True)
    day_of_the_week = Column(DateTime(), nullable=False)
    opnning_time = Column(DateTime(), nullable=False)
    clousing_time = Column(DateTime(), nullable=False)
    id_parking = Column(String(4), ForeignKey('parking.id_parking'))
    