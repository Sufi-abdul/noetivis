
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.auth.deps import require_role
from app.models_phase10 import Batch
from app.models_phase8 import Payout
from datetime import datetime
import uuid

router = APIRouter(prefix="/batches", tags=["batches-db"])

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@router.post("/create")
def create(db: Session = Depends(get_db), user=Depends(require_role("founder"))):
    b = Batch()
    db.add(b); db.commit(); db.refresh(b)
    return {"batch_id": b.id, "status": b.status}

@router.post("/lock")
def lock(batch_id: str, db: Session = Depends(get_db), user=Depends(require_role("founder"))):
    b = db.query(Batch).filter(Batch.id==batch_id).first()
    if not b:
        return {"locked": False, "reason": "not_found"}
    b.status = "locked"
    b.locked_at = datetime.utcnow()
    db.commit(); db.refresh(b)
    return {"locked": True, "batch_id": b.id, "status": b.status, "locked_at": str(b.locked_at)}

@router.get("/pending")
def pending(limit: int = 200, db: Session = Depends(get_db), user=Depends(require_role("founder"))):
    rows = db.query(Payout).filter(Payout.status=="pending").order_by(Payout.created_at.asc()).limit(limit).all()
    return {"count": len(rows), "items": [{"id": r.id, "role": r.payee_role, "user_id": r.payee_user_id, "amount": r.amount} for r in rows]}
