from datetime import datetime
from sqlalchemy import Column, String, DateTime, ForeignKey, Enum

from data import Base


class Notification(Base):
    __tablename__ = 'notification'
    id_notication = Column(String(4), primary_key=True)
    request_date = Column(DateTime(), default=datetime.now())
    id_employee = Column(String(4), ForeignKey('employee.id_employee'))
    id_customer = Column(String(4), ForeignKey('customer.id_customer'))
