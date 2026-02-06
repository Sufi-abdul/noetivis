
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/vault", tags=["vault"])

class VaultItem(BaseModel):
    label: str
    data: str

@router.post("/store")
def store(item: VaultItem):
    return {"stored": True, "label": item.label}

@router.get("/list")
def list_items():
    return {"items": ["demo_record"]}
