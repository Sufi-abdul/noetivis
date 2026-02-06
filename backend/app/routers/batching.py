
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.auth.deps import require_role
from app.models_phase8 import Payout
import uuid, datetime

router = APIRouter(prefix="/batch", tags=["batching"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create")
def create_batch(status: str = "pending", db: Session = Depends(get_db), user=Depends(require_role("founder"))):
    # Group pending payouts by (payee_role, payee_user_id)
    rows = db.query(Payout).filter(Payout.status==status).order_by(Payout.created_at.asc()).all()
    batch_id = str(uuid.uuid4())
    groups = {}
    for r in rows:
        key = (r.payee_role, r.payee_user_id or "POOL")
        groups.setdefault(key, []).append(r)

    summary = []
    for (role, payee), items in groups.items():
        total = round(sum(float(x.amount) for x in items), 6)
        summary.append({"role": role, "payee": payee, "count": len(items), "total": total})

    return {"batch_id": batch_id, "created_at": str(datetime.datetime.utcnow()), "groups": summary, "note": "In production, persist batches to DB and lock payouts."}

@router.get("/receipt")
def receipt(role: str, payee_user_id: str = "POOL", db: Session = Depends(get_db), user=Depends(require_role("founder"))):
    rows = db.query(Payout).filter(Payout.status=="pending", Payout.payee_role==role)
    if payee_user_id != "POOL":
        rows = rows.filter(Payout.payee_user_id==payee_user_id)
    items = rows.order_by(Payout.created_at.asc()).all()
    total = round(sum(float(x.amount) for x in items), 6)
    return {
        "role": role,
        "payee_user_id": payee_user_id,
        "count": len(items),
        "total": total,
        "items": [{"payout_id": x.id, "ledger_id": x.ledger_id, "amount": x.amount, "created_at": str(x.created_at)} for x in items]
    }
