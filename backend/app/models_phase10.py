
from sqlalchemy import Column, String, Float, DateTime, Boolean
from app.database import Base
import uuid, datetime

class Treasury(Base):
    __tablename__ = "treasury"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    pool = Column(String)  # founder_pool|contributors_pool|ops_pool
    amount = Column(Float, default=0.0)
    currency = Column(String, default="USD")
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)

class ContributorAllocation(Base):
    __tablename__ = "contributor_allocations"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    contributor_user_id = Column(String, index=True)
    weight = Column(Float, default=1.0)  # proportional share of contributors_pool
    active = Column(Boolean, default=True)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)

class Batch(Base):
    __tablename__ = "batches"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    status = Column(String, default="open")  # open|locked|paid
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    locked_at = Column(DateTime, nullable=True)

class PayoutLock(Base):
    __tablename__ = "payout_locks"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    payout_id = Column(String, index=True, unique=True)
    locked = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
