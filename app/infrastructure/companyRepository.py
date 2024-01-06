from ..database.models import Company
from sqlalchemy.orm import Session


class CompanyRepository:
    def __init__(self, db: Session):
        self.db = db

    def save(self, company_data: dict) -> Company:
        db_company = Company(**company_data)
        self.db.add(db_company)
        self.db.commit()
        self.db.refresh(db_company)
        return db_company

    def get_company(self, company_name) -> Company:
        company = self.db.query(Company).filter(Company.name == company_name).first()
        return company


    def update(self, company_data: dict, company_id:int) -> Company:
        company = self.db.query(Company).filter(Company.id == company_id).first()
        if company:
            for key, value in company_data.items():
                setattr(company, key, value)
            self.db.commit()
            self.db.refresh(company)
            return company
        return None # type: ignore
        