
from app.services.vtu.base import VTUProvider

class DemoVTU(VTUProvider):
    def topup(self, phone: str, amount: float, network: str, metadata: dict) -> dict:
        return {"ok": True, "provider": "demo_vtu", "phone": phone, "amount": amount, "network": network, "ref": "sim_vtu_001"}
