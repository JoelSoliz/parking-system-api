from datetime import datetime

from sqlalchemy import Column, String, Enum, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from data import Base

class ReservationAssignment(Base):
    __tablename__ = 'reservation_assignment'
    id_assignment = Column(String(4), primary_key=True)
    status = Column(Enum('Reserved', 'Occupied', 'Available'), nullable=False)
    date_created = Column(DateTime(), default=datetime.now())
    id_spot = Column(String(4), ForeignKey('parking_spot.id_spot'))
    id_reservation = Column(String(4), ForeignKey('reservation.id_reservation'))
    # id_assignment_rate = Column(String(4), ForeignKey('assignment_rate.id_assignment_rate'))

    parking_spots = relationship("ParkingSpot", back_populates="reservation_assignment")
    reservations = relationship("Reservation", back_populates="reservation_assignment")

    def __repr__(self):
        return f"<ReservationAssignment(id_assignment='{self.id_assignment}', status='{self.status}', date_created='{self.date_created}', id_spot='{self.id_spot}', id_reservation='{self.id_reservation}', id_assignment_rate='{self.id_assignment_rate}')>"
    