
from app.services.payments_providers.base import Provider

class StripeProvider(Provider):
    def create_charge(self, amount: float, currency: str, metadata: dict) -> dict:
        return {"ok": True, "provider": "stripe", "amount": amount, "currency": currency, "ref": "sim_stripe_001"}

    def parse_webhook(self, payload: dict) -> dict:
        # Stripe often wraps payload as {id, type, data:{object:{...}}}
        evt_id = payload.get("id") or "unknown"
        evt_type = payload.get("type") or "unknown"
        obj = ((payload.get("data") or {}).get("object") or {})
        return {
            "event_id": str(evt_id),
            "type": str(evt_type),
            "status": str(obj.get("status") or "unknown"),
            "amount": float((obj.get("amount") or 0)/100.0) if isinstance(obj.get("amount"), (int,float)) else float(obj.get("amount") or 0),
            "currency": str(obj.get("currency") or "USD").upper(),
            "customer_ref": str(obj.get("receipt_email") or obj.get("customer") or ""),
            "provider_ref": str(obj.get("id") or ""),
        }
