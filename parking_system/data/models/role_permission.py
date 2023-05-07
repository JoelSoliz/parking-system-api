from sqlalchemy import Column, ForeignKey, String

from data import Base


class RolePermission(Base):
    __tablename__ = 'role_permission'
    id_role_permission = Column(String(4), primary_key=True)
    id_role = Column(String(4), ForeignKey('role.id_role'))
    id_permission = Column(String(4), ForeignKey('permission.id_permission'))
