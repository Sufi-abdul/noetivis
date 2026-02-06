
from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = "CHANGE_ME_IN_ENV"
ALGORITHM = "HS256"

def create_access_token(data: dict, minutes: int = 60):
    payload = dict(data)
    payload["exp"] = datetime.utcnow() + timedelta(minutes=minutes)
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
