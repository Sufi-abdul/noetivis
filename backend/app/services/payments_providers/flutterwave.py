
from app.services.payments_providers.base import Provider

class FlutterwaveProvider(Provider):
    def create_charge(self, amount: float, currency: str, metadata: dict) -> dict:
        return {"ok": True, "provider": "flutterwave", "amount": amount, "currency": currency, "ref": "sim_flw_001"}

    def parse_webhook(self, payload: dict) -> dict:
        evt = payload.get("event") or payload.get("event.type") or "unknown"
        data = payload.get("data") or payload
        return {
            "event_id": str(data.get("id") or payload.get("id") or "unknown"),
            "type": evt,
            "status": str(data.get("status") or "unknown"),
            "amount": float(data.get("amount") or 0),
            "currency": str(data.get("currency") or "NGN"),
            "customer_ref": str((data.get("customer") or {}).get("email") or ""),
            "provider_ref": str(data.get("tx_ref") or data.get("flw_ref") or ""),
        }
