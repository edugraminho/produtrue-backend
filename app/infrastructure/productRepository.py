from sqlalchemy import func
from sqlalchemy.orm import Session
from ..database.models import Product, Company, Batch
from ..services.qr_generation import QrCode
from ..services.token_generation import Token
from ..services.utils import convert_date_to_timestamp


class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def save(self, product_data: dict) -> Product:
        company_data = (
            self.db.query(Company).filter_by(id=product_data["company_id"]).first()
        )
        if not company_data:
            return "Company not found"

        batch_data = self.db.query(Batch).filter_by(id=product_data["batch_id"]).first()
        if not batch_data:
            return "Batch not found"

        existing_products_count = (
            self.db.query(func.count(Product.id))
            .filter_by(batch_id=batch_data.id)
            .scalar()
        )

        remaining_quantity = batch_data.quantity - existing_products_count

        product_list = []

        for i in range(remaining_quantity):
            token, url = Token().token_generator(
                company_data.trade_name,
                product_data["name"],
            )

            manufacturing_timestamp = convert_date_to_timestamp(
                product_data.get("manufacturing_date", None)
            )
            expiration_date = product_data.get("expiration_date", None)

            if expiration_date:
                expiration_timestamp = convert_date_to_timestamp(expiration_date)
            else:
                expiration_timestamp = None

            db_product = Product(
                **{
                    "token": token,
                    "name": product_data["name"],
                    "status": True,
                    "description": product_data["description"],
                    "url_route": url,
                    "price": product_data.get("price", None),
                    "stock_quantity": product_data.get("stock_quantity", None),
                    "manufacturing_date": manufacturing_timestamp,
                    "nutritional_info": product_data.get("nutritional_info", None),
                    "expiration_date": expiration_timestamp,
                    "certification": product_data.get("certification", None),
                    "views_count": product_data.get("views_count", None),
                    "viewing_date": product_data.get("viewing_date", None),
                    "batch": batch_data,
                    "company": company_data,
                }
            )

            product_list.append(db_product)

        self.db.add_all(product_list)
        self.db.commit()

        return {
            "Status": "OK",
            "Product": {
                "inserted_products": remaining_quantity,
                "name": product_data["name"],
                "batch_id": batch_data.id,
                "batch_name": batch_data.name,
                "company_id": company_data.id,
                "company_name": company_data.trade_name,
            },
        }

    def get_product(self, company, product_name, token) -> Product:
        product = self.db.query(Product).filter(Product.token == token).first()

        company = (
            self.db.query(Company).filter(Company.id == product.company_id).first()
        )

        product.company_name = company.trade_name
        product.company_website = company.website

        return product

    def update(self, product_data: dict, product_id: int) -> Product:
        product = self.db.query(Product).filter(Product.id == product_id).first()
        if product:
            for key, value in product_data.items():
                setattr(product, key, value)
            self.db.commit()
            self.db.refresh(product)
            return product
        return None
