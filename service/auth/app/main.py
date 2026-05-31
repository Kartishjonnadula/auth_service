from fastapi import FastAPI

from app.api.auth_controller import router as auth_router
from app.database.connection import engine
from app.models.base import Base
Base.metadata.create_all(bind=engine)
app = FastAPI(title="ChatFlow Auth Service")

app.include_router(
    auth_router,
    prefix="/auth",
    tags=["auth"]
)