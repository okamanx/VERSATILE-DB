import uuid
from sqlalchemy import Column, String, Float, TIMESTAMP, ForeignKey
from backend.models.base import Base

class Game(Base):
    __tablename__ = 'games'
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey('users.id', ondelete='CASCADE'))
    game_name = Column(String)
    rank = Column(String)
    winrate = Column(Float)
    top_roles = Column(String)  # Store as JSON string
    updated_at = Column(TIMESTAMP) 