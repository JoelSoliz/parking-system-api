from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from api.dependencies import get_db_session, get_current_user
from schemas.employee import CreateEmployee, EmployeeBase, EmployeePaginated, Employee
from schemas.user import User
from schemas.administrator import Administrator
from services.employee import EmployeeService
from services.administrator import AdministratorService


employee_router = APIRouter(prefix='/employee')


@employee_router.get("/", response_model=EmployeePaginated, tags=["Employee"])
def get_employees(current_page: int, session: Session = Depends(get_db_session), name=None):
    employee_service = EmployeeService(session)
    results = employee_service.get_employees(current_page, name=name)
    if not results['results']:
        raise HTTPException(status_code=404, detail="No employees found")
    return employee_service.get_employees(current_page, name=name)

@employee_router.get("{id}", response_model=Employee, tags=['Employee'])
def get_employe(id: str, session: Session = Depends(get_db_session)):
    employee_service = EmployeeService(session)
    employee = employee_service.get_employee(id)
    if not employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"posts id {id} not found. ")
    return employee

@employee_router.get("/me", response_model=User, tags=["Employee"])
def get_me(employee: EmployeeBase = Depends(get_current_user)):
    return employee

@employee_router.post('/register', response_model=CreateEmployee, tags=['Employee'])
def register_employee(employee: CreateEmployee = Depends(),
                      session: Session = Depends(get_db_session),
                      administrator: Administrator = Depends(get_current_user)):
    employee_service = EmployeeService(session)
    administrator_service = AdministratorService(session)
    db_administrator = administrator_service.get_administrator_by_email(administrator.email)
    if not db_administrator:
        raise HTTPException(
            status_code=403, detail="Only administrators can register new employee")

    return employee_service.register_employee(administrator.id_administrator, employee)
