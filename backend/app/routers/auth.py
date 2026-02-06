
from fastapi import APIRouter
router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/signup")
def signup(email: str):
    return {"status": "user created", "email": email}
