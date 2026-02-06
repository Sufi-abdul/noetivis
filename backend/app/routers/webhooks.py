
from fastapi import APIRouter, Depends, Request, Header, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
import json, os

from app.database import SessionLocal
from app.models_phase20 import WebhookEvent, DeadLetter
from app.security.webhook_verify import hmac_sha256_verify, sha512_verify
from app.services.idempotency import seen
from app.services.payments_providers.registry import get_provider
from app.services.wallet import get_wallet, credit

router = APIRouter(prefix="/webhooks", tags=["webhooks"])

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

def _idempotency(provider: str, event_id: str) -> str:
    return f"{provider}:{event_id}"

@router.post("/{provider}")
async def receive(provider: str,
                  request: Request,
                  db: Session = Depends(get_db),
                  x_signature: str = Header(default=""),
                  x_signature_sha512: str = Header(default="")):
    payload_bytes = await request.body()
    try:
        payload = json.loads(payload_bytes.decode("utf-8") or "{}")
    except Exception:
        payload = {}

    # Verify signature (scaffold: set secrets in env)
    secret = os.environ.get(f"NOETIVIS_{provider.upper()}_WEBHOOK_SECRET", "")
    if secret:
        # choose an algorithm based on provider conventions; keep both options
        sig_ok = False
        if x_signature:
            sig_ok = hmac_sha256_verify(secret, payload_bytes, x_signature)
        if (not sig_ok) and x_signature_sha512:
            sig_ok = sha512_verify(secret, payload_bytes, x_signature_sha512)
        if not sig_ok:
            raise HTTPException(status_code=401, detail="Invalid webhook signature")

    prov = get_provider(provider)
    if not prov:
        raise HTTPException(status_code=400, detail="Unknown provider")

    evt = prov.parse_webhook(payload)
    idem = _idempotency(provider, evt.get("event_id","unknown"))

    if seen(db, idem):
        return {"ok": True, "status": "duplicate_ignored", "idempotency_key": idem}

    we = WebhookEvent(provider=provider, event_id=evt.get("event_id","unknown"), idempotency_key=idem, payload=json.dumps(payload))
    db.add(we); db.commit(); db.refresh(we)

    try:
        # Simple credit-on-success example:
        status = (evt.get("status") or "").lower()
        if "success" in status or "succeeded" in status:
            # Identify user by customer_ref (email) in real system via mapping table.
            # Here we credit to a demo "POOL" wallet only if env maps it.
            demo_user = os.environ.get("NOETIVIS_DEMO_WALLET_USER", "POOL")
            w = get_wallet(db, demo_user, currency=str(evt.get("currency","USD")).upper())
            credit(db, w, float(evt.get("amount") or 0), provider=provider, provider_ref=evt.get("provider_ref") or evt.get("event_id"))
        we.status = "processed"
        we.processed_at = datetime.utcnow()
        db.commit()
        return {"ok": True, "status": we.status, "idempotency_key": idem}
    except Exception as e:
        dl = DeadLetter(provider=provider, idempotency_key=idem, error=str(e), payload=json.dumps(payload))
        db.add(dl)
        we.status = "failed"
        db.commit()
        return {"ok": False, "status": "failed", "idempotency_key": idem}
