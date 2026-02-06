
def split(amount: float):
    return {
        "founder": round(amount*0.20, 6),
        "contributors": round(amount*0.10, 6),
        "partner": round(amount*0.05, 6),
        "owner": round(amount*0.65, 6),
    }
