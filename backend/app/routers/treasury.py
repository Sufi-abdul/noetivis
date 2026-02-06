
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.auth.deps import require_role
from app.services.treasury import get_pool, add_to_pool, deduct_from_pool

router = APIRouter(prefix="/treasury", tags=["treasury"])

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@router.get("/pool")
def pool(pool: str, currency: str="USD", db: Session = Depends(get_db), user=Depends(require_role("founder"))):
    row = get_pool(db, pool, currency)
    return {"pool": row.pool, "amount": row.amount, "currency": row.currency, "updated_at": str(row.updated_at)}

@router.post("/add")
def add(pool: str, amount: float, currency: str="USD", db: Session = Depends(get_db), user=Depends(require_role("founder"))):
    row = add_to_pool(db, pool, amount, currency)
    return {"updated": True, "pool": row.pool, "amount": row.amount}

@router.post("/deduct")
def deduct(pool: str, amount: float, currency: str="USD", db: Session = Depends(get_db), user=Depends(require_role("founder"))):
    row = deduct_from_pool(db, pool, amount, currency)
    return {"updated": True, "pool": row.pool, "amount": row.amount}
