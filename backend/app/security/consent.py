
from fastapi import HTTPException
from typing import List

# MVP scopes; expand as needed
# Example: vault:read, vault:write, tax:report, payments:charge, royalties:write
def require_scopes(user_payload: dict, required: List[str]):
    scopes = user_payload.get("scopes") or []
    missing = [s for s in required if s not in scopes]
    if missing:
        raise HTTPException(status_code=403, detail=f"Missing scopes: {missing}")
    return True
