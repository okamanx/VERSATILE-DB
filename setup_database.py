import os
import subprocess
import sys

def install_dependencies():
    """Install required dependencies"""
    print("📦 Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False
    return True

def setup_database():
    """Set up the database tables and seed data"""
    print("🗄️ Setting up database...")
    
    try:
        # Create tables
        print("  - Creating tables...")
        subprocess.check_call([sys.executable, "backend/create_tables.py"])
        print("  ✅ Tables created successfully!")
        
        # Seed data
        print("  - Seeding data...")
        subprocess.check_call([sys.executable, "backend/seed_data.py"])
        print("  ✅ Data seeded successfully!")
        
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Database setup failed: {e}")
        return False

def test_database():
    """Test the database functionality"""
    print("🧪 Testing database...")
    try:
        subprocess.check_call([sys.executable, "test_database.py"])
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Database test failed: {e}")
        return False

def main():
    """Main setup function"""
    print("🚀 VERSATILE-DB Setup Script")
    print("=" * 50)
    
    # Step 1: Install dependencies
    if not install_dependencies():
        print("❌ Setup failed at dependency installation")
        return
    
    # Step 2: Setup database
    if not setup_database():
        print("❌ Setup failed at database setup")
        return
    
    # Step 3: Test database
    if not test_database():
        print("❌ Setup failed at database testing")
        return
    
    print("\n🎉 Setup completed successfully!")
    print("\n📋 Summary:")
    print("  ✅ Dependencies installed")
    print("  ✅ Database tables created")
    print("  ✅ Sample data seeded")
    print("  ✅ Database functionality tested")
    
    print("\n🚀 You can now:")
    print("  - Run 'python backend/seed_data.py' to add more data")
    print("  - Run 'python test_database.py' to test the database")
    print("  - Start building your application!")
    print("\n💡 Database file: versatile_db.sqlite")

if __name__ == '__main__':
    main() 