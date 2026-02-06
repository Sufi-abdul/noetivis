
from sqlalchemy.orm import Session
from app.models_phase10 import PayoutLock

def lock_payout(db: Session, payout_id: str):
    existing = db.query(PayoutLock).filter(PayoutLock.payout_id==payout_id).first()
    if existing:
        return False
    row = PayoutLock(payout_id=payout_id, locked=True)
    db.add(row); db.commit()
    return True
