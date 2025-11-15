from fastapi import APIRouter, Depends, HTTPException, status
from application.services.auth_service import AuthService
from application.services.user_service import UserService
from infrastructure.dependencies import get_auth_service, get_current_user, get_user_service
from infrastructure.schemas import User, Token, CreateUser, UserResponse


auth_router = APIRouter(prefix='/auth', tags=["Auth"])


@auth_router.post('/register/', response_model=UserResponse)
async def register(
    user: CreateUser,
    auth_service: AuthService = Depends(get_auth_service)
):
    print(f'primer log: {user}')
    try:
        new_user: User = await auth_service.register_user(
            email=user.email,
            username=user.username,
            password=user.password
        )

        final_user = UserResponse(
            id=new_user.id,
            email=new_user.email,
            username=new_user.username,
        )

        return final_user
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    

@auth_router.post('/login', response_model=Token)
async def login(
    user: CreateUser,
    auth_service: AuthService = Depends(get_auth_service),
    service: UserService = Depends(get_user_service)
):
    user_db = await service.get_by_username(user.username)

    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username"
        )

    user = await auth_service.authenticate_user(
        user_id=user_db.id,
        password=user.password
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )
    
    access_token = await auth_service.security.create_access_token(data={'sub': str(user.id)})

    return {'access_token': access_token, 'token_type': 'bearer'}


@auth_router.get("/me", response_model=UserResponse)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user