from fastapi import FastAPI
from api.routes.users import user_router
from api.routes.auth import auth_router
from api.routes.products import products_router
from infrastructure.dependencies import create_db


app = FastAPI(title="Tu API",
    description="API con autenticación",
    version="1.0.0")

create_db()

app.include_router(user_router)
app.include_router(auth_router)
app.include_router(products_router)
