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


class DeleteUser(BaseModel):
    username: str

    class Meta:
        orm_mode = True
