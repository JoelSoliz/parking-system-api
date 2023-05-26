from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship

from data import Base


class User(Base):
    __tablename__ = 'user'
    id_user = Column(String(4), primary_key=True)
    name = Column(String(10), nullable=False)
    last_name = Column(String(30), nullable=False)
    ci = Column(Integer, nullable=False)
    email = Column(String(70), nullable=False)
    password = Column(String(60), nullable=False)
    phone = Column(String(8), nullable=False)
    role = Column(String(4), ForeignKey('role.id_role'))
    user_type = Column(String(50), nullable=False)

    role_info = relationship('Role', back_populates='users')
    user_permissions = relationship(
        'Permission', secondary='user_permission', back_populates='users')

    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': user_type
    }

    def __repr__(self):
        return f"User(id_user='{self.id_user}', name='{self.name}', last_name='{self.last_name}', ci='{self.ci}', email='{self.email}', password='{self.password}', phone='{self.phone}', role='{self.role}', user_type='{self.user_type}')"
