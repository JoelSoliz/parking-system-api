from datetime import datetime
from sqlalchemy import Column, String, Float, ForeignKey, DateTime, Time
from sqlalchemy.orm import relationship

from data import Base


class Pay(Base):
    __tablename__ = 'pay'
    id_pay = Column(String(4), primary_key=True)
    payment_datetime = Column(DateTime(), default=datetime.now())
    amount = Column(Float(precision=5), nullable=False)
    # customer = Column(String(4), ForeignKey('customer.id_customer'))
    reservation = Column(String(4), ForeignKey('reservation.id_reservation'))

    # customer = relationship("Customer", back_populates="pays")
    reservations = relationship("Reservation", back_populates="pays")
