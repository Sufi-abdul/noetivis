
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Literal, Dict

router = APIRouter(prefix="/creators", tags=["creators"])

ContentType = Literal["music","video","photo","writing"]
UsageType = Literal["play","view","read","download","license","share"]

DEFAULT_RATES = {
    "music": {"play": 0.002, "download": 0.05, "license": 25.0},
    "video": {"view": 0.01, "download": 0.10, "license": 50.0},
    "photo": {"view": 0.001, "download": 0.25, "license": 15.0},
    "writing": {"read": 0.005, "download": 0.20, "license": 10.0},
}

class UsageEvent(BaseModel):
    content_id: str
    content_type: ContentType
    usage_type: UsageType
    units: float = 1.0
    metadata: Dict[str, str] = {}

@router.get("/rates")
def get_rates():
    return DEFAULT_RATES

@router.post("/usage")
def register_usage(event: UsageEvent):
    rate = DEFAULT_RATES.get(event.content_type, {}).get(event.usage_type, 0.0)
    gross = float(rate) * float(event.units)
    return {"content_id": event.content_id, "rate": rate, "gross_royalty": gross}
