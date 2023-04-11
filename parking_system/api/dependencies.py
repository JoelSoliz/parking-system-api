from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from config import get_settings

from data import Session
from services.user import UserService


def get_db_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")
config = get_settings()


def get_current_user(session: Session = Depends(get_db_session),
                     token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, config.jwt_secret_key,
                             algorithms=["HS256"])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    auth_service = UserService(session)
    user = auth_service.get_user_by_email(email)
    if user is None:
        raise credentials_exception

    return user


def check_user_permission(session: Session = Depends(get_db_session),
                          token: str = Depends(oauth2_scheme),
                          required_role=None,
                          required_permission=None):
    pass
