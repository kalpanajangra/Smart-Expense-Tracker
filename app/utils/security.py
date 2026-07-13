from passlib.context import CryptContext
from fastapi import Depends, HTTPException

from jose import JWTError,jwt
from datetime import datetime, timedelta

from fastapi.security import OAuth2PasswordBearer


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

#Hash function
def hash_password(password):
    return pwd_context.hash(password)

#verify function
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(
        plain_password,
        hashed_password
    )

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)

def verify_token(token: str):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        return payload
    except JWTError:
        return None
    
def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        email = payload.get("sub")

        if email is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        return email

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Could not validate credentials"
        )