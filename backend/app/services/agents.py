
def run_agents(sector: str, payload: dict):
    strength = float(payload.get("strength", 0.7))
    if strength > 0.85: action = "escalate"
    elif strength > 0.6: action = "monitor"
    else: action = "ignore"
    return [{"sector": sector, "action": action, "note": "MVP agent"}]
