
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.auth.deps import require_role

router = APIRouter(prefix="/tenants", tags=["tenants"])

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

class TenantBody(BaseModel):
    slug: str
    name: str
    branding: dict = {}

@router.post("/create")
def create_tenant(body: TenantBody, db: Session = Depends(get_db), user=Depends(require_role("founder"))):
    from app.models_phase19 import Tenant
    row = Tenant(slug=body.slug, name=body.name, branding_json=str(body.branding))
    db.add(row); db.commit(); db.refresh(row)
    return {"created": True, "slug": row.slug}

@router.get("/list")
def list_tenants(db: Session = Depends(get_db), user=Depends(require_role("founder"))):
    from app.models_phase19 import Tenant
    rows = db.query(Tenant).order_by(Tenant.created_at.desc()).all()
    return {"count": len(rows), "items": [{"slug": r.slug, "name": r.name} for r in rows]}
