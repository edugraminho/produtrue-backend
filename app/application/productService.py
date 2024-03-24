from ..database.models import Product
from ..infrastructure.productRepository import ProductRepository
from ..services.qr_generation import QrCode


class ProductService:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def get_product(self, company, product, token):
        return self.product_repository.get_product(company, product, token)

    def create_product(self, product_data: dict) -> Product:
        return self.product_repository.save(product_data)

    def update_product(self, data: dict, product_id: int) -> Product:
        return self.product_repository.update(data, product_id)
