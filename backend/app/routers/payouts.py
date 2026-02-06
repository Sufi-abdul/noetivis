
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import List
from app.auth.deps import require_role
from app.services.payouts import split

router = APIRouter(prefix="/payouts", tags=["payouts"])

class LedgerEvent(BaseModel):
    id: str
    amount: float

@router.post("/run")
def run(events: List[LedgerEvent], user=Depends(require_role("founder"))):
    return {"by": user.get("sub"), "payouts": [{"ledger_id": e.id, "split": split(e.amount)} for e in events]}
