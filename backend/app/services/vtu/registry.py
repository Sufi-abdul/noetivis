
from app.services.vtu.demo_provider import DemoVTU

VTU_REGISTRY = {"demo_vtu": DemoVTU()}

def get_vtu(name: str):
    return VTU_REGISTRY.get(name)
