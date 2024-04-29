from typing import Union
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from .database.db_connection import get_db

from .application.userService import UserService
from .application.companyService import CompanyService
from .application.productService import ProductService
from .application.batchService import BatchService

from .infrastructure.userRepository import UserRepository
from .infrastructure.companyRepository import CompanyRepository
from .infrastructure.productRepository import ProductRepository
from .infrastructure.batchRepository import BatchRepository

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def get_health_check():
    return {"message": "Service up and running"}


@app.post("/users/add")
def create_user(user_data: dict, db: Session = Depends(get_db)):
    user_service = UserService(UserRepository(db))
    return user_service.create_user(user_data)


@app.put("/users/{user_id}")
def update_user(user_id: int, user_data: dict, db: Session = Depends(get_db)):
    user_service = UserService(UserRepository(db))
    return user_service.update_user(user_data, user_id)


@app.get("/users/{user_id}")
def get_user(user_id: int, q: Union[str, None] = None, db: Session = Depends(get_db)):
    user_service = UserService(UserRepository(db))
    user_info = user_service.get_tweet(user_id, q)
    return {"payload": user_info, "item_id": user_id, "q": q}


# Company API
@app.post("/company/add")
def post_company(company_data: dict, db: Session = Depends(get_db)):
    """
    Endpoint to add a new company.
    JSON:
        {
            "trade_name": "Company LTDA",
            "legal_name": "Company",
            "cnpj": "12.345.678/0001-11",
            "address": "Company address",
            "contact_email": "email@company.com",
            "phone_number": "123456789",
            "website": "http://www.company.com"
        }
    """
    company_service = CompanyService(CompanyRepository(db))
    return company_service.create_company(company_data)


@app.put("/company/{company_id}")
def update_company(company_id: int, company_data: dict, db: Session = Depends(get_db)):
    company_service = CompanyService(CompanyRepository(db))
    return company_service.update_company(company_data, company_id)


@app.get("/company/{company_name}")
def get_company(
    company_name: str, q: Union[str, None] = None, db: Session = Depends(get_db)
):
    company_service = CompanyService(CompanyRepository(db))
    company_info = company_service.get_company(company_name, q)
    return {"payload": company_info, "name": company_name, "q": q}


# Product API
@app.post("/product/add")
def post_product(product_data: dict, db: Session = Depends(get_db)):
    """
    Endpoint to add a new product.
    JSON:
        {
            "name": "Product Name",
            "description": "Product description",
            "price": 19.99,
            "stock_quantity": 100,
            "manufacturing_date": "2024-01-06T12:00:00",
            "expiration_date": "",
            "nutritional_info": "Nutritional information",
            "certification": "Product certification",
            "views_count": 0,
            "viewing_date" : "2022-01-01T00:00:00",
            "batch_id": 1,
            "company_id": 1
        }
    """
    product_service = ProductService(ProductRepository(db))
    return product_service.create_product(product_data)


@app.patch("/product/{product_id}")
def update_product(product_id: int, product_data: dict, db: Session = Depends(get_db)):
    product_service = ProductService(ProductRepository(db))
    return product_service.update_product(product_data, product_id)


@app.get("/{company}/{product}/{token}")
def get_product(
    company: str,
    product: str,
    token: str,
    q: Union[str, None] = None,
    db: Session = Depends(get_db),
):
    """
    [
        {
            "id": 36,
            "name": "Whey",
            "description": "Whey description",
            "price": 101.99,
            "manufacturing_date": "2022-01-01T00:00:00",
            "certification": "Product certification",
            "batch_id": 5,
            "token": "PCXqur1qihAd1iaJ1vqoby6D1yoq1g",
            "status": true,
            "url_route": "",
            "stock_quantity": 100,
            "expiration_date": "2030-12-31T00:00:00",
            "company_id": 1
        }
    ]
    """
    product_service = ProductService(ProductRepository(db))

    product_info = product_service.get_product(company, product, token)

    return {product_info}


# Batch Product API
@app.post("/batch/add")
def post_batch(data: dict, db: Session = Depends(get_db)):
    """
    Endpoint to add a new batch and generate associated products.

    JSON:
        {
            "name": "Batch Name",
            "quantity": 100,
            "level": 1,
            "qrcode_settings": {
                "version": 1,
                "box_size": 5,
                "border": 10,
                "fill_color": "white",
                "back_color": "black"
            },
            "notes": "Additional notes",
            "company_id": 1
        }
    """

    batch_service = BatchService(BatchRepository(db))
    return batch_service.generate_batch_products(data=data)
