
def split_default(amount: float):
    a = float(amount)
    return {
        "founder": round(a*0.20, 6),
        "contributors": round(a*0.10, 6),
        "partner": round(a*0.05, 6),
        "owner": round(a*0.65, 6),
        # reseller can optionally come from partner/owner in Phase 9; left 0 here by default
        "reseller": 0.0,
    }
