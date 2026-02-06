
from sqlalchemy import Column, String, DateTime, Text
from app.database import Base
import uuid, datetime

class DataVault(Base):
    __tablename__ = "data_vault"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, index=True)
    label = Column(String)
    encrypted_blob = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class AccessAudit(Base):
    __tablename__ = "access_audit"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    actor = Column(String)
    action = Column(String)
    resource = Column(String)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
