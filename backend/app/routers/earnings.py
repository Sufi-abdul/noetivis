
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import List, Dict
from app.auth.deps import current_user

router = APIRouter(prefix="/earnings", tags=["earnings"])

# MVP: accept ledger events and compute splits. Later: query DB ledger by user/entity.
class LedgerEvent(BaseModel):
    id: str
    amount: float
    entity_id: str
    reason: str = "value_event"

def split(amount: float) -> Dict[str, float]:
    return {
        "founder": round(amount*0.20, 6),
        "contributors": round(amount*0.10, 6),
        "partner": round(amount*0.05, 6),
        "owner": round(amount*0.65, 6),
    }

@router.post("/summary")
def summary(events: List[LedgerEvent], user=Depends(current_user)):
    totals = {"founder":0.0,"contributors":0.0,"partner":0.0,"owner":0.0}
    for e in events:
        parts = split(e.amount)
        for k,v in parts.items():
            totals[k] += float(v)
    return {"by": user.get("sub"), "role": user.get("role"), "totals": {k: round(v,6) for k,v in totals.items()}}
