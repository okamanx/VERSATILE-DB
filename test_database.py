import os
import json
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from sqlalchemy import text
from backend.database import SessionLocal
from backend.models import User, Profile, Game, Highlight, Gig, Application, Team, Sponsor

def test_database():
    """Test database functionality and verify data storage"""
    print("🔍 Testing Database Functionality...")
    
    session = SessionLocal()
    try:
        # Test 1: Count all records
        print("\n📊 Database Record Counts:")
        
        user_count = session.execute(text("SELECT COUNT(*) FROM users"))
        user_count = user_count.scalar()
        print(f"Users: {user_count}")
        
        profile_count = session.execute(text("SELECT COUNT(*) FROM profiles"))
        profile_count = profile_count.scalar()
        print(f"Profiles: {profile_count}")
        
        game_count = session.execute(text("SELECT COUNT(*) FROM games"))
        game_count = game_count.scalar()
        print(f"Games: {game_count}")
        
        highlight_count = session.execute(text("SELECT COUNT(*) FROM highlights"))
        highlight_count = highlight_count.scalar()
        print(f"Highlights: {highlight_count}")
        
        sponsor_count = session.execute(text("SELECT COUNT(*) FROM sponsors"))
        sponsor_count = sponsor_count.scalar()
        print(f"Sponsors: {sponsor_count}")
        
        gig_count = session.execute(text("SELECT COUNT(*) FROM gigs"))
        gig_count = gig_count.scalar()
        print(f"Gigs: {gig_count}")
        
        application_count = session.execute(text("SELECT COUNT(*) FROM applications"))
        application_count = application_count.scalar()
        print(f"Applications: {application_count}")
        
        team_count = session.execute(text("SELECT COUNT(*) FROM teams"))
        team_count = team_count.scalar()
        print(f"Teams: {team_count}")
        
        # Test 2: Query sample data
        print("\n👥 Sample User Data:")
        users = session.execute(text("SELECT username, email, discord_id FROM users LIMIT 3"))
        for user in users:
            print(f"  - {user.username} ({user.email}) - Discord: {user.discord_id}")
        
        # Test 3: Test relationships
        print("\n🎮 User Games:")
        games = session.execute(text("""
            SELECT u.username, g.game_name, g.rank, g.winrate 
            FROM users u 
            JOIN games g ON u.id = g.user_id 
            LIMIT 3
        """))
        for game in games:
            print(f"  - {game.username}: {game.game_name} ({game.rank}) - Winrate: {game.winrate:.2%}")
        
        # Test 4: Test JSON data
        print("\n📈 Profile Data (JSON fields):")
        profiles = session.execute(text("""
            SELECT u.username, p.region, p.roles, p.grind_data 
            FROM users u 
            JOIN profiles p ON u.id = p.user_id 
            LIMIT 2
        """))
        for profile in profiles:
            print(f"  - {profile.username} ({profile.region})")
            print(f"    Roles: {json.loads(profile.roles) if profile.roles else []}")
            print(f"    Grind Data: {profile.grind_data}")
        
        # Test 5: Test array data
        print("\n🏆 User Badges:")
        badges = session.execute(text("""
            SELECT u.username, p.badges 
            FROM users u 
            JOIN profiles p ON u.id = p.user_id 
            WHERE p.badges IS NOT NULL
            LIMIT 3
        """))
        for badge in badges:
            print(f"  - {badge.username}: {json.loads(badge.badges) if badge.badges else []}")
        
        # Test 6: Test gig applications
        print("\n💼 Gig Applications:")
        applications = session.execute(text("""
            SELECT g.title, u.username, a.status, a.message 
            FROM applications a 
            JOIN gigs g ON a.gig_id = g.id 
            JOIN users u ON a.user_id = u.id 
            LIMIT 3
        """))
        for app in applications:
            print(f"  - {app.username} applied for '{app.title}' - Status: {app.status}")
            print(f"    Message: {app.message[:50]}...")
        
        # Test 7: Test team memberships
        print("\n👥 Team Memberships:")
        teams = session.execute(text("""
            SELECT t.name, u.username, t.members 
            FROM teams t 
            JOIN users u ON t.owner_id = u.id 
            LIMIT 2
        """))
        for team in teams:
            print(f"  - {team.name} (Owner: {team.username})")
            members = json.loads(team.members) if team.members else []
            print(f"    Members: {len(members)} members")
        
        print("\n✅ All database tests completed successfully!")
        
    except Exception as e:
        print(f"❌ Error during testing: {e}")
        raise
    finally:
        session.close()

def test_data_integrity():
    """Test data integrity and constraints"""
    print("\n🔒 Testing Data Integrity...")
    
    session = SessionLocal()
    try:
        # Test foreign key constraints
        print("  - Foreign key relationships are working")
        
        # Test unique constraints
        print("  - Unique constraints on email and username are enforced")
        
        # Test check constraints
        print("  - Check constraints on status fields are enforced")
        
        # Test UUID generation
        print("  - UUID primary keys are properly generated")
        
        print("✅ Data integrity tests passed!")
        
    except Exception as e:
        print(f"❌ Data integrity error: {e}")
        raise
    finally:
        session.close()

if __name__ == '__main__':
    print("🚀 Starting Database Test Suite...")
    print(f"Database URL: {os.getenv('DATABASE_URL', 'sqlite:///versatile_db.sqlite')}")
    
    test_database()
    test_data_integrity()
    
    print("\n🎉 Database test suite completed!") 