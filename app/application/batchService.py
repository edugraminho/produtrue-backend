from ..database.models import Batch
from ..infrastructure.batchRepository import BatchRepository
from ..application.productService import ProductService
from ..services.qr_generation import QrCode
from sqlalchemy.orm import Session


class BatchService:
    def __init__(self, batch_repository: BatchRepository):
        self.batch_repository = batch_repository

    def get_batch(self, name, q):
        return self.batch_repository.get_batch(name)

    def generate_batch_products(self, data: dict) -> Batch:
        return self.batch_repository.save(data)

    def update_batch(self, data: dict, batch_id: int) -> Batch:
        return self.batch_repository.update(data, batch_id)
