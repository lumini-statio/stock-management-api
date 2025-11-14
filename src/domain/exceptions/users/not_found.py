class UserNotFoundError(Exception):
    def __init__(self, username: str = ''):
        super.__init__(f'No se pudo encontrar el usuario {username}, ingrese un nombre que ya exista.')