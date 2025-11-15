from abc import ABC, abstractmethod
from typing import Optional, List
from domain.entities.product import Product, ProductCreate, ProductUpdate, ProductDelete


class ProductRepository(ABC):
    @abstractmethod
    async def all(self) -> List[Product]:
        pass

    @abstractmethod
    async def get_by_id(self, product_id: int) -> Optional[Product]:
        pass
    
    @abstractmethod
    async def save(self, product_create: ProductCreate) -> Product:
        pass

    @abstractmethod
    async def update(self, productmodel, product_update: ProductUpdate) -> Optional[Product]:
        pass

    @abstractmethod
    async def delete(self, productmodel) -> Optional[Product]:
        pass
