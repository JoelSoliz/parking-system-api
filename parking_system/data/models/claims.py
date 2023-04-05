from sqlalchemy import Column, String, DateTime, ForeignKey

from data import Base

class Claims(Base):
    __tablename__ = 'claims'
    id_claims = Column(String(4), primary_key=True)
    subject = Column(String(20), nullable=False)
    description = Column(String(100), nullable=False)
    request = Column(String(50), nullable=False)
    date_of_resgistration = Column(DateTime(), nullable=False)
    id_customer = Column(String(4), ForeignKey('customer.id_customer'))
    