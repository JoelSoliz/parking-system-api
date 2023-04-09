from sqlalchemy.orm import Session

from data.models import AssignmentRole
from schemas.assignment import AssignmentCreate, AssignmentBase
from .utils import generate_id


class AssignmentService:
    def __init__(self, session: Session):
        self.session = session

    def get_assignment(self, id_assignment):
        assignment = self.session.query(AssignmentRole).filter(
            AssignmentRole.id_assignment == id_assignment
        )
        return assignment.first()
    
    def register_assignment(self, id_role, assignment: AssignmentCreate):
        id_assignment = generate_id()
        db_assignment = AssignmentRole(id_assignment=id_assignment, id_role=id_role, 
                                       assignment_date=assignment.assignment_date)
        self.session.add(db_assignment)
        self.session.commit()   
        self.session.refresh(db_assignment)
        return db_assignment
