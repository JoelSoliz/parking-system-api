from sqlalchemy import Column, ForeignKey, String, Integer

from data import Base


class UserPermission(Base):
    __tablename__ = 'user_permission'
    id_user_permission = Column(String(4), primary_key=True)
    id_user = Column(String(4), ForeignKey('user.id_user'))
    id_permission = Column(String(4), ForeignKey('permission.id_permission'))
