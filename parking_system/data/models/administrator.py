from sqlalchemy import Column, String, Integer

from data import Base


class Administrator(Base):
    __tablename__ = 'administrator'
    id_administrator = Column(String(4), primary_key= True)
    name = Column(String(10), nullable=False)
    last_name = Column(String(30), nullable=False)
    ci = Column(Integer, nullable=False)
    email = Column(String(70), nullable=False)
    password = Column(String(20), nullable=False)
    phone = Column(Integer, nullable=False)
    address = Column(String(50), nullable=False)
