from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from application.services.auth_service import AuthService
from application.services.user_service import UserService

from domain.ports.user_repository import UserRepository

from infrastructure.adapters.database.db_config import DatabaseConfig
from infrastructure.adapters.repositories.user_repository import SQLUserRepository
from infrastructure.adapters.security.jwt_adapter import JWTSecurityAdapter


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


async def get_user_service(repo: UserRepository = Depends(get_user_repository)):
    return UserService(repo)

async def get_current_user(
        credentials: HTTPAuthorizationCredentials,
        auth_service: AuthService = Depends(get_auth_service)
):
    token = credentials.credentials
    user = await auth_service.get_current_user(token)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    return user