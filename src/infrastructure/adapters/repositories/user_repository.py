from sqlalchemy.orm import Session
from typing import Optional

from src.domain.ports.user_repository import UserRepository
from src.infrastructure.adapters.database.models import UserModel
from src.infrastructure.schemas import User, CreateUser, UpdateUser, UserResponse


class SQLUserRepository(UserRepository):
    def __init__(self, db: Session):
        self.db = db
    

    async def all(self):
        users_db = self.db.query(UserModel).all()
        users = [await self._usermodel_to_user_response(user) for user in users_db]
        return users
    

    async def get_by_username(self, username: str) -> Optional[UserModel]:
        usermodel = self.db.query(UserModel).filter(UserModel.username == username).first()

        if not usermodel:
            return None
        
        return usermodel

    
    async def get_by_id(self, used_id: int) -> Optional[User]:
        usermodel = self.db.query(UserModel).filter(UserModel.id == used_id).first()

        if not usermodel:
            return None
        
        return usermodel
    
    async def save(self, user: CreateUser) -> User:
        usermodel = UserModel(
            email=user.email,
            username=user.username,
            password=user.password
        )

        self.db.add(usermodel)
        self.db.commit()
        self.db.refresh(usermodel)

        return await self._usermodel_to_user(usermodel)
    
    async def update(self, usermodel: UserModel, user: UpdateUser) -> Optional[User]:
        user_dump = user.model_dump(exclude_unset=True)

        for key, value in user_dump.items():
            setattr(usermodel, key, value)
        
        self.db.commit()

        return await self._usermodel_to_user(usermodel)
    
    async def delete(self, usermodel: UserModel) -> User:
        self.db.delete(usermodel)
        self.db.commit()

        return await self._usermodel_to_user(usermodel)
    
    @staticmethod
    async def _usermodel_to_user(usermodel: UserModel):
        return User(
            id=usermodel.id,
            email=usermodel.email,
            username=usermodel.username,
            hashed_password=usermodel.password
        )
    
    @staticmethod
    async def _usermodel_to_user_response(usermodel: UserModel):
        return UserResponse(
            id=usermodel.id,
            email=usermodel.email,
            username=usermodel.username,
        )