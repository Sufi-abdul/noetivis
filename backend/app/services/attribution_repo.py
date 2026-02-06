
from sqlalchemy.orm import Session
from app.models_phase8 import Attribution

def set_attribution(db: Session, subject_type: str, subject_id: str, owner_user_id=None, partner_user_id=None, reseller_user_id=None):
    # Upsert naive: delete existing then insert (MVP)
    db.query(Attribution).filter(Attribution.subject_type==subject_type, Attribution.subject_id==subject_id).delete()
    row = Attribution(
        subject_type=subject_type,
        subject_id=subject_id,
        owner_user_id=owner_user_id,
        partner_user_id=partner_user_id,
        reseller_user_id=reseller_user_id
    )
    db.add(row)
    db.commit()
    db.refresh(row)
    return row

def get_attribution(db: Session, subject_type: str, subject_id: str):
    return db.query(Attribution).filter(Attribution.subject_type==subject_type, Attribution.subject_id==subject_id).first()
