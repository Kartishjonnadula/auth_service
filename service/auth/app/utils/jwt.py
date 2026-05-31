import jwt

# SECRET_KEY = "some random secret key for now"

# ALGORITHM = "HS256"

# def create_access_token(
#     user_id: int,
# ):
#     payload = {
#         "sub": str(user_id)
#     }

#     return jwt.encode(
#         payload,
#         SECRET_KEY,
#         algorithm=ALGORITHM,
#     )

from datetime import datetime
from datetime import timedelta
from datetime import UTC

with open("keys/private.pem", "r") as f:
    PRIVATE_KEY = f.read()

with open("keys/public.pem", "r") as f:
    PUBLIC_KEY = f.read()


ALGORITHM = "RS256"


def create_access_token(user_id: int):

    now = datetime.now(UTC)

    payload = {
        "sub": str(user_id),
        "iat": now,
        "exp": now + timedelta(minutes=15),
    }

    return jwt.encode(
        payload,
        PRIVATE_KEY,
        algorithm=ALGORITHM,
    )
   

def verify_access_token(token: str):

    return jwt.decode(
        token,
        PUBLIC_KEY,
        algorithms=[ALGORITHM],
    )