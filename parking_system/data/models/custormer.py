from sqlalchemy import Column, String, Integer, ForeignKey

from data import Base

class Customer(Base):
    __tablename__ = 'customer'
    id_customer = Column(String(4), primary_key= True)
    name = Column(String(10), nullable=False)
    last_name = Column(String(30), nullable=False)
    ci = Column(Integer, nullable=False)
    email = Column(String(70), nullable=False)
    password = Column(String(20), nullable=False)
    Phone = Column(Integer, nullable=False)
    address = Column(String(50), nullable=False)
    id_parking = Column(String(4), ForeignKey('parking.id_parking'))
    id_administrator = Column(String(4), ForeignKey('administrator.id_administrator'))
    id_asignment = Column(String(4), ForeignKey('assignment_role.id_assignment'))
