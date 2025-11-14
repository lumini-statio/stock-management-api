class NotMatchedPasswordError(Exception):
    def __init__(self, username: str):
        super().__init__(f"La contraseña que intenta ingresar para \
                         el usuario '{username}' es incorrecta, intente nuevamente.")