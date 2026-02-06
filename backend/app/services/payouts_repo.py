
from sqlalchemy.orm import Session
from app.models_phase8 import Payout
from datetime import datetime

def create_payout(db: Session, ledger_id: str, payee_role: str, amount: float, currency: str="USD", payee_user_id=None):
    row = Payout(ledger_id=ledger_id, payee_role=payee_role, amount=float(amount), currency=currency, payee_user_id=payee_user_id)
    db.add(row)
    db.commit()
    db.refresh(row)
    return row

def mark_paid(db: Session, payout_id: str):
    row = db.query(Payout).filter(Payout.id==payout_id).first()
    if not row:
        return None
    row.status = "paid"
    row.paid_at = datetime.utcnow()
    db.commit()
    db.refresh(row)
    return row

def list_payouts(db: Session, status: str=None, limit: int=500):
    q = db.query(Payout).order_by(Payout.created_at.desc())
    if status:
        q = q.filter(Payout.status==status)
    return q.limit(limit).all()
