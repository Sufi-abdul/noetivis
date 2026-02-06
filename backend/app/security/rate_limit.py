
import time
from fastapi import Request, HTTPException
from config import NOETIVIS_RPM_LIMIT

# MVP in-memory store: {ip: (window_start, count)}
_BUCKETS = {}

def rate_limit(request: Request):
    ip = request.client.host if request.client else "unknown"
    now = time.time()
    window = int(now // 60)  # per-minute buckets
    key = (ip, window)
    count = _BUCKETS.get(key, 0) + 1
    _BUCKETS[key] = count
    if count > NOETIVIS_RPM_LIMIT:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")
