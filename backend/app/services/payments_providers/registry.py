
from app.services.payments_providers.paystack import PaystackProvider
from app.services.payments_providers.flutterwave import FlutterwaveProvider
from app.services.payments_providers.stripe import StripeProvider

REGISTRY = {
    "paystack": PaystackProvider(),
    "flutterwave": FlutterwaveProvider(),
    "stripe": StripeProvider(),
}

def get_provider(name: str):
    return REGISTRY.get(name)
