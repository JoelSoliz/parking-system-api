from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from data import Base


class Role(Base):
    __tablename__ = 'role'
    id_role = Column(String(4), primary_key=True)
    description = Column(String(50), nullable=False)

    role_permissions = relationship(
        'Permission', secondary='role_permission', back_populates='roles')
    users = relationship('User', back_populates='role_info')
