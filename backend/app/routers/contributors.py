
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.auth.deps import require_role
from app.models_phase10 import ContributorAllocation

router = APIRouter(prefix="/contributors", tags=["contributors"])

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

class ContributorBody(BaseModel):
    contributor_user_id: str
    weight: float = 1.0
    active: bool = True

@router.post("/set")
def set_contributor(body: ContributorBody, db: Session = Depends(get_db), user=Depends(require_role("founder"))):
    # Upsert by contributor_user_id
    row = db.query(ContributorAllocation).filter(ContributorAllocation.contributor_user_id==body.contributor_user_id).first()
    if not row:
        row = ContributorAllocation(contributor_user_id=body.contributor_user_id)
        db.add(row)
    row.weight = body.weight
    row.active = body.active
    db.commit(); db.refresh(row)
    return {"saved": True, "contributor_user_id": row.contributor_user_id, "weight": row.weight, "active": row.active}

@router.get("/list")
def list_contributors(db: Session = Depends(get_db), user=Depends(require_role("founder"))):
    rows = db.query(ContributorAllocation).order_by(ContributorAllocation.updated_at.desc()).all()
    return {"count": len(rows), "items": [{"contributor_user_id": r.contributor_user_id, "weight": r.weight, "active": r.active} for r in rows]}
