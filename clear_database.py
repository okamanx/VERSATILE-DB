import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from backend.database import SessionLocal
from backend.models import User, Profile, Game, Highlight, Gig, Application, Team, Sponsor

def clear_database():
    session = SessionLocal()
    try:
        print("🗑️ Clearing all data from database...")
        
        # Delete in reverse order of dependencies
        session.query(Application).delete()
        session.query(Team).delete()
        session.query(Highlight).delete()
        session.query(Game).delete()
        session.query(Profile).delete()
        session.query(Gig).delete()
        session.query(Sponsor).delete()
        session.query(User).delete()
        
        session.commit()
        print("✅ Database cleared successfully!")
    except Exception as e:
        session.rollback()
        print(f"❌ Error clearing database: {e}")
    finally:
        session.close()

if __name__ == '__main__':
    clear_database() 