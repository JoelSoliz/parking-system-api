from sqlalchemy import Column, String,  LargeBinary, ForeignKey

from data import Base


class Vihicle(Base):
    __tablename__ = 'vehicle'
    id_vehicle = Column(String(4), primary_key=True)
    license_plate = Column(String(8), nullable=False)
    type_vehicle = Column(String(10), nullable=False)
    color = Column(String(15), nullable=False)
    photo = Column(LargeBinary((2**32)-1))
    id_employee=Column(String(4), ForeignKey('employee.id_employee'))
