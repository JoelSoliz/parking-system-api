from sqlalchemy import Column, String

from data import Base


class Role(Base):
    __tablename__ = 'role'
    id_role = Column(String(4), primary_key=True)
    description = Column(String(50), nullable=False)
