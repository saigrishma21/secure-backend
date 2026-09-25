import os
from datetime import datetime, timedelta, timezone

from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from jose import jwt
from passlib.context import CryptContext

from dotenv import load_dotenv
load_dotenv()
SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "development-secret-key"
)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


bearer_scheme = HTTPBearer()


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:
    return pwd_context.verify(
        plain_password,
        hashed_password
    )


def create_access_token(
    data: dict,
    expires_minutes: int = ACCESS_TOKEN_EXPIRE_MINUTES
) -> str:

    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=expires_minutes
    )

    to_encode.update({
        "exp": expire
    })

    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )


def verify_token(
    credentials: HTTPAuthorizationCredentials = Depends(
        bearer_scheme
    )
):
    token = credentials.credentials

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload

    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )
def require_admin(
    current_user: dict = Depends(verify_token)
):
    if current_user.get("role") != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

    return current_user