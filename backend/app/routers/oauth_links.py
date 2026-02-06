
from fastapi import APIRouter, Depends, Request
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.auth.deps import current_user
from app.security.crypto import seal
from app.security.audit_enforce import audit_request

router = APIRouter(prefix="/oauth", tags=["oauth"])

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

class LinkBody(BaseModel):
    provider: str
    provider_user_id: str
    tokens: dict

@router.post("/link")
def link(body: LinkBody, request: Request, db: Session = Depends(get_db), user=Depends(current_user)):
    # Store sealed tokens (placeholder encryption wrapper)
    from app.models_phase19 import OAuthLink
    row = OAuthLink(
        user_id=user.get("uid") or user.get("sub"),
        provider=body.provider,
        provider_user_id=body.provider_user_id,
        encrypted_tokens=seal(str(body.tokens)),
    )
    db.add(row); db.commit(); db.refresh(row)
    audit_request(request, actor=user.get("sub","user"), action="oauth.link", resource=f"oauth:{body.provider}")
    return {"linked": True, "provider": row.provider}
