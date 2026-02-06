
from fastapi import APIRouter

router = APIRouter(prefix="/query", tags=["query"])

@router.post("/search")
def search(query: str):
    return {"result": f"authorized query processed: {query}"}
