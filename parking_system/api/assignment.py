from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.dependencies import get_db_session
from schemas.assignment import AssignmentBase, AssignmentCreate, AssignmentWithRole
from services.assignment import AssignmentService

assignment_router = APIRouter(prefix='/assignment')


@assignment_router.get('/{id}', response_model=AssignmentBase, tags=['Assignment'])
def get_assignment(id, session: Session = Depends(get_db_session)):
    assginment_service = AssignmentService(session)
    assignment = assginment_service.get_assignment(id)
    if not assignment:
        raise HTTPException(
            status_code=404,
            detail=f'assignment {id} not found'
        )
    return assignment


@assignment_router.post('register', response_model=AssignmentCreate, tags=['Assignment'])
def register_assignment(id_role, assignment: AssignmentWithRole = Depends(),
                        session: Session = Depends(get_db_session)):
    assignment_service = AssignmentService(session)
    return assignment_service.register_assignment(id_role, assignment)
