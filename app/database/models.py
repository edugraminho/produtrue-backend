from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import join, outerjoin, relationship, validates

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)

    def __init__(self, username: str, email: str, id: int = None):  # type: ignore
        self.id = id
        self.username = username
        self.email = email


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, autoincrement=True)
    token = Column(String(255), unique=True, nullable=False)
    qr_code = Column(String(255), unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(String(1000))
    company_id = Column(Integer, ForeignKey("company.id"))

    company = relationship("Company", back_populates="products")

    def __init__(self, token, name, description, company):
        self.token = token
        self.name = name
        self.description = description
        self.company = company


class Company(Base):
    __tablename__ = "company"

    # TODO add mais informacoes da empresa

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    products = relationship("Product", back_populates="company")
