from sqlalchemy import Column, String, Float, DateTime

from data import Base


class Price(Base):
    __tablename__ = 'hourly_rate'
    id_price = Column(String(4), primary_key=True)
    day_of_the_week = Column(DateTime(), nullable=False)
    hourly_rate = Column(Float(precision=5), nullable=False)
    daily_rate = Column(Float(precision=5), nullable=False)
    weekly_rate = Column(Float(precision=5), nullable=False)
    monthly_rate = Column(Float(precision=5), nullable=False)
    annual_rate = Column(Float(precision=5), nullable=False)
