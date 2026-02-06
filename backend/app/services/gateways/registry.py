
from app.services.gateways.stripe_like import StripeLikeGateway
from app.services.gateways.paystack_like import PaystackLikeGateway
from app.services.gateways.flutterwave_like import FlutterwaveLikeGateway

REGISTRY = {
    "stripe_like": StripeLikeGateway(),
    "paystack_like": PaystackLikeGateway(),
    "flutterwave_like": FlutterwaveLikeGateway(),
}

def get_gateway(name: str):
    return REGISTRY.get(name)
