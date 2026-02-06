
from abc import ABC, abstractmethod
from typing import Dict

class PaymentGateway(ABC):
    @abstractmethod
    def charge(self, amount: float, currency: str, metadata: Dict) -> Dict:
        raise NotImplementedError
