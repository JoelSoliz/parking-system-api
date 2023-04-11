from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from api.dependencies import get_db_session
from schemas.user import UserLogin, UserToken
from services.auth import AuthenticationService


auth_router = APIRouter(prefix='/auth')


@auth_router.post('/login', response_model=UserToken, tags=["User"])
def login_user(user: UserLogin, session: Session = Depends(get_db_session)):
    auth_service = AuthenticationService(session)
    if not auth_service.authenticate_user(user):
        raise HTTPException(
            status_code=400, detail="Incorrect email or password.")

    return auth_service.login_session(user)


@auth_router.post('/token', response_model=UserToken, tags=["User"])
def login_oauth(user: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_db_session)):
    auth_service = AuthenticationService(session)
    user = UserLogin(email=user.username, password=user.password)
    if not auth_service.authenticate_user(user):
        raise HTTPException(
            status_code=400, detail="Incorrect email or password.")

    return auth_service.login_session(user)
