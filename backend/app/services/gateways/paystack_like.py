
from app.services.gateways.base import PaymentGateway

class PaystackLikeGateway(PaymentGateway):
    def charge(self, amount: float, currency: str, metadata: dict) -> dict:
        return {"ok": True, "provider": "paystack_like", "amount": amount, "currency": currency, "ref": "sim_paystack_001"}
