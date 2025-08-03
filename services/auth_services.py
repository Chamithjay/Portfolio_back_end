from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm
from models.token_model import Token
from database import get_user_collection  # Assume this function retrieves the user collection from the database
from fastapi import HTTPException, status
from services.token_services import create_access_token

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

async def login_user(form_data: OAuth2PasswordRequestForm) -> Token:
    username = form_data.username
    password = form_data.password
    user_collection = get_user_collection()  # Assume this function retrieves the user collection from the database
    user = await user_collection.find_one({"username": form_data.username})
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    hashed_password = user["hashed_password"]
    if not verify_password(password, hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(data={"sub": username})
    return Token(access_token=access_token, token_type="bearer")
