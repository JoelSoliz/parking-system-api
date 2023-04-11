from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from data import Base


class Permission(Base):
    __tablename__ = 'permission'
    id_permission = Column(String(4), primary_key=True)
    description = Column(String(50), nullable=False)

    roles = relationship('Role', secondary='role_permission', back_populates='role_permissions')
    users = relationship('User', secondary='user_permission', back_populates='user_permissions')
