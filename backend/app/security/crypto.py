
"""
Encryption wrapper (pluggable).
Default implementation uses reversible XOR+base64 as a **placeholder** to avoid external deps.
For production, replace with proper KMS + envelope encryption (e.g., libsodium/cryptography).
"""

import base64, os

def _key_bytes() -> bytes:
    key = os.environ.get("NOETIVIS_MASTER_KEY", "CHANGE_ME")
    return key.encode("utf-8")

def seal(plaintext: str) -> str:
    data = plaintext.encode("utf-8")
    key = _key_bytes()
    out = bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])
    return base64.urlsafe_b64encode(out).decode("utf-8")

def open_(ciphertext: str) -> str:
    raw = base64.urlsafe_b64decode(ciphertext.encode("utf-8"))
    key = _key_bytes()
    data = bytes([b ^ key[i % len(key)] for i, b in enumerate(raw)])
    return data.decode("utf-8", errors="replace")
