from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
    Numeric,
    JSON,
    Boolean,
    LargeBinary
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)

    def __init__(self, username: str, email: str, id: int = None):
        self.id = id
        self.username = username
        self.email = email


class Batch(Base):
    __tablename__ = "batch"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    quantity = Column(Integer, nullable=False)
    production_date = Column(DateTime, default=datetime.utcnow)
    registration_date = Column(DateTime, default=datetime.utcnow)
    level = Column(Integer)
    status = Column(Boolean, nullable=False)
    qrcode_settings = Column(JSON)
    notes = Column(String(1000))
    company_id = Column(Integer, ForeignKey("company.id"))

    # Relationship
    company = relationship("Company", back_populates="batches")
    products = relationship("Product", back_populates="batch")

    def __init__(
        self,
        name,
        quantity,
        production_date,
        level,
        status,
        qrcode_settings,
        notes,
        company_id,
        company,
    ):
        self.name = name
        self.quantity = quantity
        self.production_date = production_date
        self.registration_date = datetime.utcnow()
        self.level = level
        self.status = status
        self.qrcode_settings = qrcode_settings
        self.notes = notes
        self.company_id = company_id
        self.company = company


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, autoincrement=True)
    token = Column(String(255), unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    status = Column(Boolean, nullable=False)
    description = Column(String(1000))
    url_route = Column(String(255), unique=True)
    price = Column(Numeric(10, 2))
    stock_quantity = Column(Integer)
    manufacturing_date = Column(DateTime)
    expiration_date = Column(DateTime)
    certification = Column(String(100))
    batch_id = Column(Integer, ForeignKey("batch.id"))
    company_id = Column(Integer, ForeignKey("company.id"))
    # supplier_id = Column(Integer, ForeignKey("supplier.id"))
    # category_id = Column(Integer, ForeignKey("category.id"))

    # Relationship
    batch = relationship("Batch", back_populates="products")
    company = relationship("Company", back_populates="products")
    # category = relationship("Category")
    # supplier = relationship("Supplier")

    def __init__(
        self,
        token,
        name,
        status,
        description,
        url_route,
        price,
        stock_quantity,
        manufacturing_date,
        expiration_date,
        nutritional_info,
        certification,
        batch,
        company,
    ):
        self.token = token
        self.name = name
        self.status = status
        self.description = description
        self.url_route = url_route
        self.price = price
        self.stock_quantity = stock_quantity
        self.manufacturing_date = manufacturing_date
        self.expiration_date = expiration_date
        self.nutritional_info = nutritional_info
        self.certification = certification
        self.batch = batch
        self.company = company


class Company(Base):
    __tablename__ = "company"

    id = Column(Integer, primary_key=True, autoincrement=True)
    trade_name = Column(String(255))  # Nome Fantasia
    legal_name = Column(String(255))  # Razão Social
    cnpj = Column(String(18), unique=True, nullable=False)
    address = Column(String(500))
    contact_email = Column(String(255))
    phone_number = Column(String(20))
    website = Column(String(255))

    batches = relationship("Batch", back_populates="company")
    products = relationship("Product", back_populates="company")

    def __init__(
        self,
        trade_name,
        legal_name,
        cnpj,
        address,
        contact_email,
        phone_number,
        website,
    ):
        self.trade_name = trade_name
        self.legal_name = legal_name
        self.cnpj = cnpj
        self.address = address
        self.contact_email = contact_email
        self.phone_number = phone_number
        self.website = website
