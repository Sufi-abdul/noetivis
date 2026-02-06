
import os

def getenv(name: str, default: str = "") -> str:
    return os.environ.get(name, default)

NOETIVIS_SECRET_KEY = getenv("NOETIVIS_SECRET_KEY", "CHANGE_ME")
NOETIVIS_ENV = getenv("NOETIVIS_ENV", "dev")

NOETIVIS_API_KEYS = [k.strip() for k in getenv("NOETIVIS_API_KEYS", "").split(",") if k.strip()]
NOETIVIS_RPM_LIMIT = int(getenv("NOETIVIS_RPM_LIMIT", "120"))
