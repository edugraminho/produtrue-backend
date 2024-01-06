from ..database.models import Product
from ..infrastructure.productRepository import ProductRepository


class ProductService:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def get_product(self, name, q):
        return self.product_repository.get_product(name)

    def create_product(self, data: dict) -> Product:
        return self.product_repository.save(data)

    def update_product(self, data: dict, product_id: int) -> Product:
        return self.product_repository.update(data, product_id)
