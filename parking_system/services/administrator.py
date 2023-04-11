from sqlalchemy.orm import Session

from data.models import Administrator
from schemas.administrator import Administrator as AdministratorSchema
from schemas.user import UserCreate
from .constants import ROLES_ID
from .user import UserService
from .utils import generate_id, get_hashed_password

ADMIN_TYPE = 'administrator'


class AdministratorService:
    def __init__(self, session: Session):
        self.session = session
        self.user_service = UserService(session)

    def get_administrator(self, id):
        db_administrator = self.session.query(Administrator).filter(
            Administrator.id_administrator == id)

        return db_administrator

    def get_administrator_by_email(self, email: str):
        user = self.user_service.get_user_by_email(email)
        if isinstance(user, Administrator):
            return AdministratorSchema(**user.__dict__)

        return bool(user)

    def register_administrator(self, user: UserCreate):
        id_user = generate_id()
        hashed_password = get_hashed_password(user.password)
        db_administrator = Administrator(id_user=id_user, id_administrator=id_user, name=user.name,
                                         last_name=user.last_name, ci=user.ci,
                                         email=user.email.lower(), password=hashed_password,
                                         phone=user.phone, role=ROLES_ID.get(ADMIN_TYPE), user_type=ADMIN_TYPE)
        self.session.add(db_administrator)
        self.session.commit()
        self.session.refresh(db_administrator)

        return db_administrator
