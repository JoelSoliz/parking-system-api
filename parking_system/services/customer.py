import math
from sqlalchemy.orm import Session

from data.models.customer import Customer
from schemas.customer import Customer as CustomerSchema
from schemas.user import UserCreate
from services.user import UserService
from .constants import ROLES_ID
from .utils import generate_id, get_hashed_password


CUSTOMER_TYPE = 'customer'


class CustomerService():
    def __init__(self, session: Session):
        self.session = session
        self.user_service = UserService(session)

    def get_customer(self, id: str):
        customer = self.session.query(Customer).filter(Customer.id_customer == id).first()
        return customer

    def get_customer_by_email(self, email: str):
        user = self.user_service.get_user_by_email(email)
        if isinstance(user, Customer):
            return CustomerSchema(**user.__dict__)

        return bool(user)

    def get_customers(self, current_page, page_count=10, name=None):
        result_query = self.session.query(Customer)

        if name:
            result_query = result_query.filter(Customer.name.like(f'%{name}%'))

        results = result_query.order_by(Customer.created_at.desc()).offset(
            (current_page - 1) * page_count).limit(page_count).all()
        count_data = result_query.count()

        if count_data:
            data = {
                'results': [customer.__dict__ for customer in results],
                'current_page': current_page,
                'total_pages': math.ceil(count_data / page_count),
                'total_elements': count_data,
                'element_per_page': page_count
            }
        else:
            data = {
                'results': [],
                'current_page': 0,
                'total_pages': 0,
                'total_elements': 0,
                'element_per_page': 0
            }

        return data

    def register_customer(self, user: UserCreate):
        id_user = generate_id()
        hashed_password = get_hashed_password(user.password)
        db_customer = Customer(id_user=id_user, id_customer=id_user, name=user.name,
                               last_name=user.last_name, ci=user.ci,
                               email=user.email.lower(), password=hashed_password,
                               phone=user.phone, role=ROLES_ID.get(CUSTOMER_TYPE), user_type=CUSTOMER_TYPE)
        self.session.add(db_customer)
        self.session.commit()
        self.session.refresh(db_customer)

        return db_customer
