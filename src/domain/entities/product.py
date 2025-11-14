from pydantic import BaseModel
from typing import Optional


class ProductBase(BaseModel):
    class Meta:
        orm_mode = True

class Product(ProductBase):
    id: int
    name: str
    description: Optional[str]
    price: str

class ProductCreate(ProductBase):
    name: str
    description: Optional[str]
    price: str

class ProductUpdate(ProductBase):
    name: str
    description: Optional[str]
    price: str

class ProductDelete(ProductBase):
    id: int