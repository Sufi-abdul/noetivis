
from sqlalchemy import Column, String, DateTime, Text
from app.database import Base
import uuid, datetime

class OAuthLink(Base):
    __tablename__ = "oauth_links"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, index=True)
    provider = Column(String)  # google|microsoft|github|custom
    provider_user_id = Column(String, index=True)
    encrypted_tokens = Column(Text)  # sealed tokens json
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class Tenant(Base):
    __tablename__ = "tenants"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    slug = Column(String, unique=True, index=True)  # public, org-xyz
    name = Column(String)
    branding_json = Column(Text)  # theme config json
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class Plugin(Base):
    __tablename__ = "plugins"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    tenant_slug = Column(String, index=True, default="public")
    name = Column(String)
    version = Column(String, default="0.1.0")
    manifest_json = Column(Text)  # plugin manifest
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class RoyaltyRule(Base):
    __tablename__ = "royalty_rules"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    tenant_slug = Column(String, index=True, default="public")
    content_type = Column(String)  # music|video|photo|writing
    rule_json = Column(Text)       # split config
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
