from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.dependencies import get_db_session, get_current_user
from schemas.user import UserBase, UserCreate
from schemas.administrator import Administrator
from services.administrator import AdministratorService


administrator_router = APIRouter(prefix='/administrator')


@administrator_router.get("/me", response_model=Administrator, tags=["Administrator"])
def get_me(administrator: Administrator = Depends(get_current_user)):
    return administrator


@administrator_router.post('/register', response_model=Administrator, tags=['Administrator'])
def register_administrator(administrator: UserCreate = Depends(),
                           session: Session = Depends(get_db_session)):
    administrator_service = AdministratorService(session)
    db_administrator = administrator_service.get_administrator_by_email(administrator.email)
    if db_administrator:
        raise HTTPException(status_code=400, detail="Email already registered")

    return administrator_service.register_administrator(administrator)
