from fastapi import FastAPI
from api.routes.user_routes import user_router
from api.routes.auth import auth_router
# from infrastructure.dependencies import create_db
from fastapi.security import HTTPBearer

security_scheme = HTTPBearer()

app = FastAPI(title="Tu API",
    description="API con autenticación",
    version="1.0.0")

# create_db()

app.include_router(user_router)
app.include_router(auth_router)
