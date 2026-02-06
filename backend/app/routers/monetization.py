
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Literal, Dict

router = APIRouter(prefix="/monetization", tags=["monetization"])
EventType = Literal["impression","click","conversion","order","refund"]

class MonetizationEvent(BaseModel):
    event_type: EventType
    source: str
    ref_id: str
    value: float = 0.0
    currency: str = "USD"
    metadata: Dict[str, str] = {}

@router.post("/event")
def record_event(evt: MonetizationEvent):
    if evt.source == "affiliate" and evt.event_type == "conversion":
        commission = evt.value * 0.15
    elif evt.source == "adsense_like" and evt.event_type == "click":
        commission = max(0.02, evt.value * 0.05)
    elif evt.source in ["ecommerce","dropship","reseller"] and evt.event_type == "order":
        commission = evt.value * 0.08
    else:
        commission = 0.0
    return {"event": evt.model_dump(), "platform_commission": round(commission, 6)}
