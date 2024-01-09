from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
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
    company_id = Column(Integer, ForeignKey("company.id"))
    quantity = Column(Integer, nullable=False)
    registration_date = Column(DateTime, default=datetime.utcnow)

    company = relationship("Company", back_populates="batches")
    products = relationship("Product", back_populates="batch")

    def __init__(self, company, quantity):
        self.company = company
        self.quantity = quantity


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, autoincrement=True)
    token = Column(String(255), unique=True, nullable=False)
    qrcode = Column(String(255), unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(String(1000))
    url_route = Column(String(255), unique=True)
    batch_id = Column(Integer, ForeignKey("batch.id"))
    company_id = Column(Integer, ForeignKey("company.id"))
    
    batch = relationship("Batch", back_populates="products")
    company = relationship("Company", back_populates="products")

    def __init__(self, token, qrcode, name, description, company):
        self.token = token
        self.name = name
        self.qrcode = qrcode
        self.description = description
        self.company = company


class Company(Base):
    __tablename__ = "company"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    cnpj = Column(String(255), unique=True, nullable=False)
    batches = relationship("Batch", back_populates="company")
    products = relationship("Product", back_populates="company")

    def __init__(self, name, cnpj):
        self.name = name
        self.cnpj = cnpj