from sqlalchemy.orm import Session

from data.models.administrator import Administrator
from data.models.customer import Customer
from data.models.employee import Employee
from schemas.user import UserLogin
from .utils import create_access_token, verify_password


class AuthenticationService:
    def __init__(self, session: Session):
        self.session = session

    def get_user_by_email(self, email: str):
        administrator = self.session.query(
        Administrator).filter(Administrator.email == email.lower()).first()
        if administrator:
            return administrator
        employee = self.session.query(
            Employee).filter(Employee.email==email.lower()).first()
        if employee:
            return employee
        customer= self.session.query(
            Customer).filter(Customer.email==email.lower()).first()
        if customer:
            return customer
        return None

    def authenticate_user(self, user: UserLogin):
        user_db = self.get_user_by_email(user.email)
        return not (not user_db or not verify_password(user.password, user_db.password))

    def login_session(self, user: UserLogin):
        return {
            "access_token": create_access_token(user.email),
            "token_type": "bearer"
        }
