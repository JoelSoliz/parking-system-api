from sqlalchemy import Column, String, Float, ForeignKey, DateTime, Time

from data import Base


class Pay(Base):
    __tablename__ = 'pay'
    id_pay = Column(String(4), primary_key=True)
    payment_date = Column(DateTime(), nullable=False)
    payment_time = Column(Time(), nullable=False)
    amount = Column(Float(precision=5), nullable=False)
    employee = Column(String(4), ForeignKey('customer.id_customer'))
