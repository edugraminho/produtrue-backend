from ..database.models import Batch, Company
from sqlalchemy.orm import Session
from ..services.utils import convert_date_to_timestamp
from ..variables import DATE_NOW


class BatchRepository:
    def __init__(self, db: Session):
        self.db = db

    def save(self, batch_data: dict) -> Batch:

        existing_company = (
            self.db.query(Company).filter_by(id=batch_data["company_id"]).first()
        )

        if not existing_company:
            return "Company not found"

        timestamp = convert_date_to_timestamp(batch_data.get("production_date", None))
        timestamp_now = convert_date_to_timestamp(DATE_NOW)

        db_batch = Batch(
            **{
                "name": batch_data.get("name", None),
                "quantity": batch_data.get("quantity", None),
                "production_date": timestamp,
                "registration_date": timestamp_now,
                "level": batch_data.get("level", None),
                "status": True,
                "qrcode_settings": batch_data.get("qrcode_settings", None),
                "notes": batch_data.get("notes", None),
                "company_id": batch_data.get("company_id", None),
                "company": existing_company,
            }
        )

        self.db.add(db_batch)
        self.db.commit()
        self.db.refresh(db_batch)
        return db_batch

    def get_batch(self, _id) -> Batch:
        batch = self.db.query(Batch).filter(Batch.id == _id).first()
        return batch

    def update(self, batch_data: dict, batch_id: int) -> Batch:
        batch = self.db.query(Batch).filter(Batch.id == batch_id).first()
        if batch:
            for key, value in batch_data.items():
                setattr(batch, key, value)
            self.db.commit()
            self.db.refresh(batch)
            return batch
        return None  # type: ignore
