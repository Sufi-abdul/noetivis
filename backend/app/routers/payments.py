
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/payments", tags=["payments"])

class PaymentRequest(BaseModel):
    gateway: str
    amount: float
    currency: str = "USD"

@router.post("/charge")
def charge(req: PaymentRequest):
    return {
        "gateway": req.gateway,
        "status": "simulated_success",
        "amount": req.amount
    }
