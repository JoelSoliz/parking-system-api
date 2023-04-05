from sqlalchemy import Column, String, DateTime, ForeignKey

from data import Base


class Notify(Base):
    __tablename__ = 'notify'
    id_notify = Column(String(4), primary_key=True)
    reques_date = Column(DateTime(), nullable=False)
    id_employee = Column(String(4), ForeignKey('employee.id_employee'))
    id_customer = Column(String(4), ForeignKey('customer.id_customer'))
    