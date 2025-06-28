import uuid
from sqlalchemy import Column, String, Float, ForeignKey, CheckConstraint
from backend.models.base import Base

class Gig(Base):
    __tablename__ = 'gigs'
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String)
    description = Column(String)
    org_id = Column(String)
    budget = Column(Float)
    method = Column(String, CheckConstraint("method IN ('upi', 'card')"))
    status = Column(String, CheckConstraint("status IN ('open', 'closed')"))

class Application(Base):
    __tablename__ = 'applications'
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    gig_id = Column(String, ForeignKey('gigs.id', ondelete='CASCADE'))
    user_id = Column(String, ForeignKey('users.id', ondelete='CASCADE'))
    resume_link = Column(String)
    message = Column(String)
    status = Column(String, CheckConstraint("status IN ('pending', 'accepted', 'rejected')")) 