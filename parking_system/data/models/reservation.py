from datetime import datetime

from sqlalchemy import Column, String, Boolean, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from data import Base


class Reservation(Base):
    __tablename__ = "reservation"
    id_reservation = Column(String(4), primary_key=True)
    start_date = Column(Date(), nullable=False)
    end_date = Column(Date(), nullable=False)
    status = Column(Boolean, default=False)
    create_at = Column(DateTime(), default=datetime.now())
    id_customer = Column(String(4), ForeignKey("customer.id_customer"))
    id_spot = Column(String(4), ForeignKey("parking_spot.id_spot"))

    customer = relationship("Customer", back_populates="reservations")
    