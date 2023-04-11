from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, status
from sqlalchemy.orm import Session

from api.dependencies import get_db_session, get_current_user
from schemas.role import RoleBase, Role
from schemas.administrator import Administrator
from services.administrator import AdministratorService
from services.role import RoleService


role_router = APIRouter(prefix="/role")


@role_router.get("/{id}", response_model=RoleBase, tags=["Role"])
def get_role(id, session: Session = Depends(get_db_session)):
    role_service = RoleService(session)
    role = role_service.get_role(id)
    if not role:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Role id {id} not found."
        )

    return role


@role_router.get("/", response_model=list[Role], tags=["Role"])
def get_roles(session: Session = Depends(get_db_session)):
    role_service = RoleService(session)
    return role_service.get_roles()


@role_router.post("/", response_model=Role, tags=["Role"])
def register_role(
    role: RoleBase,
    session: Session = Depends(get_db_session),
    administrator: Administrator = Depends(get_current_user),
):
    role_service = RoleService(session)
    administrator_service = AdministratorService(session)
    db_administrator = administrator_service.get_administrator_by_email(administrator.email)
    if isinstance(db_administrator, bool) or not db_administrator:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You don't have permission to register new roles.",
        )

    return role_service.register_role(role)
