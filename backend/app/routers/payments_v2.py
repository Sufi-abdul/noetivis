
from fastapi import APIRouter, Depends, Request, HTTPException
from pydantic import BaseModel
from app.auth.deps import current_user
from app.security.consent import require_scopes
from app.security.audit_enforce import audit_request
from app.services.gateways.registry import get_gateway

router = APIRouter(prefix="/payments", tags=["payments-v2"])

class ChargeBody(BaseModel):
    gateway: str
    amount: float
    currency: str = "USD"
    metadata: dict = {}

@router.post("/charge-v2")
def charge(body: ChargeBody, request: Request, user=Depends(current_user)):
    require_scopes(user, ["payments:charge"])
    gw = get_gateway(body.gateway)
    if not gw:
        raise HTTPException(status_code=400, detail="Unknown gateway")
    res = gw.charge(body.amount, body.currency, body.metadata)
    audit_request(request, actor=user.get("sub","user"), action="payments.charge", resource=f"gateway:{body.gateway}", meta={"amount": body.amount, "currency": body.currency})
    return res
