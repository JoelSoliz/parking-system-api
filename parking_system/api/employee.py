from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from api.dependencies import get_db_session, get_current_user
from schemas.administrator import Administrator
from schemas.employee import CreateEmployee, EmployeePaginated, Employee
from services.administrator import AdministratorService
from services.employee import EmployeeService
from data.models.employee import Employee as Employ


employee_router = APIRouter(prefix="/employee")


@employee_router.get("/me", response_model=Employee, tags=["Employee"])
def get_me(employee: Employee = Depends(get_current_user)):
    return employee


@employee_router.get("/{id}", response_model=Employee, tags=["Employee"])
def get_employee(
    id: str,
    session: Session = Depends(get_db_session),
    administrator: Administrator = Depends(get_current_user),
):
    employee_service = EmployeeService(session)
    administrator_service = AdministratorService(session)
    db_administrator = administrator_service.get_administrator_by_email(administrator.email)
    if isinstance(db_administrator, bool) or not db_administrator:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You don't have permission to find employee id.",
        )

    employee = employee_service.get_employee(id)
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Employee id {id} not found."
        )

    return employee


@employee_router.get("/", response_model=EmployeePaginated, tags=["Employee"])
def get_employees(
    current_page: int,
    session: Session = Depends(get_db_session),
    administrator: Administrator = Depends(get_current_user),
    name=None,
):
    employee_service = EmployeeService(session)
    administrator_service = AdministratorService(session)
    db_administrator = administrator_service.get_administrator_by_email(administrator.email)
    if isinstance(db_administrator, bool) or not db_administrator:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You don't have permission to list employees.",
        )

    return employee_service.get_employees(current_page, name=name)


@employee_router.post("/", response_model=CreateEmployee, tags=["Employee"])
def register_employee(
    employee: CreateEmployee,
    session: Session = Depends(get_db_session),
    administrator: Administrator = Depends(get_current_user),
):
    employee_service = EmployeeService(session)
    administrator_service = AdministratorService(session)
    db_administrator = administrator_service.get_administrator_by_email(administrator.email)
    if isinstance(db_administrator, bool) or not db_administrator:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You don't have permission to register new employees.",
        )

    db_employee = employee_service.get_employee_by_email(employee.email)
    if db_employee:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered."
        )

    return employee_service.register_employee(administrator.id_administrator, employee)
