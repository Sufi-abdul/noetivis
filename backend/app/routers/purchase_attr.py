
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.auth.deps import current_user
from app.services.ledger_repo import create_ledger
from app.services.attribution_repo import get_attribution
from app.services.payee_resolver import resolve_payees
from app.services.splitter_v2 import split_with_reseller
from app.services.payouts_repo import create_payout

router = APIRouter(prefix="/purchase", tags=["purchase-attr"])

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

@router.post("/marketplace-attr")
def marketplace_attr(body: Purchase, db: Session = Depends(get_db), user=Depends(current_user)):
    # 1) Ledger row
    led = create_ledger(db, entity_id=body.seller_entity_id, amount=body.value, reason=f"marketplace_purchase:{body.item_id}")

    # 2) Attribution for seller entity
    attr = get_attribution(db, "entity", body.seller_entity_id)
    payees = resolve_payees(attr)
    has_reseller = bool(payees.get("reseller_user_id"))

    # 3) Split with reseller support
    parts = split_with_reseller(led.amount, has_reseller=has_reseller)

    # 4) Persist payouts with payee_user_id where applicable
    payout_rows = []
    payout_rows.append(create_payout(db, ledger_id=led.id, payee_role="founder", amount=parts["founder"], currency=body.currency, payee_user_id=None))
    payout_rows.append(create_payout(db, ledger_id=led.id, payee_role="contributors", amount=parts["contributors"], currency=body.currency, payee_user_id=None))

    if parts["partner"] > 0:
        payout_rows.append(create_payout(db, ledger_id=led.id, payee_role="partner", amount=parts["partner"], currency=body.currency, payee_user_id=payees.get("partner_user_id")))

    if parts["reseller"] > 0:
        payout_rows.append(create_payout(db, ledger_id=led.id, payee_role="reseller", amount=parts["reseller"], currency=body.currency, payee_user_id=payees.get("reseller_user_id")))

    if parts["owner"] > 0:
        payout_rows.append(create_payout(db, ledger_id=led.id, payee_role="owner", amount=parts["owner"], currency=body.currency, payee_user_id=payees.get("owner_user_id")))

    return {
        "purchased": True,
        "ledger_id": led.id,
        "attribution_found": bool(attr),
        "split": parts,
        "payouts_created": len(payout_rows),
    }
