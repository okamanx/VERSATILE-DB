import uuid
from sqlalchemy import Column, String, Boolean
from backend.models.base import Base

class Sponsor(Base):
    __tablename__ = 'sponsors'
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String)
    org_id = Column(String)
    verified = Column(Boolean) 