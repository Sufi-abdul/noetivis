
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.auth.deps import current_user

router = APIRouter(prefix="/plugins", tags=["plugins"])

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

class PluginBody(BaseModel):
    tenant_slug: str = "public"
    name: str
    version: str = "0.1.0"
    manifest: dict

@router.post("/register")
def register(body: PluginBody, db: Session = Depends(get_db), user=Depends(current_user)):
    from app.models_phase19 import Plugin
    row = Plugin(tenant_slug=body.tenant_slug, name=body.name, version=body.version, manifest_json=str(body.manifest))
    db.add(row); db.commit(); db.refresh(row)
    return {"registered": True, "id": row.id, "name": row.name}

@router.get("/list")
def list_plugins(tenant_slug: str = "public", db: Session = Depends(get_db)):
    from app.models_phase19 import Plugin
    rows = db.query(Plugin).filter(Plugin.tenant_slug==tenant_slug).order_by(Plugin.created_at.desc()).all()
    return {"count": len(rows), "items": [{"id": r.id, "name": r.name, "version": r.version} for r in rows]}
