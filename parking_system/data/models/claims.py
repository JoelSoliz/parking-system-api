from sqlalchemy import Column, String, DateTime, ForeignKey

from data import Base


class Claim(Base):
    __tablename__ = 'claims'
    id_claim = Column(String(4), primary_key=True)
    subject = Column(String(20), nullable=False)
    description = Column(String(100), nullable=False)
    request = Column(String(50), nullable=False)
    registration_date = Column(DateTime(), nullable=False)
    author = Column(String(4), ForeignKey('customer.id_customer'))
