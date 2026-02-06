
from app.services.payments_providers.base import Provider

class PaystackProvider(Provider):
    def create_charge(self, amount: float, currency: str, metadata: dict) -> dict:
        # Stub: integrate real Paystack initialize transaction endpoint later.
        return {"ok": True, "provider": "paystack", "amount": amount, "currency": currency, "ref": "sim_ps_001"}

    def parse_webhook(self, payload: dict) -> dict:
        # Normalize common fields (structure varies; adjust per Paystack docs)
        evt = payload.get("event") or "unknown"
        data = payload.get("data") or {}
        return {
            "event_id": str(data.get("id") or payload.get("id") or "unknown"),
            "type": evt,
            "status": str(data.get("status") or "unknown"),
            "amount": float((data.get("amount") or 0)/100.0) if isinstance(data.get("amount"), (int,float)) else float(data.get("amount") or 0),
            "currency": str(data.get("currency") or "NGN"),
            "customer_ref": str((data.get("customer") or {}).get("email") or ""),
            "provider_ref": str(data.get("reference") or ""),
        }
