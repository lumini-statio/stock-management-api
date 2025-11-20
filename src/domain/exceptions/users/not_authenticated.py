from fastapi import status, HTTPException

class UserNotAuthenticatedError(HTTPException):
    def __init__(
        self,
        status_code=status.HTTP_400_BAD_REQUEST,
        detail: str = 'Usuario no autenticado'
    ):
        self.detail = detail
        self.status_code = status_code