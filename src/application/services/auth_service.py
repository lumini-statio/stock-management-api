from domain.ports.security import SecurityPort
from domain.entities.user import User, CreateUser
from domain.exceptions.security.not_match_pw import NotMatchedPasswordError
from domain.exceptions.users.already_exists import UserAlreadyExistsError
from application.services.user_service import UserService
from typing import Optional
from fastapi import HTTPException, status
from jose import JWTError


class AuthService:
    def __init__(self, service: UserService, security: SecurityPort):
        self.service = service
        self.security = security


    async def authenticate_user(self, user_id: int, password: str) -> Optional[User]:
        user = await self.service.get_by_id(user_id)

        if not await self.security.verify_password(password, user.password):
            raise NotMatchedPasswordError(user.username)
        
        return user
    

    async def register_user(self, email: str, username: str, password: str) -> CreateUser:
        existing_user = await self.service.get_by_username(username)
        if existing_user:
            raise UserAlreadyExistsError(existing_user.username)
        
        hashed_password = await self.security.hash_password(password)
        user = CreateUser(email=email, username=username, password=hashed_password)

        return await self.service.save(user)


    async def get_current_user(self, token: str) -> Optional[User]:
        try:
            payload = await self.security.verify_token(token)

            if not payload:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid authentication credentials",
                )
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token",
            )
            
        user_id = payload.get('sub')

        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not founded",
            )
        
        
        return await self.service.get_by_id(user_id)