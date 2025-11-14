class UserNotAuthenticatedError(Exception):
    def __init__(self):
        super().__init__('Usuario no autenticado')