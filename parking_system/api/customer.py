from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from api.dependencies import get_db_session, get_current_user
from schemas.customer import CreateCustomer, CustomerBase, CustomerPaginated, Customer
from schemas.user import User
from schemas.administrator import Administrator
from services.customer import CustomerService
from services.administrator import AdministratorService


customer_router = APIRouter(prefix='/customer')


@customer_router.get("/me", response_model=User, tags=["Customer"])
def get_me(customer: CustomerBase = Depends(get_current_user)):
    return customer


@customer_router.get("{id}", response_model=Customer, tags=['Customer'])
def get_customer(id: str, session: Session = Depends(get_db_session)):
    customer_service = CustomerService(session)
    customer = customer_service.get_customer(id)
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"posts id {id} not found. ")
    return customer


@customer_router.get("/", response_model=CustomerPaginated, tags=["Customer"])
def get_customers(current_page: int, session: Session = Depends(get_db_session), name=None):
    customer_service = CustomerService(session)
    results = customer_service.get_customers(current_page, name=name)
    if not results['results']:
        raise HTTPException(status_code=404, detail="No customers found")
    return customer_service.get_customers(current_page, name=name)


@customer_router.post('/register', response_model=CreateCustomer, tags=['Customer'])
def register_customer(customer: CreateCustomer = Depends(), session: Session = Depends(get_db_session),
                      administrator: Administrator = Depends(get_current_user)):
    customer_service = CustomerService(session)
    administrator_service = AdministratorService(session)
    db_administrator = administrator_service.get_administrator_by_email(administrator.email)
    if not db_administrator:
        raise HTTPException(
            status_code=403, detail="Only administrators can register new customers")

    return customer_service.register_customer(administrator.id_administrator, customer)
