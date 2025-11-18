from pydantic import BaseModel
from typing import List

from src.domain.entities.product import Product

class OrderBase(BaseModel):
    class Meta:
        orm_mode = True


class Order(OrderBase):
    id: int
    purchase_id: int
    number: int
    products: List[Product]
    state: str


class OrderCreate(OrderBase):
    purchase_id: int
    number: int
    products: List[Product]


class OrderUpdate(OrderBase):
    purchase_id: int
    number: int
    products: List[Product]
    state: str


class OrderDelete(OrderBase):
    id: int