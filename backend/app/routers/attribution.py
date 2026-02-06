
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.auth.deps import require_role, current_user
from app.services.attribution_repo import set_attribution, get_attribution

router = APIRouter(prefix="/attribution", tags=["attribution"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class AttributionBody(BaseModel):
    subject_type: str
    subject_id: str
    owner_user_id: str | None = None
    partner_user_id: str | None = None
    reseller_user_id: str | None = None

@router.post("/set")
def set_attr(body: AttributionBody, db: Session = Depends(get_db), user=Depends(require_role("founder"))):
    row = set_attribution(db, body.subject_type, body.subject_id, body.owner_user_id, body.partner_user_id, body.reseller_user_id)
    return {"set": True, "row": {"subject_type": row.subject_type, "subject_id": row.subject_id}}

@router.get("/get")
def get_attr(subject_type: str, subject_id: str, db: Session = Depends(get_db), user=Depends(current_user)):
    row = get_attribution(db, subject_type, subject_id)
    if not row:
        return {"found": False}
    return {"found": True, "row": {
        "subject_type": row.subject_type,
        "subject_id": row.subject_id,
        "owner_user_id": row.owner_user_id,
        "partner_user_id": row.partner_user_id,
        "reseller_user_id": row.reseller_user_id
    }}
