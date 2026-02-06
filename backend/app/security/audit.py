
import json, datetime, os

AUDIT_PATH = os.environ.get("NOETIVIS_AUDIT_PATH", "./audit.log")

def audit(event: dict):
    record = {
        "ts": datetime.datetime.utcnow().isoformat() + "Z",
        **event
    }
    with open(AUDIT_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")
