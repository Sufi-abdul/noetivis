
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.auth.deps import current_user

router = APIRouter(prefix="/purchase", tags=["purchase"])

class Purchase(BaseModel):
    item_id: str
    value: float
    currency: str = "USD"
    buyer_entity_id: str = "buyer_entity"
    seller_entity_id: str = "seller_entity"

@router.post("/marketplace")
def buy(item: Purchase, user=Depends(current_user)):
    # In production: validate item exists; create order; write to ledger DB
    ledger_event = {
        "entity_id": item.seller_entity_id,
        "amount": item.value,
        "reason": f"marketplace_purchase:{item.item_id}",
        "buyer": user.get("sub")
    }
    return {"purchased": True, "ledger_event_to_record": ledger_event}
