from sqlalchemy import Column, String, DateTime, ForeignKey

from data import Base


class AssignmentRole(Base):
    __tablename__ = 'assignment_role'
    id_assignment = Column(String(4), primary_key=True)
    assignment_date = Column(DateTime(), nullable=False)
    id_role = Column(String(4), ForeignKey('role.id_role'))
    