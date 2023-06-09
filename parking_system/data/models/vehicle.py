from sqlalchemy import Column, String, LargeBinary, ForeignKey

from data import Base


class Vehicle(Base):
    __tablename__ = 'vehicle'
    id_vehicle = Column(String(4), primary_key=True)
    license_plate = Column(String(8), nullable=False)
    vehicle_type = Column(String(10), nullable=False)
    color = Column(String(15), nullable=False)
    photo = Column(LargeBinary((2**32)-1))
    id_customer = Column(String(4), ForeignKey('customer.id_customer'))
