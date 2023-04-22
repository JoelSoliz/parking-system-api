from sqlalchemy import Column, String, Enum, Time, ForeignKey
from sqlalchemy.orm import relationship

from data import Base


class WeekDay(Base):
    __tablename__ = "weekday"
    id_day = Column(String(4), primary_key=True)
    day = Column(Enum('Monday', 'Tuesday', 'Wednesday', 'Thursday',
                        'Friday', 'Saturday', 'Sunday', name='day_of_week_enum'), nullable=False)
    id_reservation = Column(String(4), ForeignKey("reservation.id_reservation"))
    start_time = Column(Time(), nullable=False)
    end_time = Column(Time(), nullable=False)
