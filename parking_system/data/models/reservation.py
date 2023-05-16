from datetime import datetime

from sqlalchemy import Column, String, Boolean, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from data import Base


class Reservation(Base):
    __tablename__ = "reservation"
    id_reservation = Column(String(4), primary_key=True)
    start_date = Column(Date(), nullable=False)
    end_date = Column(Date(), nullable=False)
    create_at = Column(DateTime(), default=datetime.now())
    id_customer = Column(String(4), ForeignKey("customer.id_customer"))
    id_price = Column(String(4), ForeignKey('hourly_rate.id_price'))

    customer = relationship("Customer", back_populates="reservations")
    reservation_assignment = relationship("ReservationAssignment", back_populates="reservations")
    weekdays = relationship("WeekDay", back_populates="reservation")
    pays = relationship("Pay", back_populates="reservations")

    def __repr__(self):
        return f"<Reservation(id_reservation='{self.id_reservation}', start_date='{self.start_date}', end_date='{self.end_date}')>"
