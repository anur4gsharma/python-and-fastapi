from jose imoprt jwt, JWTError
from datetime import datetime, timedelta
# SECRET KEY
# Algorithm
# Expiration Time

SECRET_KEY = "hJk0un+LCbyIzl6ZaYpu7iTyETcj+9+N8ajW0sNCy7w="

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()

