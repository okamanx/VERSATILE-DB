import uuid
from sqlalchemy import Column, String, ForeignKey
from backend.models.base import Base

class Team(Base):
    __tablename__ = 'teams'
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String)
    owner_id = Column(String, ForeignKey('users.id'))
    members = Column(String)  # Store as JSON string 