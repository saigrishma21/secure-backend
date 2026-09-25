from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from ..database import get_db

from ..models import User

from ..schemas import UserCreate, UserLogin

from ..auth import (
    hash_password,
    verify_password,
    create_access_token,
    verify_token,
    require_admin
)


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):
    existing_user = (
        db.query(User)
        .filter(
            (User.username == user_data.username)
            | (User.email == user_data.email)
        )
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Username or email already exists"
        )

    hashed_password = hash_password(
        user_data.password
    )

    new_user = User(
        username=user_data.username,
        email=user_data.email,
        password_hash=hashed_password,
        role="user"
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User registered successfully",
        "username": new_user.username,
        "email": new_user.email,
        "role": new_user.role
    }


@router.post("/login")
def login(
    user_data: UserLogin,
    db: Session = Depends(get_db)
):
    user = (
        db.query(User)
        .filter(User.username == user_data.username)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    if not verify_password(
        user_data.password,
        user.password_hash
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    access_token = create_access_token(
        data={
            "sub": user.username,
            "role": user.role
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.get("/profile")
def profile(
    current_user: dict = Depends(verify_token)
):
    return {
        "message": "You accessed a protected endpoint",
        "username": current_user.get("sub"),
        "role": current_user.get("role")
    }
@router.get("/admin")
def admin_area(
    current_user: dict = Depends(require_admin)
):
    return {
        "message": "Welcome to the admin area",
        "username": current_user.get("sub"),
        "role": current_user.get("role")
    }
@router.post("/make-admin/{username}")
def make_admin(
    username: str,
    db: Session = Depends(get_db)
):
    user = (
        db.query(User)
        .filter(User.username == username)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    user.role = "admin"

    db.commit()
    db.refresh(user)

    return {
        "message": "User promoted to admin",
        "username": user.username,
        "role": user.role
    }