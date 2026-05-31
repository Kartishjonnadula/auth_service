from sqlalchemy.orm import Session

from app.models.refresh_token import RefreshToken


class RefreshTokenRepository:

    def create(
        self,
        db: Session,
        user_id: int,
        token_hash: str,
        expires_at,
    ):
        refresh_token = RefreshToken(
            user_id=user_id,
            token_hash=token_hash,
            expires_at=expires_at,
        )

        db.add(refresh_token)
        db.commit()
        db.refresh(refresh_token)

        return refresh_token
    def get_by_hash(
        self,
        db: Session,
        token_hash: str,
    ):
        return (
            db.query(RefreshToken)
            .filter(
                RefreshToken.token_hash == token_hash
            )
            .first()
        )
    def delete(
        self,
        db: Session,
        refresh_token: RefreshToken,
    ):
        db.delete(refresh_token)
        db.commit()

    def delete_by_hash(
        self,
        db: Session,
        token_hash: str,
    ):
        session = (
            db.query(RefreshToken)
            .filter(
                RefreshToken.token_hash == token_hash
            )
            .first()
        )

        if not session:
            return

        db.delete(session)
        db.commit()
refresh_token_repository = RefreshTokenRepository()