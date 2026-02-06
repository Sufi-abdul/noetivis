
from fastapi import Header, HTTPException
from config import NOETIVIS_API_KEYS

def require_api_key(x_api_key: str = Header(default="")):
    if NOETIVIS_API_KEYS and x_api_key not in NOETIVIS_API_KEYS:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return x_api_key
