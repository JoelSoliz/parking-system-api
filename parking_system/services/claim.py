from sqlalchemy.orm import Session, joinedload
from .utils import generate_id


from schemas.claim import ClaimBase
from data.models.claims import Claim
from data.models.customer import Customer


class ClaimService:
    def __init__(self, session: Session):
        self.session = session

    def get_claim_detail(self, id_claim):
        query_claim = self.session.query(Claim).options(
            joinedload(Claim.customer)
        ).filter(Claim.id_claim==id_claim).first()
        return {'claim':query_claim, 'customer':query_claim.customer}
    
    def get_claim_details(self, current_page:int, page_size=20):
        query_claim = self.session.query(Claim).options(
            joinedload(Claim.customer)
        ).filter(Claim.status==False)

        offset_value = (current_page - 1) * page_size
        query = query_claim.limit(page_size).offset(offset_value)
        query_claim = query.all()

        result = [{'claim':{'subject':claim.subject,
                       'registration_date': claim.registration_date},
                       'customer':claim.customer} for claim in query_claim]
        print(result)
        return result

    def register_claim(self, author:str, clain: ClaimBase):
        id_claim = generate_id()
        query_claim = Claim(id_claim=id_claim, subject=clain.subject, 
                            description=clain.description, request=clain.request,
                            author=author)
        
        self.session.add(query_claim)
        self.session.commit()
        self.session.refresh(query_claim)

        return query_claim