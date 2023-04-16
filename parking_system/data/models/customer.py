from datetime import datetime
from sqlalchemy import Column, String, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship

from .user import User


class Customer(User):
    __tablename__ = "customer"
    id_customer = Column(String(4), primary_key=True)
    id_user = Column(String(4), ForeignKey("user.id_user"))
    notification_type = Column(Enum('Whatsapp', 'Email'), nullable=False)
    created_at = Column(DateTime(), default=datetime.now())

    reservations = relationship("Reservation", back_populates="customer")

    __mapper_args__ = {
        "polymorphic_identity": "customer",
    }
