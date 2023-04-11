from datetime import datetime
from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from .user import User


class Customer(User):
    __tablename__ = "customer"
    id_customer = Column(String(4), primary_key=True)
    id_user = Column(String(4), ForeignKey("user.id_user"))
    created_at = Column(DateTime(), default=datetime.now())

    reservations = relationship("Reservation", back_populates="customer")

    __mapper_args__ = {
        "polymorphic_identity": "customer",
    }
