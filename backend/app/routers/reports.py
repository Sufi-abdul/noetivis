
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.auth.deps import require_role
from app.services.payouts_repo import list_payouts

router = APIRouter(prefix="/reports", tags=["reports"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/payouts.csv")
def payouts_csv(status: str | None = None, limit: int = 1000, db: Session = Depends(get_db), user=Depends(require_role("founder"))):
    rows = list_payouts(db, status=status, limit=limit)
    lines = ["payout_id,ledger_id,role,amount,currency,status,created_at,paid_at"]
    for r in rows:
        lines.append(f"{r.id},{r.ledger_id},{r.payee_role},{r.amount},{r.currency},{r.status},{r.created_at},{r.paid_at or ''}")
    return {"filename": "payouts.csv", "csv": "\n".join(lines)}
