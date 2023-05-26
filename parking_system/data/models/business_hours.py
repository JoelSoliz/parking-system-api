from sqlalchemy import Column, String, Enum, Time
from sqlalchemy.orm import relationship

from data import Base


class BusinessHours(Base):
    __tablename__ = 'business_hours'
    id_hour = Column(String(4), primary_key=True)
    days = Column(Enum('Monday', 'Tuesday', 'Wednesday', 'Thursday',
                           'Friday', 'Saturday', 'Sunday', name='day_of_week_enum'), nullable=False)
    openning_time = Column(Time(), nullable=False)
    clousing_time = Column(Time(), nullable=False)
