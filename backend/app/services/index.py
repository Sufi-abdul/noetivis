
def compute_index(metrics: dict) -> float:
    vals = [float(v) for v in metrics.values()] or [0.0]
    return round(sum(vals)/len(vals), 4)
