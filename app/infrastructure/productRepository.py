from ..database.models import Product, Company, Batch
from sqlalchemy.orm import Session


class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def save(self, product_data: dict) -> Product:

        existing_company = (
            self.db.query(Company).filter_by(name=product_data["company"]).first()
        )

        if not existing_company:
            return "Company not found"


        existing_batch = (
            self.db.query(Batch).filter_by(id=product_data["batch_id"]).first()
        )

        if not existing_batch:
            return "Batch not found"
        

        for q in range(data["quantity"]):
            qrcode, token, url = QrCode.generate_qrcode(
                data["company"].lower(),
                data["product"]["name"].lower(),
                data["qrcode_settings"]["version"],
                data["qrcode_settings"]["box_size"],
                data["qrcode_settings"]["border"],
            )


            db_product = Product(**{
                "token" : product_data["token"],
                "name" : product_data["name"],
                "qrcode" : product_data["token"], # TODO Pegar o qrcode gerado
                "description" : product_data["description"],
                "company" : existing_company,
                "batch" : existing_batch,
            })

            self.db.add(db_product)

        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    def get_product(self, product_name) -> Product:
        product = self.db.query(Product).filter(Product.name == product_name).first()
        return product

    def update(self, product_data: dict, product_id: int) -> Product:
        product = self.db.query(Product).filter(Product.id == product_id).first()
        if product:
            for key, value in product_data.items():
                setattr(product, key, value)
            self.db.commit()
            self.db.refresh(product)
            return product
        return None  # type: ignore
