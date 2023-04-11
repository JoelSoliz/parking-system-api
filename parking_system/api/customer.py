from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from api.dependencies import get_db_session, get_current_user
from schemas.customer import CustomerPaginated, Customer
from schemas.user import UserCreate
from schemas.administrator import Administrator
from services.customer import CustomerService
from services.administrator import AdministratorService


customer_router = APIRouter(prefix='/customer')


@customer_router.get("/me", response_model=Customer, tags=["Customer"])
def get_me(customer: Customer = Depends(get_current_user)):
    return customer


@customer_router.get("/{id}", response_model=Customer, tags=['Customer'])
def get_customer(id: str, session: Session = Depends(get_db_session), administrator: Administrator = Depends(get_current_user)):
    customer_service = CustomerService(session)
    administrator_service = AdministratorService(session)
    db_administrator = administrator_service.get_administrator_by_email(administrator.email)
    if isinstance(db_administrator, bool) or not db_administrator:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="You don't have permission to find customer id.")

    customer = customer_service.get_customer(id)
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Customer id {id} not found. ")

    return customer


@customer_router.get("/", response_model=CustomerPaginated, tags=["Customer"])
def get_customers(current_page: int, session: Session = Depends(get_db_session),
                  administrator: Administrator = Depends(get_current_user), name=None):
    customer_service = CustomerService(session)
    administrator_service = AdministratorService(session)
    db_administrator = administrator_service.get_administrator_by_email(administrator.email)
    if isinstance(db_administrator, bool) or not db_administrator:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="You don't have permission to list customers.")

    return customer_service.get_customers(current_page, name=name)


@customer_router.post('/', response_model=Customer, tags=['Customer'])
def register_customer(customer: UserCreate = Depends(), session: Session = Depends(get_db_session)):
    customer_service = CustomerService(session)
    db_customer = customer_service.get_customer_by_email(customer.email)
    if db_customer:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Email already registered.")

    return customer_service.register_customer(customer)
