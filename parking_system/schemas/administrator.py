from pydantic import BaseModel


class AdministratorBase(BaseModel):
    email: str

class CreateAdministrator(AdministratorBase):
    name: str
    last_name: str
    ci: str
    phone: str
    address: str
    password: str

    class Config:
        orm_mode = True

class Administrator(AdministratorBase):
    id_administrator: str
    name: str
    last_name: str
    
    class Config:
        orm_mode = True

class AdministratorLogin(AdministratorBase):
    password:str

class AdministratorToken(BaseModel):
    access_token: str
    token_type: str
