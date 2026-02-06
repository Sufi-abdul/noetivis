
from fastapi import APIRouter, Depends, Request
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.auth.deps import current_user
from app.security.consent import require_scopes
from app.security.audit_enforce import audit_request
from app.services.royalties_rules import apply_rule

router = APIRouter(prefix="/royalties", tags=["royalties-v2"])

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

class RoyaltyCompute(BaseModel):
    tenant_slug: str = "public"
    content_type: str
    gross: float

@router.post("/compute")
def compute(body: RoyaltyCompute, request: Request, db: Session = Depends(get_db), user=Depends(current_user)):
    require_scopes(user, ["royalties:compute"])
    # optional tenant rule override
    from app.models_phase19 import RoyaltyRule
    row = db.query(RoyaltyRule).filter(RoyaltyRule.tenant_slug==body.tenant_slug, RoyaltyRule.content_type==body.content_type).first()
    splits = apply_rule(body.content_type, body.gross, row.rule_json if row else None)
    audit_request(request, actor=user.get("sub","user"), action="royalties.compute", resource=f"royalties:{body.content_type}", meta={"gross": body.gross})
    return {"content_type": body.content_type, "gross": body.gross, "splits": splits}
