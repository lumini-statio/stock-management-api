class UserAlreadyExistsError(Exception):
    def __init__(self, username: str):
        super().__init__(f'El usuario {username} ya existe, elija otro nombre.')