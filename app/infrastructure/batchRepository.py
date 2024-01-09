from ..database.models import Batch, Company
from sqlalchemy.orm import Session
from ..variables import NOW

class BatchRepository:
    def __init__(self, db: Session):
        self.db = db

    def save(self, batch_data: dict) -> Batch:

        existing_company = (
            self.db.query(Company).filter_by(name=batch_data["company"]).first()
        )

        if not existing_company:
            return "Company not found"

        db_batch = Batch(**{
            "company": existing_company,
            "quantity": batch_data["quantity"],
        })

        self.db.add(db_batch)
        self.db.commit()
        self.db.refresh(db_batch)
        return db_batch

    def get_batch(self, _id) -> Batch:
        batch = self.db.query(Batch).filter(Batch.id == _id).first()
        return batch


    def update(self, batch_data: dict, batch_id:int) -> Batch:
        batch = self.db.query(Batch).filter(Batch.id == batch_id).first()
        if batch:
            for key, value in batch_data.items():
                setattr(batch, key, value)
            self.db.commit()
            self.db.refresh(batch)
            return batch
        return None # type: ignore
        