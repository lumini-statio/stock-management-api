from pydantic import BaseModel, EmailStr
from typing import Optional


class User(BaseModel):
    id: int
    email: EmailStr
    username: str
    hashed_password: Optional[str] = None

    class Meta:
        orm_mode = True


class CreateUser(BaseModel):
    email: EmailStr
    username: str
    password: str

    class Meta:
        orm_mode = True


class UpdateUser(BaseModel):
    email: EmailStr
    username: str
    password: str

    class Meta:
        orm_mode = True


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    username: str

    class Meta:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class ProductBase(BaseModel):
    class Meta:
        orm_mode = True

class Product(ProductBase):
    id: int
    name: str
    description: Optional[str]
    price: float


class ProductCreate(ProductBase):
    name: str
    description: Optional[str]
    price: float

class ProductUpdate(ProductBase):
    name: str
    description: Optional[str]
    price: float


class ProductDelete(ProductBase):
    id: int