
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.auth.jwt import create_access_token
from app.services.users_repo import authenticate, create_user

router = APIRouter(prefix="/auth", tags=["auth-db"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Signup(BaseModel):
    email: str
    password: str
    role: str = "client"

class Login(BaseModel):
    email: str
    password: str

@router.post("/signup-db")
def signup_db(body: Signup, db: Session = Depends(get_db)):
    u = create_user(db, body.email, body.password, body.role)
    return {"created": True, "email": u.email, "role": u.role}

@router.post("/login-db")
def login_db(body: Login, db: Session = Depends(get_db)):
    u = authenticate(db, body.email, body.password)
    if not u:
        raise HTTPException(status_code=401, detail="Bad credentials")
    token = create_access_token({"sub": u.email, "role": u.role, "uid": u.id})
    return {"access_token": token, "token_type": "bearer", "role": u.role}
