
from fastapi import APIRouter, Depends, Request
from app.auth.deps import require_role
from app.security.audit_enforce import audit_request

router = APIRouter(prefix="/compliance", tags=["compliance-v2"])

@router.get("/dashboard")
def dashboard(request: Request, user=Depends(require_role("founder"))):
    audit_request(request, actor=user.get("sub","founder"), action="compliance.dashboard", resource="compliance")
    return {"status": "ok", "note": "Compliance dashboard scaffold (declared transactions only)"}

@router.get("/exports/tax.csv")
def export_tax_csv(request: Request, user=Depends(require_role("founder"))):
    audit_request(request, actor=user.get("sub","founder"), action="compliance.export.tax", resource="compliance:tax")
    csv = "date,invoice_id,amount,tax\n"
    return {"filename": "tax.csv", "csv": csv}
