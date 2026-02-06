
from typing import Dict

def compute_gross(content_type: str, usage_type: str, units: float, rates: Dict) -> float:
    rate = float(rates.get(content_type, {}).get(usage_type, 0.0))
    return rate * float(units)
