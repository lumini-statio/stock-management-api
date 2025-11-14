from fastapi import APIRouter, Depends
from typing import List

from application.services.user_service import UserService
from infrastructure.schemas import CreateUser, UserResponse
from infrastructure.dependencies import  get_user_service

user_router = APIRouter(prefix="", tags=["Users Operations"])


@user_router.get('/')
def root():
    return {'message': 'Everything OK!'}

@user_router.get('/users/', response_model=List[UserResponse])
async def users(service: UserService = Depends(get_user_service)):
    users = await service.all()
    return users

@user_router.get('/users/{user_id}')
async def get_user_by_id(user_id: int, service: UserService = Depends(get_user_service)):
    user = await service.get_by_id(user_id)
    return user

@user_router.put('/users/{user_id}')
async def update_user(user_id: int, user: CreateUser, service: UserService = Depends(get_user_service)):
    user = await service.update(user_id, user)

    return user

@user_router.delete('/users/{user_id}')
def delete_user(user_id: int, service: UserService = Depends(get_user_service)):
    user = service.delete(user_id)
    return user