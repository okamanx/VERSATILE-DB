import uuid
from sqlalchemy import Column, String, TIMESTAMP, JSON, ForeignKey
from sqlalchemy.orm import relationship
from backend.models.base import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    discord_id = Column(String)
    wallet_address = Column(String)
    created_at = Column(TIMESTAMP)
    profile = relationship('Profile', back_populates='user', uselist=False)

class Profile(Base):
    __tablename__ = 'profiles'
    user_id = Column(String, ForeignKey('users.id', ondelete='CASCADE'), primary_key=True)
    bio = Column(String)
    region = Column(String)
    roles = Column(String)  # Store as JSON string
    badges = Column(String)  # Store as JSON string
    grind_data = Column(JSON)
    pentagon_data = Column(JSON)
    user = relationship('User', back_populates='profile') 