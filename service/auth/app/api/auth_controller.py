from fastapi import APIRouter
from fastapi import Depends
from app.schemas.auth import RegisterRequest,RefreshRequest,LoginRequest,LogoutRequest
from app.service.auth_service import auth_service
from app.database.dependencies import get_db
from fastapi import HTTPException
from app.auth.dependencies import get_current_user


router = APIRouter()
from fastapi.security import OAuth2PasswordBearer


@router.post("/register")
def register(request: RegisterRequest,db=Depends(get_db)):
    user= auth_service.register(db=db,username=request.username,email=request.email,password=request.password)
    return {
        "id": user.id,
        "username": user.username,
        "email": user.email,
    }


@router.post("/login")
def login(request:LoginRequest,db=Depends(get_db)):
    token=auth_service.login(db=db,email=request.email,password=request.password)
    if not token:
        raise HTTPException(
            status_code=401,
            detail="invalid credentials"
        )
    return token

@router.get("/me")
def get_user(
    current_user=Depends(get_current_user)
):
    return {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email,
    }

@router.post("/refresh")
def refresh(
    request: RefreshRequest,
    db=Depends(get_db),
):
    token = auth_service.refresh_access_token(
        db=db,
        refresh_token=request.refresh_token,
    )

    if not token:
        raise HTTPException(
            status_code=401,
            detail="Invalid refresh token",
        )

    return token

@router.post("/logout")
def logout(
    request: LogoutRequest,
    db=Depends(get_db),
):
    auth_service.logout(
        db=db,
        refresh_token=request.refresh_token,
    )

    return {
        "message": "logged out"
    }