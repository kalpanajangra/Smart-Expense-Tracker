from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.user import User
from app.schemas.user import UserCreate , UserResponse
from fastapi.security import OAuth2PasswordRequestForm
from app.utils.security import (
    hash_password,
    verify_password,
    create_access_token,
    get_current_user
)

router = APIRouter()

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):

    new_user = User(
        username=user.username,
        email=user.email,
        password=hash_password(user.password)
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return {
        "message": "User Registered Successfully"
    }

@router.post("/login")
def login( form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    db_user = db.query(User).filter(
        User.email == form_data.username
    ).first()

    if db_user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if not verify_password(form_data.password, db_user.password):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    access_token = create_access_token(
        {"sub": db_user.email}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

@router.get("/me", response_model=UserResponse)
def get_me(
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    print(current_user)
    user = db.query(User).filter(
        User.email == current_user
    ).first()

    print(user)

    return user
