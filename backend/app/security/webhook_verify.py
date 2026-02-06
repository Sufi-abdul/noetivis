
"""Webhook signature verification helpers.

Provider specifics vary; these are safe scaffolds:
- HMAC SHA256 signatures (common pattern)
- Hash comparison using constant-time compare
"""

import hmac, hashlib

def hmac_sha256_verify(secret: str, payload_bytes: bytes, signature_hex: str) -> bool:
    mac = hmac.new(secret.encode("utf-8"), msg=payload_bytes, digestmod=hashlib.sha256).hexdigest()
    return hmac.compare_digest(mac, signature_hex or "")

def sha512_verify(secret: str, payload_bytes: bytes, signature_hex: str) -> bool:
    mac = hmac.new(secret.encode("utf-8"), msg=payload_bytes, digestmod=hashlib.sha512).hexdigest()
    return hmac.compare_digest(mac, signature_hex or "")
