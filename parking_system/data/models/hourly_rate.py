from sqlalchemy import Column, String, Float, Enum

from data import Base


class HourlyRate(Base):
    __tablename__ = 'hourly_rate'
    id_price = Column(String(4), primary_key=True)
    week_day = Column(Enum('Monday', 'Tuesday', 'Wednesday', 'Thursday',
                           'Friday', 'Saturday', 'Sunday', name='day_of_week_enum'), nullable=False)
    hourly_rate = Column(Float(precision=5), nullable=False)
    daily_rate = Column(Float(precision=5), nullable=False)
    weekly_rate = Column(Float(precision=5), nullable=False)
    monthly_rate = Column(Float(precision=5), nullable=False)
    annual_rate = Column(Float(precision=5), nullable=False)
