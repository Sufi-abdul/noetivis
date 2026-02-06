
from app.services.gateways.base import PaymentGateway

class StripeLikeGateway(PaymentGateway):
    def charge(self, amount: float, currency: str, metadata: dict) -> dict:
        # Stub: integrate real SDK later
        return {"ok": True, "provider": "stripe_like", "amount": amount, "currency": currency, "ref": "sim_stripe_001"}
