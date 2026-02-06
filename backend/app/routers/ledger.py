
from fastapi import APIRouter
router = APIRouter(prefix="/ledger", tags=["ledger"])

@router.post("/record")
def record(entity_id: str, amount: float, reason: str):
    return {
        "entity": entity_id,
        "amount": amount,
        "reason": reason,
        "commission_split": {
            "founder": amount * 0.20,
            "contributors": amount * 0.10,
            "partner": amount * 0.05,
            "owner": amount * 0.65
        }
    }
