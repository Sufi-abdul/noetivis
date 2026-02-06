
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.auth.deps import require_role
from app.services.locks import lock_payout
from app.services.payouts_repo import mark_paid

router = APIRouter(prefix="/safe", tags=["safe-pay"])

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@router.post("/mark-paid")
def safe_mark_paid(payout_id: str, db: Session = Depends(get_db), user=Depends(require_role("founder"))):
    ok = lock_payout(db, payout_id)
    if not ok:
        return {"updated": False, "reason": "already_locked_or_paid"}
    row = mark_paid(db, payout_id)
    if not row:
        return {"updated": False, "reason": "payout_not_found"}
    return {"updated": True, "id": row.id, "status": row.status, "paid_at": str(row.paid_at)}
