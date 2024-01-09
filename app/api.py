from typing import Union
from fastapi import FastAPI, Depends
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
    product_service = ProductService(ProductRepository(db))
    return product_service.create_product(product_data)


@app.put("/product/{product_id}")
def update_product(product_id: int, product_data: dict, db: Session = Depends(get_db)):
    product_service = ProductService(ProductRepository(db))
    return product_service.update_product(product_data, product_id)


@app.get("/product/{product_name}")
def get_product(
    product_name: str, q: Union[str, None] = None, db: Session = Depends(get_db)
):
    product_service = ProductService(ProductRepository(db))
    product_info = product_service.get_product(product_name, q)
    return {"payload": product_info, "name": product_name, "q": q}


# Batch Product API
@app.post("/batch/add")
def post_batch(data: dict, db: Session = Depends(get_db)):

    batch_service = BatchService(BatchRepository(db))
    response = batch_service.generate_batch_products(
        data=data, ProductSessionDb=ProductRepository(db)
    )

    return response
