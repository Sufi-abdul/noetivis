
from abc import ABC, abstractmethod
from typing import Dict

class Provider(ABC):
    @abstractmethod
    def create_charge(self, amount: float, currency: str, metadata: Dict) -> Dict:
        raise NotImplementedError

    @abstractmethod
    def parse_webhook(self, payload: Dict) -> Dict:
        """Return a normalized event dict:
        {event_id, type, status, amount, currency, customer_ref, provider_ref}
        """
        raise NotImplementedError
