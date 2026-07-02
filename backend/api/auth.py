from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Header

from sqlalchemy.orm import Session

from db.database import get_db
from models.user import User
from schemas.user import UserCreate
from core.security import hash_password

from schemas.auth import LoginRequest
from core.security import verify_password
from core.security import create_access_token

from core.dependencies import get_current_user

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/register")
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    existing_user = (
        db.query(User)
        .filter(User.email == user.email)
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    new_user = User(
        email=user.email,
        hashed_password=hash_password(user.password),
        role=user.role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User created successfully",
        "email": new_user.email,
        "role": new_user.role
    }

@router.post("/login")
def login(
    user_credentials: LoginRequest,
    db: Session = Depends(get_db)
):

    user = (
        db.query(User)
        .filter(User.email == user_credentials.email)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    valid_password = verify_password(
        user_credentials.password,
        user.hashed_password
    )

    if not valid_password:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    access_token = create_access_token(
        {
            "sub": user.email,
            "role": user.role
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.get("/me")
def get_me(
    current_user=Depends(get_current_user)
):
    return {
        "email": current_user["sub"],
        "role": current_user["role"]
    }


@router.get("/debug-token")
def debug_token(
    authorization: str = Header(default=None)
):
    return {
        "authorization": authorization
    }
