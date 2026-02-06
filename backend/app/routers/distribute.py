
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.auth.deps import require_role
from app.services.contributor_pool import distribute_contributor_pool

router = APIRouter(prefix="/distribute", tags=["distribute"])

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@router.post("/contributors")
def distribute(db: Session = Depends(get_db), user=Depends(require_role("founder"))):
    return distribute_contributor_pool(db, currency="USD")
