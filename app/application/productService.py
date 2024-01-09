from ..database.models import Product
from ..infrastructure.productRepository import ProductRepository
from ..services.qr_generation import QrCode


class ProductService:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def get_product(self, name, q):
        return self.product_repository.get_product(name)

    def create_product(self, product_data: dict) -> Product:
        data = {
            "token": token,
            "qrcode": qrcode,
            "name": product_data["name"],
            "description": product_data["description"],
            "company": product_data["company"],
            "url_route": url,
        }

        return self.product_repository.save(data)

    def update_product(self, data: dict, product_id: int) -> Product:
        return self.product_repository.update(data, product_id)