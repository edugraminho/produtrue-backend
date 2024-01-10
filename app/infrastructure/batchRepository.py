from ..database.models import Batch, Company
from sqlalchemy.orm import Session
from ..variables import NOW

class BatchRepository:
    def __init__(self, db: Session):
        self.db = db

    def save(self, batch_data: dict) -> Batch:

        existing_company = (
            self.db.query(Company).filter_by(id=batch_data["company_id"]).first()
        )

        if not existing_company:
            return "Company not found"

        db_batch = Batch(**{
            "name": batch_data["name"],
            "quantity": batch_data["quantity"],
            "production_date": "01/01/2024",
            "level": batch_data["level"],
            "status": True,
            "qrcode_settings": batch_data["qrcode_settings"],
            "notes": batch_data["notes"],
            "company_id": batch_data["company_id"],
            "company": existing_company,
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
        