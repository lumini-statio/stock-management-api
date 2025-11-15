from domain.entities.product import Product, ProductCreate, ProductUpdate, ProductDelete
from domain.exceptions.products.not_found import ProductNotFoundError
from domain.ports.product_repository import ProductRepository
from typing import Optional


class ProductService:
    def __init__(self, repo: ProductRepository):
        self.repo = repo


    async def all(self):
        return await self.repo.all()
    
    
    async def get_by_id(self, product_id: int) -> Optional[Product]:
        product_db = await self.repo.get_by_id(product_id)

        if not product_db:
            raise ProductNotFoundError()
        
        return product_db
    
    
    async def save(self, product: ProductCreate) -> Optional[Product]:
        return await self.repo.save(product)
    
    
    async def update(self, product_id, product_update: ProductUpdate) -> Optional[Product]:
        product_db = await self.get_by_id(product_id)
        
        if not product_db:
            raise ProductNotFoundError()
        
        return await self.repo.update(product_db, product_update)
    
    
    async def delete(self, product: ProductDelete) -> Optional[Product]:
        product_db = await self.get_by_id(product.id)
        
        if not product_db:
            raise ProductNotFoundError()
        
        return await self.repo.delete(product_db)
