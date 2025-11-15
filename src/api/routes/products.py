from fastapi import APIRouter, Depends
from typing import List

from application.services.product_service import ProductService
from infrastructure.schemas import Product, ProductCreate, ProductDelete, ProductUpdate
from infrastructure.dependencies import get_product_service


products_router = APIRouter(prefix='', tags=['Products Operations'])

@products_router.get('/products/', response_model=List[Product])
async def products(service: ProductService = Depends(get_product_service)):
    return await service.all()


@products_router.get('/products/{product_id}', response_model=Product)
async def product(product_id: int, service: ProductService = Depends(get_product_service)):
    try:
        return await service.get_by_id(product_id)
    except Exception as e:
        raise e


@products_router.post('/products/', response_model=Product)
async def create_product(product_create: ProductCreate, service: ProductService = Depends(get_product_service)):
    return await service.save(product_create)


@products_router.put('/products/{product_id}', response_model=Product)
async def product(product_id: int, product_update: ProductUpdate, service: ProductService = Depends(get_product_service)):
    return await service.update(product_id, product_update)


@products_router.delete('/products/{product_id}', response_model=Product)
async def product(product_delete: ProductDelete, service: ProductService = Depends(get_product_service)):
    return await service.delete(product_delete)