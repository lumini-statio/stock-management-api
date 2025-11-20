from fastapi import status, HTTPException

class UserNotFoundError(HTTPException):
    def __init__(
        self,
        detail: str = f'No se pudo encontrar el usuario, ingrese un nombre que ya exista.',
        status_code = status.HTTP_404_NOT_FOUND,
        ):
        self.detail = detail
        self.status_code = status_code