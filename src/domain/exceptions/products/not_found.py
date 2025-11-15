from fastapi import HTTPException, status

class ProductNotFoundError(HTTPException):
    def __init__(
        self,
        detail: str = 'No se pudo encontrar el producto con ese identificador.',
        status_code = status.HTTP_404_NOT_FOUND
        ):
        self.detail = detail
        self.status_code = status_code