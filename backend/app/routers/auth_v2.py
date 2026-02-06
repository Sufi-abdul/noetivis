
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from passlib.context import CryptContext
from app.auth.jwt import create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])
pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")

USERS = {
  "founder@noetivis.local": {"hash": pwd.hash("founder"), "role":"founder"},
  "partner@noetivis.local": {"hash": pwd.hash("partner"), "role":"partner"},
  "reseller@noetivis.local": {"hash": pwd.hash("reseller"), "role":"reseller"},
}

class Login(BaseModel):
    email: str
    password: str

@router.post("/login")
def login(body: Login):
    u = USERS.get(body.email)
    if not u or not pwd.verify(body.password, u["hash"]):
        raise HTTPException(status_code=401, detail="Bad credentials")
    token = create_access_token({"sub": body.email, "role": u["role"]})
    return {"access_token": token, "token_type": "bearer", "role": u["role"]}
