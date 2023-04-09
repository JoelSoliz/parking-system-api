from sqlalchemy.orm import Session

from data.models import Administrator
from schemas.administrator import CreateAdministrator
from .utils import generate_id, get_hashed_password


class AdministratorService:
    def __init__(self, session: Session):
        self.session = session


    def get_administrator_by_email(self, email: str):
        administrator_filter = self.session.query(
        Administrator).filter(Administrator.email == email.lower())
        return administrator_filter.first()

    def register_administrator(self, administrator: CreateAdministrator):
        hashed_password = get_hashed_password(administrator.password)
        id_administrator = generate_id()
        db_administrator = Administrator(id_administrator=id_administrator, name=administrator.name, 
                                         last_name=administrator.last_name,ci=administrator.ci, 
                                         email=administrator.email.lower(), password=hashed_password, 
                                         phone=administrator.phone, address=administrator.address)
        self.session.add(db_administrator)
        self.session.commit()
        self.session.refresh(db_administrator)
        return db_administrator
    
    def get_administrator(self, id):
        db_administrator = self.session.query(Administrator).filter(Administrator.id_administrator==id)
        self.session.add(db_administrator)
        self.session.commit()
        self.session.refresh(db_administrator)

        return db_administrator
