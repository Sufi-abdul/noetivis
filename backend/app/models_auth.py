
from sqlalchemy import Column, String, DateTime
from app.database import Base
import uuid, datetime

class AuthUser(Base):
    __tablename__ = "auth_users"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    role = Column(String, default="client")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
