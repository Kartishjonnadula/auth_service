from fastapi import Header
from fastapi import HTTPException

from jwt import ExpiredSignatureError

from app.utils.jwt import verify_access_token


# def get_current_user(
#     authorization: str = Header()
# ):  
#     print("AUTH HEADER:", authorization)
#     if not authorization.startswith("Bearer "):
#         raise HTTPException(
#             status_code=401,
#             detail="Invalid token",
#         )

#     token = authorization.split(" ")[1]

#     try:
#         payload = verify_access_token(token)

#         return payload

#     except ExpiredSignatureError:
#         raise HTTPException(
#             status_code=401,
#             detail="Token expired",
#         )

#     except Exception:
#         raise HTTPException(
#             status_code=401,
#             detail="Invalid token",
#         )

# from typing import Optional

# def get_current_user(
#     authorization: Optional[str] = Header(default=None)
# ):
#     print("AUTH HEADER:", authorization)

#     if authorization is None:
#         raise HTTPException(
#             status_code=401,
#             detail="Missing Authorization Header"
#         )

#     return {"ok": True}

from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from app.repository.user_repository import user_repository
from sqlalchemy.orm import Session
from app.database.dependencies import get_db

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
):
    try:
        payload = verify_access_token(token)

        user_id = int(payload["sub"])

        user = user_repository.get_by_id(
            db=db,
            user_id=user_id,
        )

        if not user:
            raise HTTPException(
                status_code=401,
                detail="User not found",
            )

        return user

    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Invalid token",
        )