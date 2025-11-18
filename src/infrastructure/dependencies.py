from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from jose import JWTError, jwt

from src.application.services.auth_service import AuthService
from src.application.services.product_service import ProductService
from src.application.services.user_service import UserService

from src.domain.ports.product_repository import ProductRepository
from src.domain.ports.user_repository import UserRepository

from src.infrastructure.adapters.database.db_config import DatabaseConfig
from src.infrastructure.adapters.repositories.product_repository import SQLProductRepository
from src.infrastructure.adapters.repositories.user_repository import SQLUserRepository
from src.infrastructure.adapters.security.jwt_adapter import JWTSecurityAdapter


security = HTTPBearer()
SECRET_KEY = 'my-secret-key'

def get_db_config():
    db = DatabaseConfig('sqlite:///./db.sqlite3')
    return db.get_db()

def create_db():
    db = DatabaseConfig('sqlite:///./db.sqlite3')
    return db.create_database()

def get_auth_service(db: Session = Depends(get_db_config)) -> AuthService:
    user_repository = SQLUserRepository(db)
    security_adapter = JWTSecurityAdapter(
        secret_key=SECRET_KEY)
    
    return AuthService(user_repository, security_adapter)


def get_user_repository(db: Session = Depends(get_db_config)):
    return SQLUserRepository(db)


def get_product_repository(db: Session = Depends(get_db_config)):
    return SQLProductRepository(db)


async def get_user_service(repo: UserRepository = Depends(get_user_repository)):
    return UserService(repo)


async def get_product_service(repo: ProductRepository = Depends(get_product_repository)):
    return ProductService(repo)


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    auth_service: AuthService = Depends(get_auth_service)
):
    token = credentials.credentials
    
    try:
        user: dict = await auth_service.get_current_user(token)
        return user
    except Exception as e:
        raise e
