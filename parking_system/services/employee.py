import math
from sqlalchemy.orm import Session

from data.models.employee import Employee
from schemas.employee import CreateEmployee
from .utils import generate_id, get_hashed_password

class EmployeeService():
    def __init__(self, session: Session):
        self.session = session

    def get_employee(self, id:str):
        employee = self.session.query(Employee).filter(
            Employee.id_employee==id
        ).first()
        return employee

    def get_employee_by_email(self, email: str):
        employee_filter = self.session.query(
            Employee).filter(Employee.email == email.lower())
        return employee_filter.first()
    
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

    def register_employee(self, resgitered_by, employee:CreateEmployee):
        hashed_password = get_hashed_password(employee.password)
        id_employee = generate_id()
        db_employee = Employee(id_employee=id_employee, registered_by = resgitered_by, 
                               id_assignment=employee.id_assignment,name=employee.name, 
                               last_name=employee.last_name, ci=employee.ci, email=employee.email,password=hashed_password,
                                phone=employee.phone, hire_date=employee.hire_date, salary=employee.salary)
        self.session.add(db_employee)
        self.session.commit()
        self.session.refresh(db_employee)
        return db_employee
    