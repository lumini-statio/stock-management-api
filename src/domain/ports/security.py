from abc import ABC, abstractmethod


class SecurityPort(ABC):
    @abstractmethod
    async def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        pass

    @abstractmethod
    async def hash_password(self, password: str) -> str:
        pass

    @abstractmethod
    async def create_access_token(self, data: dict) -> str:
        pass

    @abstractmethod
    async def verify_token(self, token: str) -> dict:
        pass