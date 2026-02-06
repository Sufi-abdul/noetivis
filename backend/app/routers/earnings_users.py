
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.auth.deps import current_user, require_role
from app.models_phase8 import Payout

router = APIRouter(prefix="/earnings", tags=["earnings-users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/me")
def my_earnings(status: str = "pending", db: Session = Depends(get_db), user=Depends(current_user)):
    uid = user.get("uid")
    role = user.get("role")
    # founder/contributors pools are handled separately (Phase 10)
    q = db.query(Payout).filter(Payout.status==status)
    if role in ("partner","reseller","client","contributor"):
        q = q.filter(Payout.payee_user_id==uid)
    elif role == "founder":
        # founder can see everything if desired; but here return founder-role payouts only
        q = q.filter(Payout.payee_role=="founder")
    rows = q.order_by(Payout.created_at.desc()).limit(500).all()
    total = sum([float(r.amount) for r in rows])
    return {"user": user.get("sub"), "role": role, "status": status, "total": round(total,6), "count": len(rows),
            "items": [{"id": r.id, "ledger_id": r.ledger_id, "role": r.payee_role, "amount": r.amount, "status": r.status, "created_at": str(r.created_at)} for r in rows]}

@router.get("/founder/overview")
def founder_overview(db: Session = Depends(get_db), user=Depends(require_role("founder"))):
    # totals by role for pending payouts
    roles = ["founder","contributors","partner","reseller","owner"]
    out = {}
    for r in roles:
        out[r] = float(db.query(Payout).filter(Payout.status=="pending", Payout.payee_role==r).with_entities(Payout.amount).all() and 0)
    # compute properly
    for r in roles:
        rows = db.query(Payout).filter(Payout.status=="pending", Payout.payee_role==r).all()
        out[r] = round(sum(float(x.amount) for x in rows), 6)
    return {"pending_totals_by_role": out}
