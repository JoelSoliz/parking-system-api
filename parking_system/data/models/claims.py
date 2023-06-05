from datetime import datetime

from sqlalchemy import Column, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from data import Base


class Claim(Base):
    __tablename__ = 'claims'
    id_claim = Column(String(4), primary_key=True)
    subject = Column(String(30), nullable=False)
    description = Column(String(200), nullable=False)
    request = Column(String(125), nullable=False)
    registration_date = Column(DateTime(), default=datetime.now())
    author = Column(String(4), ForeignKey('customer.id_customer'))
    status = Column(Boolean, default=False)
    customer = relationship('Customer', back_populates='claim')

    def __repr__(self):
        return f"Claim(id_claim={self.id_claim}, subject='{self.subject}', description='{self.description}', " \
               f"request='{self.request}', registration_date='{self.registration_date}', author='{self.author}')"