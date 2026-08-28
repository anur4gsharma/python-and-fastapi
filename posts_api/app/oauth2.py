from jose import jwt, JWTError
from datetime import datetime, timedelta
from config import settings

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=settings.access_token_expire_minutes)
    to_encode.update({"exp": expire})

    jwt.encode(to_encode, settings.secret_key, settings.algorithm)