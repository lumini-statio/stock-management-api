from domain.ports.product_repository import ProductRepository
from infrastructure.schemas import Product, ProductCreate, ProductUpdate, ProductDelete
from infrastructure.adapters.database.models import ProductModel
from sqlalchemy.orm import Session
from typing import Optional, List


class SQLProductRepository(ProductRepository):
    def __init__(self, db: Session):
        self.db = db
    
    
    async def all(self) -> List[Product]:
        products_db = self.db.query(ProductModel).all()
        products = [await self._productmodel_to_product(user) for user in products_db]
        
        return products
    
    
    async def get_by_id(self, product_id: int) -> Optional[Product]:
        productmodel = self.db.query(ProductModel).filter(ProductModel.id == product_id).first()
        
        if not productmodel:
            return None
        
        return productmodel
    
    
    async def save(self, product_create: ProductCreate) -> Product:
        productmodel = ProductModel(
            name=product_create.name,
            description=product_create.description,
            price=product_create.price
        )
        
        self.db.add(productmodel)
        self.db.commit()
        self.db.refresh(productmodel)
        
        return await self._productmodel_to_product(productmodel)
    
    
    async def update(self, productmodel: ProductModel, product_update: ProductUpdate) -> Product:
        model_dump = product_update.model_dump(exclude_unset=True)
        
        for key, value in model_dump.items():
            setattr(productmodel, key, value)
        
        self.db.commit()
        
        return await self._productmodel_to_product(productmodel)
    
    
    async def delete(self, productmodel: ProductModel) -> Product:
        self.db.delete(productmodel)
        self.db.commit()
        
        return await self._productmodel_to_product(productmodel)
    
    
    @staticmethod
    async def _productmodel_to_product(productmodel: ProductModel) -> Product:
        return Product(
            id=productmodel.id,
            name=productmodel.name,
            description=productmodel.description,
            price=productmodel.price
        )