from fastapi import HTTPException, status
from config import STATIC_TOKEN
def authenticate(token: str):
    if token != STATIC_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )
    return token
