class UserNotFoundError(Exception):
    def __init__(self):
        super.__init__(f'No se pudo encontrar el usuario, ingrese un nombre que ya exista.')