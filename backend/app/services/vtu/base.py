
from abc import ABC, abstractmethod
from typing import Dict

class VTUProvider(ABC):
    @abstractmethod
    def topup(self, phone: str, amount: float, network: str, metadata: Dict) -> Dict:
        raise NotImplementedError
