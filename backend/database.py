from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Hardcoded for local development - use SQLite
DATABASE_URL = "sqlite:///versatile_db.sqlite"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(engine, expire_on_commit=False) 