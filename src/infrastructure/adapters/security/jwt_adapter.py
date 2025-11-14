from domain.ports.security import SecurityPort
from jose import jwt, JWTError
from datetime import datetime, timedelta
from typing import Optional
import bcrypt


class JWTSecurityAdapter(SecurityPort):
    def __init__(
            self,
            secret_key: str,
            algorithm: str = 'HS256',
            access_token_expire_minutes: int = 30
    ):
        self.secret_key = secret_key
        self.algorithm = algorithm
        self.access_token_expire_minutes = access_token_expire_minutes

    
    async def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(plain_password.encode('utf-8'), 
                              hashed_password.encode('utf-8'))
    

    async def hash_password(self, password):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)

        return hashed.decode('utf-8')
    

    async def create_access_token(self, data: dict):
        to_encode = data.copy()
        expire = datetime.now() + timedelta(minutes=self.access_token_expire_minutes)
        to_encode.update({'exp': expire})
        encoded_jwt = jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)

        return encoded_jwt
    

    async def verify_token(self, token: str) -> Optional[dict]:
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return payload
        except JWTError as e:
            raise e