
from fastapi import APIRouter
router = APIRouter(prefix="/entities", tags=["entities"])

@router.post("/create")
def create(type: str, name: str):
    return {"entity": name, "type": type}
