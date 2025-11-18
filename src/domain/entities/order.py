from pydantic import BaseModel
from typing import List

from src.domain.entities.product import Product

class OrderBase(BaseModel):
    class Meta:
        orm_mode = True


class Order(OrderBase):
    id: int
    number: int
    products: List[Product]
    state: str = 'Dispatching'


class OrderCreate(OrderBase):
    number: int
    products: List[Product]
    state: str = 'Dispatching'


class OrderUpdate(OrderBase):
    number: int
    products: List[Product]
    state: str = 'Dispatching'


class OrderDelete(OrderBase):
    id: int