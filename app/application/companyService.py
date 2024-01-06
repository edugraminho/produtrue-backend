from ..database.models import Company
from ..infrastructure.companyRepository import CompanyRepository


class CompanyService:
    def __init__(self, company_repository: CompanyRepository):
        self.company_repository = company_repository

    def get_company(self, name, q):
        return self.company_repository.get_company(name)

    def create_company(self, data: dict) -> Company:
        return self.company_repository.save(data)

    def update_company(self, data: dict, company_id: int) -> Company:
        return self.company_repository.update(data, company_id)
