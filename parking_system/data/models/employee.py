from sqlalchemy import Column, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship

from .user import User


class Employee(User):
    __tablename__ = 'employee'
    id_user = Column(String(4), ForeignKey('user.id_user'))
    id_employee = Column(String(4), primary_key=True)
    hire_date = Column(DateTime(), nullable=False)
    salary = Column(Float(precision=5), nullable=False)
    registered_by = Column(String(4), ForeignKey('administrator.id_administrator'))

    __mapper_args__ = {
        'polymorphic_identity': 'employee',
    }
