from ..database.models import Product
from sqlalchemy.orm import Session


class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def save(self, product_data: dict) -> Product:
        # TODO fazer um for loop, pegando as informacoes dos produtos

        db_product = Product(**product_data)
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    def get_product(self, product_name) -> Product:
        product = self.db.query(Product).filter(Product.name == product_name).first()
        return product


    def update(self, product_data: dict, product_id:int) -> Product:
        product = self.db.query(Product).filter(Product.id == product_id).first()
        if product:
            for key, value in product_data.items():
                setattr(product, key, value)
            self.db.commit()
            self.db.refresh(product)
            return product
        return None # type: ignore
        