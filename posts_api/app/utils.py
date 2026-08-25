from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password):
    hashed_password = pwd_context.hash(password)
    password = hashed_password
    return password

def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)