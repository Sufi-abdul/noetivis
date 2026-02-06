
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.auth.deps import current_user
from app.services.ledger_repo import list_ledger
from app.services.splitter import split_default

router = APIRouter(prefix="/earnings", tags=["earnings-db"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/summary-db")
def summary_db(limit: int = 200, db: Session = Depends(get_db), user=Depends(current_user)):
    rows = list_ledger(db, limit=limit)
    totals = {"founder":0.0,"contributors":0.0,"partner":0.0,"owner":0.0,"reseller":0.0}
    for r in rows:
        parts = split_default(r.amount)
        for k,v in parts.items():
            totals[k] += float(v)
    return {"by": user.get("sub"), "role": user.get("role"), "limit": limit, "totals": {k: round(v,6) for k,v in totals.items()}}
