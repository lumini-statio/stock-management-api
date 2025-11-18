from fastapi import FastAPI
from src.api.routes.users import user_router
from src.api.routes.auth import auth_router
from src.api.routes.products import products_router
from src.infrastructure.dependencies import create_db


app = FastAPI(title="Tu API",
    description="API con autenticación",
    version="1.0.0")

create_db()

app.include_router(user_router)
app.include_router(auth_router)
app.include_router(products_router)
