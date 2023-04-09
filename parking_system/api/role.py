from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, status
from sqlalchemy.orm import Session

from api.dependencies import get_db_session
from schemas.role import RoleBase, RoleCreate
from services.role import RoleService


role_router = APIRouter(prefix='/role')


@role_router.get('/{id}', response_model=RoleBase, tags=['Role'])
def get_role(id, session: Session = Depends(get_db_session)):
    role_service = RoleService(session)
    role = role_service.get_role(id)
    if not role:
        raise HTTPException(
            status_code=404,
            detail=f'role {id} not found'
        )
    return role

@role_router.post('/register', response_model=RoleCreate, tags=["Role"])
def register_role(role: RoleBase = Depends(), session: Session = Depends(get_db_session)):
    role_service = RoleService(session)
    return role_service.register_role(role)