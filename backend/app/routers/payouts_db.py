
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.auth.deps import require_role
from app.services.payouts_repo import list_payouts, mark_paid

router = APIRouter(prefix="/payouts", tags=["payouts-db"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/list")
def payouts_list(status: str | None = None, limit: int = 200, db: Session = Depends(get_db), user=Depends(require_role("founder"))):
    rows = list_payouts(db, status=status, limit=limit)
    return {"count": len(rows), "items": [
        {"id": r.id, "ledger_id": r.ledger_id, "role": r.payee_role, "amount": r.amount, "status": r.status, "created_at": str(r.created_at)}
        for r in rows
    ]}

@router.post("/mark-paid")
def payouts_mark_paid(payout_id: str, db: Session = Depends(get_db), user=Depends(require_role("founder"))):
    row = mark_paid(db, payout_id)
    if not row:
        return {"updated": False}
    return {"updated": True, "id": row.id, "status": row.status, "paid_at": str(row.paid_at)}
