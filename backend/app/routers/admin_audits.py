
from fastapi import APIRouter, Depends
from app.auth.deps import require_role
import os

router = APIRouter(prefix="/admin", tags=["admin-audits"])

@router.get("/audits")
def audits(limit: int = 100, user=Depends(require_role("founder"))):
    path = os.environ.get("NOETIVIS_AUDIT_PATH", "./audit.log")
    if not os.path.exists(path):
        return {"count": 0, "items": []}
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()[-limit:]
    items = [ln.strip() for ln in lines if ln.strip()]
    return {"count": len(items), "items": items}
