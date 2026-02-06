
from fastapi import Request
from app.security.audit import audit

def audit_request(request: Request, actor: str, action: str, resource: str, meta: dict | None = None):
    audit({
        "actor": actor,
        "action": action,
        "resource": resource,
        "path": str(request.url.path),
        "method": request.method,
        "meta": meta or {}
    })
