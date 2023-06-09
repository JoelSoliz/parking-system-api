from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    db_host: str
    db_name: str
    db_password: str
    db_user: str
    jwt_secret_key: str

    email: str
    password: str

    webapp_url: str

    class Config:
        env_file = ".env"


@lru_cache
def get_settings():
    return Settings()
