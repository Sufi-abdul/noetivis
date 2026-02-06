
from app.services.gateways.base import PaymentGateway

class FlutterwaveLikeGateway(PaymentGateway):
    def charge(self, amount: float, currency: str, metadata: dict) -> dict:
        return {"ok": True, "provider": "flutterwave_like", "amount": amount, "currency": currency, "ref": "sim_flw_001"}
