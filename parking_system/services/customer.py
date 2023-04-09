import math
from sqlalchemy.orm import Session

from data.models.customer import Customer
from schemas.customer import CreateCustomer
from .utils import generate_id, get_hashed_password

class CustomerService():
    def __init__(self, session: Session):
        self.session = session

    def get_customer_by_email(self, email: str):
        customer_filter = self.session.query(
            Customer).filter(Customer.email == email.lower())
        return customer_filter.first()

    def get_customer(self, id:str):
        customer = self.session.query(Customer).filter(
            Customer.id_customer==id
        ).first()
        return customer

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

    def register_customer(self, resgitered_by, customer:CreateCustomer):
        hashed_password = get_hashed_password(customer.password)
        id_customer = generate_id()
        db_customer = Customer(id_customer=id_customer, registered_by = resgitered_by, 
                               id_assignment=customer.id_assignment,name=customer.name, 
                               last_name=customer.last_name, ci=customer.ci, email=customer.email,password=hashed_password,
                                phone=customer.phone, address=customer.address)
        self.session.add(db_customer)
        self.session.commit()
        self.session.refresh(db_customer)
        return db_customer
    