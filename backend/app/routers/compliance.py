
from fastapi import APIRouter

router = APIRouter(prefix="/compliance", tags=["compliance"])

@router.get("/tax-report")
def tax_report():
    return {"report": "tax summary scaffold"}
