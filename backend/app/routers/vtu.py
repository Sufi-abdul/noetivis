
from fastapi import APIRouter, Depends, Request, HTTPException
from pydantic import BaseModel
from app.auth.deps import current_user
from app.security.consent import require_scopes
from app.security.audit_enforce import audit_request
from app.services.vtu.registry import get_vtu

router = APIRouter(prefix="/vtu", tags=["vtu"])

class TopupBody(BaseModel):
    provider: str = "demo_vtu"
    phone: str
    amount: float
    network: str
    metadata: dict = {}

@router.post("/topup")
def topup(body: TopupBody, request: Request, user=Depends(current_user)):
    require_scopes(user, ["vtu:topup"])
    prov = get_vtu(body.provider)
    if not prov:
        raise HTTPException(status_code=400, detail="Unknown VTU provider")
    res = prov.topup(body.phone, body.amount, body.network, body.metadata)
    audit_request(request, actor=user.get("sub","user"), action="vtu.topup", resource=f"vtu:{body.provider}", meta={"amount": body.amount, "network": body.network})
    return res
