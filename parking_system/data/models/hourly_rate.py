from sqlalchemy import Column, String, Float, Enum, Date
from sqlalchemy.orm import relationship

from data import Base


class HourlyRate(Base):
    __tablename__ = 'hourly_rate'
    id_price = Column(String(4), primary_key=True)
    hourly_rate = Column(Float(precision=5), nullable=False)
    daily_rate = Column(Float(precision=5), nullable=False)
    weekly_rate = Column(Float(precision=5), nullable=False)
    monthly_rate = Column(Float(precision=5), nullable=False)
    annual_rate = Column(Float(precision=5), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)
    
    assignment_rate = relationship('AssignmentRate', back_populates='price')
