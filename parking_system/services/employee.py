import math
from sqlalchemy.orm import Session

from data.models.employee import Employee
from schemas.employee import CreateEmployee, Employee as EmployeeSchema
from .constants import ROLES_ID
from .user import UserService
from .utils import generate_id, get_hashed_password

EMPLOYEE_TYPE = 'employee'


class EmployeeService():
    def __init__(self, session: Session):
        self.session = session
        self.user_service = UserService(session)

    def get_employee(self, id: str):
        employee = self.session.query(Employee).filter(Employee.id_employee == id).first()
        return employee

    def get_employee_by_email(self, email: str):
        user = self.user_service.get_user_by_email(email)
        if isinstance(user, Employee):
            return EmployeeSchema(**user.__dict__)

        return bool(user)

    def get_employees(self, current_page, page_count=10, name=None):
        result_query = self.session.query(Employee)
        if name:
            result_query = result_query.filter(Employee.name.like(f'%{name}%'))

        results = result_query.order_by(Employee.hire_date.desc()).offset(
            (current_page - 1) * page_count).limit(page_count).all()
        count_data = result_query.count()
        if count_data:
            data = {
                'results': [employee.__dict__ for employee in results],
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

    def register_employee(self, registered_by, user: CreateEmployee):
        id_user = generate_id()
        hashed_password = get_hashed_password(user.password)
        db_employee = Employee(id_user=id_user, id_employee=id_user, name=user.name,
                               last_name=user.last_name, ci=user.ci,
                               email=user.email.lower(), password=hashed_password,
                               phone=user.phone, role=ROLES_ID.get(EMPLOYEE_TYPE), user_type=EMPLOYEE_TYPE,
                               registered_by=registered_by, hire_date=user.hire_date, salary=user.salary)
        self.session.add(db_employee)
        self.session.commit()
        self.session.refresh(db_employee)

        return db_employee
