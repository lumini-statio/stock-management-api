from fastapi import status, HTTPException

class UserAlreadyExistsError(HTTPException):
    def __init__(
        self,
        status_code = status.HTTP_400_BAD_REQUEST,
        detail: str = 'User already exists'
    ):
        self.detail = detail
        self.status_code = status_code