from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from .user import User


class Administrator(User):
    __tablename__ = 'administrator'
    id_administrator = Column(String(4), primary_key=True)
    id_user = Column(String(4), ForeignKey('user.id_user'))

    __mapper_args__ = {
        'polymorphic_identity': 'administrator',
    }
