
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app.models_auth import AuthUser

pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(db: Session, email: str, password: str, role: str = "client"):
    u = AuthUser(email=email, password_hash=pwd.hash(password), role=role)
    db.add(u)
    db.commit()
    db.refresh(u)
    return u

def authenticate(db: Session, email: str, password: str):
    u = db.query(AuthUser).filter(AuthUser.email == email).first()
    if not u or not pwd.verify(password, u.password_hash):
        return None
    return u
