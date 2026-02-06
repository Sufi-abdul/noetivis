
from fastapi import APIRouter
router = APIRouter(prefix="/content", tags=["content"])

@router.post("/register")
def register(content_type: str):
    return {"registered": content_type}
