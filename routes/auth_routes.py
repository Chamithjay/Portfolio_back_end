from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from models.token_model import Token
from services.auth_services import login_user


router = APIRouter()

@router.post("/login", response_model=Token, summary="Login user and return JWT token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return await login_user(form_data)


