
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.auth.deps import current_user
from app.services.wallet import get_wallet

router = APIRouter(prefix="/wallet", tags=["wallet"])

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@router.get("/me")
def my_wallet(currency: str="USD", db: Session = Depends(get_db), user=Depends(current_user)):
    uid = user.get("uid") or user.get("sub")
    w = get_wallet(db, uid, currency=currency)
    return {"user_id": uid, "balance": w.balance, "currency": w.currency, "updated_at": str(w.updated_at)}
