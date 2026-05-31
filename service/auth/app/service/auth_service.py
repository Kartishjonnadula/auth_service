from sqlalchemy.orm import Session

from app.repository.user_repository import user_repository
from app.utils.password_utils import hash_password,verify_password
from app.utils.jwt import create_access_token
from app.utils.refresh_token import (
    generate_refresh_token,
    hash_refresh_token,
)

from app.repository.refresh_token_repository import (
    refresh_token_repository,
)
from datetime import datetime,timedelta,UTC


class AuthService:

    def register(
        self,
        db: Session,
        username: str,
        email: str,
        password: str,
    ):
        password_hash=hash_password(password)
        return user_repository.create_user(
            db=db,
            username=username,
            email=email,
            password_hash=password_hash,
        )
        
    def login(
        self,
        db,
        email,
        password,
    ):
        user = user_repository.get_by_email(
            db=db,
            email=email,
        )

        if not user:
            return None
        
        if not verify_password(
            password,
            user.password_hash,
        ):
            return None

        access_token=create_access_token(user_id=user.id)
        refresh_token = generate_refresh_token()
        refresh_token_hash=hash_refresh_token(refresh_token)
        expires_at = (datetime.now(UTC)+ timedelta(days=7)
)
        refresh_token_repository.create(db=db,user_id=user.id,token_hash=refresh_token_hash,expires_at=expires_at)
        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
        }


    def refresh_access_token(
        self,
        db,
        refresh_token: str,
    ):
        token_hash = hash_refresh_token(
            refresh_token
        )

        refresh_session = (
            refresh_token_repository.get_by_hash(
                db=db,
                token_hash=token_hash,
            )
        )

        if not refresh_session:
            return None
  
        if refresh_session.expires_at < datetime.now(UTC):
            return None
        new_refresh_token = generate_refresh_token()
        new_refresh_token_hash = hash_refresh_token(new_refresh_token)
        new_session = (
            refresh_token_repository.create(
                db=db,
                user_id=refresh_session.user_id,
                token_hash=new_refresh_token_hash,
                expires_at=datetime.now(UTC)
                + timedelta(days=7),
            )
        )
        refresh_token_repository.delete(
            db=db,
            refresh_token=refresh_session,
        )
        access_token = create_access_token(
            refresh_session.user_id
        )

        return {
        "access_token": access_token,
        "refresh_token": new_refresh_token,
        }
    
    def logout(
        self,
        db,
        refresh_token: str,
    ):
        token_hash = hash_refresh_token(
            refresh_token
        )

        refresh_token_repository.delete_by_hash(
            db=db,
            token_hash=token_hash,
        )
auth_service = AuthService()