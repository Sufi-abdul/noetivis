
from sqlalchemy.orm import Session
from app.models import Ledger

def create_ledger(db: Session, entity_id: str, amount: float, reason: str):
    row = Ledger(entity_id=entity_id, amount=float(amount), reason=reason)
    db.add(row)
    db.commit()
    db.refresh(row)
    return row

def list_ledger(db: Session, limit: int = 200):
    return db.query(Ledger).order_by(Ledger.created_at.desc()).limit(limit).all()
