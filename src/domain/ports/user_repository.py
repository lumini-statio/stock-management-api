from abc import ABC, abstractmethod
from typing import Optional, List
from src.domain.entities.user import User, UpdateUser


class UserRepository(ABC):
    @abstractmethod
    async def all(self) -> List[User]:
        pass

    @abstractmethod
    async def get_by_id(self, id: int) -> Optional[User]:
        pass

    @abstractmethod
    async def get_by_username(self, username: str) -> Optional[User]:
        pass

    @abstractmethod
    async def save(self, user: User) -> User:
        pass

    @abstractmethod
    async def update(self, usermodel, user: UpdateUser) -> Optional[User]:
        pass

    @abstractmethod
    async def delete(self, usermodel) -> User:
        pass
