
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.auth.deps import require_role
from app.models_phase20 import WalletTxn

router = APIRouter(prefix="/reconcile", tags=["reconcile"])

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@router.get("/wallet-txns")
def wallet_txns(limit: int = 200, db: Session = Depends(get_db), user=Depends(require_role("founder"))):
    rows = db.query(WalletTxn).order_by(WalletTxn.created_at.desc()).limit(limit).all()
    return {"count": len(rows), "items": [
        {"id": r.id, "wallet_id": r.wallet_id, "dir": r.direction, "amount": r.amount, "currency": r.currency,
         "provider": r.provider, "provider_ref": r.provider_ref, "status": r.status, "created_at": str(r.created_at)}
        for r in rows
    ]}
