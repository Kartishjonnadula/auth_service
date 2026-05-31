import bcrypt


def hash_password(password: str) -> str:
    hashed = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )

    return hashed.decode()

def verify_password(
    plain_password: str,
    hashed_password: str,
) -> bool:

    return bcrypt.checkpw(
        plain_password.encode(),
        hashed_password.encode(),
    )