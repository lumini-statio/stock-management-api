from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship
from typing import List

Base = declarative_base()


purchase_products = Table(
    'purchase_products',
    Base.metadata,
    Column('purchase_id', Integer, ForeignKey('purchases.id'), primary_key=True),
    Column('product_id', Integer, ForeignKey('products.id'), primary_key=True)
)


class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(100), nullable=False)
    username = Column(String(100), unique=True, nullable=False)
    password = Column(String(200), nullable=False)


class ProductModel(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String(100), nullable=False)
    description = Column(String(500), nullable=False)
    price = Column(Float(asdecimal=True), nullable=False)


class OrderModel(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    state = Column(String(50), nullable=False)
    purchase_id = Column(Integer, ForeignKey('purchases.id'), nullable=False)  # Corregido

class PurchaseModel(Base):
    __tablename__ = 'purchases'
    id = Column(Integer, primary_key=True, autoincrement=True)
    products = relationship('ProductModel', secondary=purchase_products, backref='purchases')