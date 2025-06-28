import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.database import engine
from backend.models import Base

def create_all():
    Base.metadata.create_all(engine)
    print('All tables created!')

if __name__ == '__main__':
    print("DATABASE_URL:", os.getenv("DATABASE_URL"))
    create_all()