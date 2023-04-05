from sqlalchemy import Column, String, DateTime, ForeignKey

from data import Base

class Assignment_role(Base):
    __tablename__ = 'assignment_role'
    id_assignment = Column(String(4), primary_key=True)
    assignmente_date = Column(DateTime(), nullable=False)
    id_role = Column(String(4), ForeignKey('role.id_role'))
    