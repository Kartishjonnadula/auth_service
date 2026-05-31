from sqlalchemy import create_engine,text
from sqlalchemy.orm import sessionmaker
DATABASE_URL = (
    "postgresql://keycloak:password@localhost:5432/chatflow"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
def test_connection():
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT 1")
        )

        print(result.scalar())