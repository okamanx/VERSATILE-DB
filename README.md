# VERSATILE-DB

A comprehensive gaming platform database system built with PostgreSQL and SQLAlchemy, designed for esports teams, content creators, and gaming communities.

## 🎮 Features

- **User Management**: Complete user profiles with gaming statistics
- **Game Tracking**: Multi-game support with rankings and win rates
- **Content Creation**: Highlight clips and content management
- **Gig Economy**: Job postings and applications for gaming professionals
- **Team Management**: Esports team creation and member management
- **Sponsorship**: Sponsor verification and organization management

## 🗄️ Database Schema

### Core Tables

1. **Users** - Main user accounts with Discord integration and wallet support
2. **Profiles** - Extended user profiles with gaming stats and pentagon data
3. **Games** - User game statistics and rankings
4. **Highlights** - User-created content and clips
5. **Gigs** - Job postings for gaming professionals
6. **Applications** - Job applications and status tracking
7. **Teams** - Esports team management
8. **Sponsors** - Sponsor organizations and verification

### Key Features

- **UUID Primary Keys** for all tables
- **Foreign Key Relationships** with cascade deletes
- **JSON Data Types** for flexible gaming statistics
- **Array Data Types** for roles, badges, and tags
- **Check Constraints** for status validation
- **Async SQLAlchemy** for high performance

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- PostgreSQL 12+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd VERSATILE-DB
   ```

2. **Set up PostgreSQL**
   - Install PostgreSQL
   - Create a database named `VERSATILE-DB`
   - Default connection: `postgresql://postgres:Aman1234@localhost:5432/VERSATILE-DB`

3. **Run the setup script**
   ```bash
   python setup_database.py
   ```

   This will:
   - Install all dependencies
   - Check PostgreSQL connection
   - Create all database tables
   - Seed with sample data
   - Run comprehensive tests

### Manual Setup

If you prefer manual setup:

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Create tables**
   ```bash
   python backend/create_tables.py
   ```

3. **Seed data**
   ```bash
   python backend/seed_data.py
   ```

4. **Test database**
   ```bash
   python test_database.py
   ```

## 📊 Sample Data

The seed script creates:

- **3 Users** with complete profiles
- **3 Game records** (Overwatch 2, Valorant, League of Legends)
- **2 Highlights** with tags and URLs
- **2 Sponsors** (verified and unverified)
- **2 Gigs** with different payment methods
- **3 Applications** with various statuses
- **2 Teams** with multiple members

## 🧪 Testing

### Database Tests

Run comprehensive database tests:
```bash
python test_database.py
```

Tests include:
- Record counts for all tables
- Sample data queries
- Relationship testing
- JSON and array data validation
- Foreign key constraint verification

### Connection Test

Test PostgreSQL connection:
```bash
python test_asyncpg.py
```

## 🔧 Configuration

### Environment Variables

Set `DATABASE_URL` to override the default connection:
```bash
export DATABASE_URL="postgresql+asyncpg://user:password@host:port/database"
```

### Default Configuration

- **Host**: localhost
- **Port**: 5432
- **User**: postgres
- **Password**: Aman1234
- **Database**: VERSATILE-DB

## 📁 Project Structure

```
VERSATILE-DB/
├── backend/
│   ├── database.py          # Database connection and session
│   ├── create_tables.py     # Table creation script
│   ├── seed_data.py         # Sample data seeding
│   └── models/
│       ├── __init__.py      # Model imports
│       ├── base.py          # SQLAlchemy base
│       ├── user.py          # User and Profile models
│       ├── game.py          # Game statistics
│       ├── highlight.py     # Content clips
│       ├── gig.py           # Jobs and applications
│       ├── team.py          # Team management
│       └── sponsor.py       # Sponsor organizations
├── requirements.txt         # Python dependencies
├── setup_database.py        # Automated setup script
├── test_database.py         # Database testing
├── test_asyncpg.py          # Connection testing
└── README.md               # This file
```

## 🎯 Use Cases

### For Gamers
- Track performance across multiple games
- Build gaming portfolio with highlights
- Apply for gaming gigs and opportunities
- Join or create esports teams

### For Content Creators
- Manage highlight clips and content
- Track audience engagement
- Apply for sponsored content opportunities
- Build professional gaming profile

### For Teams
- Manage team rosters and memberships
- Track team performance across games
- Coordinate with sponsors
- Organize team applications

### For Sponsors
- Post gaming-related job opportunities
- Verify sponsor status
- Manage applications and candidates
- Track sponsorship relationships

## 🔒 Data Integrity

The database includes:
- **Foreign Key Constraints** with cascade deletes
- **Unique Constraints** on email and username
- **Check Constraints** for status validation
- **UUID Primary Keys** for security
- **Proper Indexing** for performance

## 🚀 Performance

- **Async SQLAlchemy** for non-blocking database operations
- **Connection pooling** for efficient resource usage
- **Optimized queries** with proper joins
- **Indexed foreign keys** for fast lookups

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

If you encounter any issues:

1. Check the PostgreSQL connection settings
2. Verify all dependencies are installed
3. Run the test scripts to identify problems
4. Check the console output for error messages

## 🔄 Database Migrations

For production use, consider implementing:
- Alembic for database migrations
- Environment-specific configurations
- Backup and recovery procedures
- Monitoring and logging

---

**Happy Gaming! 🎮** 