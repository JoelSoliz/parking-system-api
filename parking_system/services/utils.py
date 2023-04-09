from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from random import choices
from string import ascii_uppercase, digits
from typing import Union, Any

from config import get_settings


settings = get_settings()
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 30
ALGORITHM = "HS256"
JWT_SECRET_KEY = settings.jwt_secret_key

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def generate_id():
    return ''.join(choices(ascii_uppercase + digits, k=4))


def get_hashed_password(password: str) -> str:
    return password_context.hash(password)


def verify_password(password: str, hashed_pass: str) -> bool:
    return password_context.verify(password, hashed_pass)


def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
    return encoded_jwt
