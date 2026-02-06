
from sqlalchemy import Column, String, Float, DateTime, Text
from app.database import Base
import uuid, datetime

class Wallet(Base):
    __tablename__ = "wallets"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, index=True)
    balance = Column(Float, default=0.0)
    currency = Column(String, default="USD")
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)

class WalletTxn(Base):
    __tablename__ = "wallet_txns"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    wallet_id = Column(String, index=True)
    direction = Column(String)  # credit|debit
    amount = Column(Float)
    currency = Column(String, default="USD")
    provider = Column(String, default="internal")
    provider_ref = Column(String, index=True)  # charge_id, transfer_id
    status = Column(String, default="pending")  # pending|succeeded|failed
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class WebhookEvent(Base):
    __tablename__ = "webhook_events"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    provider = Column(String)  # paystack|flutterwave|stripe
    event_id = Column(String, index=True)  # provider event id
    idempotency_key = Column(String, unique=True, index=True)
    payload = Column(Text)
    received_at = Column(DateTime, default=datetime.datetime.utcnow)
    processed_at = Column(DateTime, nullable=True)
    status = Column(String, default="received")  # received|processed|ignored|failed

class DeadLetter(Base):
    __tablename__ = "dead_letters"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    provider = Column(String)
    idempotency_key = Column(String, index=True)
    error = Column(Text)
    payload = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
