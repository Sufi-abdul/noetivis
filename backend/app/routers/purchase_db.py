
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.auth.deps import current_user
from app.services.ledger_repo import create_ledger
from app.services.splitter import split_default
from app.services.payouts_repo import create_payout

router = APIRouter(prefix="/purchase", tags=["purchase-db"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Purchase(BaseModel):
    item_id: str
    value: float
    currency: str = "USD"
    seller_entity_id: str

@router.post("/marketplace-db")
def marketplace_db(body: Purchase, db: Session = Depends(get_db), user=Depends(current_user)):
    # Write ledger
    led = create_ledger(db, entity_id=body.seller_entity_id, amount=body.value, reason=f"marketplace_purchase:{body.item_id}")
    parts = split_default(led.amount)

    # Persist payouts (payee_user_id wiring happens in Phase 9 with attribution-to-users mapping)
    payout_rows = []
    for role, amt in parts.items():
        if amt <= 0:
            continue
        payout_rows.append(create_payout(db, ledger_id=led.id, payee_role=role, amount=amt, currency=body.currency))

    return {"purchased": True, "ledger_id": led.id, "payouts_created": len(payout_rows)}
