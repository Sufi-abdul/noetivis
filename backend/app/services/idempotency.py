
from sqlalchemy.orm import Session
from app.models_phase20 import WebhookEvent

def seen(db: Session, idempotency_key: str) -> bool:
    return db.query(WebhookEvent).filter(WebhookEvent.idempotency_key==idempotency_key).first() is not None
