import uuid
from sqlalchemy import Column, String, TIMESTAMP, ForeignKey
from backend.models.base import Base

class Highlight(Base):
    __tablename__ = 'highlights'
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey('users.id', ondelete='CASCADE'))
    title = Column(String)
    clip_url = Column(String)
    tags = Column(String)  # Store as JSON string
    created_at = Column(TIMESTAMP) 