from sqlalchemy.orm import Session, with_polymorphic, joinedload

from data.models import Administrator, Customer, Employee, User


UserPoly = with_polymorphic(User, [Administrator, Customer, Employee])


class UserService:
    def __init__(self, session: Session):
        self.session = session

    def get_user_by_email(self, email: str):
        user_filter = self.session.query(UserPoly).options(
            joinedload(UserPoly.role_info),
            joinedload(UserPoly.user_permissions)).filter(User.email == email.lower()).first()

        return user_filter
