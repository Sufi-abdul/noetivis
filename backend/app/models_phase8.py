
from sqlalchemy import Column, String, Float, DateTime, ForeignKey
from app.database import Base
import uuid, datetime

class Attribution(Base):
    __tablename__ = "attributions"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    # What is being attributed: entity/content
    subject_type = Column(String)  # entity|content
    subject_id = Column(String, index=True)
    # Who benefits
    owner_user_id = Column(String, index=True, nullable=True)
    partner_user_id = Column(String, index=True, nullable=True)
    reseller_user_id = Column(String, index=True, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class Payout(Base):
    __tablename__ = "payouts"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    ledger_id = Column(String, index=True)
    payee_role = Column(String)  # founder|contributors|partner|owner|reseller
    payee_user_id = Column(String, index=True, nullable=True)
    amount = Column(Float)
    currency = Column(String, default="USD")
    status = Column(String, default="pending")  # pending|paid|failed
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    paid_at = Column(DateTime, nullable=True)
