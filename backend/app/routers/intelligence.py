
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict, Literal
from app.services.agents import run_agents
from app.services.index import compute_index

router = APIRouter(prefix="/intelligence", tags=["intelligence"])
Sector = Literal["finance","education","government","media","technology","health"]

class Signal(BaseModel):
    sector: Sector
    source: str
    payload: Dict

@router.post("/signal")
def ingest_signal(sig: Signal):
    actions = run_agents(sig.sector, sig.payload)
    idx = compute_index({
        "signal_strength": float(sig.payload.get("strength", 0.7)),
        "confidence": float(sig.payload.get("confidence", 0.8))
    })
    return {"accepted": True, "agent_actions": actions, "global_index": idx}

@router.get("/index")
def get_index():
    return {"global_index": compute_index({"signal_strength": 0.9, "confidence": 0.88})}
