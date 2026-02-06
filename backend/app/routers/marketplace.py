
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Literal, Dict, List
from app.auth.deps import current_user

router = APIRouter(prefix="/marketplace", tags=["marketplace"])

ItemType = Literal["plugin","model","dataset","theme","service"]

class Item(BaseModel):
    item_id: str
    type: ItemType
    title: str
    price: float = 0.0
    currency: str = "USD"
    metadata: Dict[str, str] = {}

STORE: List[Item] = []

@router.post("/list")
def list_item(item: Item, user=Depends(current_user)):
    STORE.append(item)
    return {"listed": True, "by": user.get("sub"), "count": len(STORE)}

@router.get("/browse")
def browse():
    return {"items": [i.model_dump() for i in STORE]}
