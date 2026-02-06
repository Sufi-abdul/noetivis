
from sqlalchemy.orm import Session
from app.models_phase10 import Treasury
from datetime import datetime

def get_pool(db: Session, pool: str, currency: str="USD"):
    row = db.query(Treasury).filter(Treasury.pool==pool, Treasury.currency==currency).first()
    if not row:
        row = Treasury(pool=pool, amount=0.0, currency=currency, updated_at=datetime.utcnow())
        db.add(row); db.commit(); db.refresh(row)
    return row

def add_to_pool(db: Session, pool: str, amount: float, currency: str="USD"):
    row = get_pool(db, pool, currency)
    row.amount = float(row.amount) + float(amount)
    row.updated_at = datetime.utcnow()
    db.commit(); db.refresh(row)
    return row

def deduct_from_pool(db: Session, pool: str, amount: float, currency: str="USD"):
    row = get_pool(db, pool, currency)
    row.amount = max(0.0, float(row.amount) - float(amount))
    row.updated_at = datetime.utcnow()
    db.commit(); db.refresh(row)
    return row
