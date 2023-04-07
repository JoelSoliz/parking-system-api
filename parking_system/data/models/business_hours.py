from sqlalchemy import Column, String, DateTime

from data import Base


class BusinessHours(Base):
    __tablename__ = 'business_hours'
    id_hour = Column(String(4), primary_key=True)
    week_day = Column(DateTime(), nullable=False)
    opnning_time = Column(DateTime(), nullable=False)
    clousing_time = Column(DateTime(), nullable=False)
    
    