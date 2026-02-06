
import json

DEFAULT_RULES = {
  "music": {"publisher": 0.15, "distributor": 0.10, "creator": 0.75},
  "video": {"publisher": 0.10, "distributor": 0.10, "creator": 0.80},
  "photo": {"publisher": 0.08, "distributor": 0.07, "creator": 0.85},
  "writing": {"publisher": 0.10, "distributor": 0.05, "creator": 0.85},
}

def apply_rule(content_type: str, gross: float, rule_json: str | None = None):
    rule = DEFAULT_RULES.get(content_type, {"creator": 1.0})
    if rule_json:
        try:
            rule = json.loads(rule_json)
        except Exception:
            pass
    total = sum(float(v) for v in rule.values()) or 1.0
    # normalize
    norm = {k: float(v)/total for k, v in rule.items()}
    return {k: round(gross*share, 6) for k, share in norm.items()}
