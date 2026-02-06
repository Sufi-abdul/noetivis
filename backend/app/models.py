
from sqlalchemy import Column, String, Float, DateTime, ForeignKey
from app.database import Base
import uuid, datetime

class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String, unique=True)

class Entity(Base):
    __tablename__ = "entities"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    type = Column(String)
    name = Column(String)
    owner_id = Column(String, ForeignKey("users.id"))

class Content(Base):
    __tablename__ = "content"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    entity_id = Column(String, ForeignKey("entities.id"))
    content_type = Column(String)

class Ledger(Base):
    __tablename__ = "ledger"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    entity_id = Column(String)
    amount = Column(Float)
    reason = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
