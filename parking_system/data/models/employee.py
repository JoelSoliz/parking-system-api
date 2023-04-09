from sqlalchemy import Column, String, DateTime, Float, Integer,ForeignKey

from data import Base


class Employee(Base):
    __tablename__ = 'employee'
    id_employee = Column(String(4), primary_key=True)
    name = Column(String(10), nullable=False)
    last_name = Column(String(30), nullable=False)
    ci = Column(Integer, nullable=False)
    email = Column(String(70), nullable=False)
    password = Column(String(60), nullable=False)
    phone = Column(String(8), nullable=False)
    hire_date = Column(DateTime(), nullable=False)
    salary = Column(Float(precision=5), nullable=False)
    registered_by = Column(String(4), ForeignKey('administrator.id_administrator'))
    id_assignment = Column(String(4), ForeignKey('assignment_role.id_assignment'))
