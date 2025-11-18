from pydantic import BaseModel
from typing import Optional


class ProductBase(BaseModel):
    class Meta:
        orm_mode = True

class Product(ProductBase):
    id: int
    state: str
    name: str
    description: Optional[str]
    price: float

class ProductCreate(ProductBase):
    state: str
    name: str
    description: Optional[str]
    price: float

class ProductUpdate(ProductBase):
    state: str
    name: str
    description: Optional[str]
    price: float

class ProductDelete(ProductBase):
    id: int