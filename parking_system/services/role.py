from sqlalchemy.orm import Session

from data.models import Role
from schemas.role import RoleBase
from .utils import generate_id


class RoleService:
    def __init__(self, session: Session):
        self.session = session

    def get_role(self, id_role):
        role = self.session.query(Role).filter(Role.id_role == id_role)
        return role.first()

    def register_role(self, role: RoleBase):
        id_role = generate_id()
        db_role = Role(id_role=id_role, description=role.description)

        self.session.add(db_role)
        self.session.commit()
        self.session.refresh(db_role)
        return db_role
