from typing import Union

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from api.dependencies import get_current_user, get_db_session
from schemas.claim import ClaimBase, Claim, ClaimWithCustomer, ClaimPaginated
from services.claim import ClaimService
from data.models.customer import Customer
from data.models.employee import Employee
from data.models.administrator import Administrator


claim_router = APIRouter(prefix="/claim")

@claim_router.get("/{id}", response_model=ClaimWithCustomer, tags=["Claim"])
def get_claim_detail(id:str, session:Session=Depends(get_db_session),
                     user:Union[Employee, Administrator]=Depends(get_current_user)):
    claim_service = ClaimService(session)
    if not isinstance(user, Administrator) and not isinstance(user, Employee):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You don't have permission to see claim.",
        )

    return claim_service.get_claim_detail(id)

@claim_router.get("/", response_model=ClaimPaginated, tags=["Claim"])
def get_claim_details(current_page:int, session:Session=Depends(get_db_session),
                     user:Union[Employee, Administrator]=Depends(get_current_user)):
    claim_service = ClaimService(session)

    if not isinstance(user, Administrator) and not isinstance(user, Employee):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You don't have permission to see claims.",
        )
    
    return claim_service.get_claim_details(current_page)

@claim_router.post("/", response_model=Claim, tags=["Claim"])
def register_claim(claim:ClaimBase, session: Session=Depends(get_db_session), 
                   user: Customer=Depends(get_current_user)):
    claim_service = ClaimService(session)

    if not isinstance(user, Customer):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You don't have permission to make claims.",
        )

    return claim_service.register_claim(user.id_customer, claim)
