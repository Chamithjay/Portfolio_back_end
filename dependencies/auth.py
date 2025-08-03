from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from services.token_services import decode_access_token 
from database import get_user_collection
from models.user_model import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_access_token(token)
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except Exception:
        raise credentials_exception

    user = await get_user_collection().find_one({"username": username})
    if user is None:
        raise credentials_exception

    return User(**user)
