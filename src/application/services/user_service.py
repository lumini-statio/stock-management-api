from domain.ports.user_repository import UserRepository
from domain.exceptions.users.not_found import UserNotFoundError
from domain.exceptions.users.already_exists import UserAlreadyExistsError
from domain.entities.user import CreateUser, UpdateUser, DeleteUser


class UserService:
    def __init__(self, repository: UserRepository):
        self.repo = repository

    async def all(self):
        return await self.repo.all()
    
    async def get_by_id(self, id: int):
        user_db = await self.repo.get_by_id(id)

        if not user_db:
            raise UserNotFoundError()
        
        return user_db
    
    async def get_by_username(self, username: str):
        user_db = await self.repo.get_by_username(username)

        if not user_db:
            raise UserNotFoundError()
        
        return user_db
    
    async def save(self, user: CreateUser):
        user_db = await self.repo.get_by_username(user.username)

        if user_db:
            raise UserAlreadyExistsError(user.username)
        
        return await self.repo.save(user)
    
    async def update(self, user: UpdateUser):
        user_db = await self.repo.get_by_username(user.username)

        if not user_db:
            raise UserNotFoundError()

        return await self.repo.update(user_db, user)
    
    async def delete(self, user: DeleteUser):
        user_db = await self.repo.get_by_username(user.username)

        if not user_db:
            raise UserNotFoundError()
        
        return await self.repo.delete(user_db)
