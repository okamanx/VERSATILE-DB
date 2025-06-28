import uuid
import json
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from datetime import datetime, timezone
from backend.database import SessionLocal
from backend.models import User, Profile, Game, Highlight, Gig, Application, Team, Sponsor

def seed_data():
    session = SessionLocal()
    try:
        # Create more test users
        users_data = [
            {"email": "john.doe@example.com", "username": "john_doe", "discord_id": "john_doe#1234", "wallet_address": "0x1234567890abcdef"},
            {"email": "jane.smith@example.com", "username": "jane_smith", "discord_id": "jane_smith#5678", "wallet_address": "0xfedcba0987654321"},
            {"email": "bob.wilson@example.com", "username": "bob_wilson", "discord_id": "bob_wilson#9012", "wallet_address": "0xabcdef1234567890"},
            {"email": "alice.johnson@example.com", "username": "alice_j", "discord_id": "alice_j#3456", "wallet_address": "0x9876543210fedcba"},
            {"email": "charlie.brown@example.com", "username": "charlie_b", "discord_id": "charlie_b#7890", "wallet_address": "0x5555666677778888"},
            {"email": "diana.prince@example.com", "username": "diana_p", "discord_id": "diana_p#1111", "wallet_address": "0x1111222233334444"},
            {"email": "edward.norton@example.com", "username": "edward_n", "discord_id": "edward_n#2222", "wallet_address": "0x2222333344445555"},
            {"email": "fiona.gallagher@example.com", "username": "fiona_g", "discord_id": "fiona_g#3333", "wallet_address": "0x3333444455556666"},
            {"email": "george.lucas@example.com", "username": "george_l", "discord_id": "george_l#4444", "wallet_address": "0x4444555566667777"},
            {"email": "helena.bonham@example.com", "username": "helena_b", "discord_id": "helena_b#5555", "wallet_address": "0x5555666677778888"},
            {"email": "ivan.drago@example.com", "username": "ivan_d", "discord_id": "ivan_d#6666", "wallet_address": "0x6666777788889999"},
            {"email": "julia.roberts@example.com", "username": "julia_r", "discord_id": "julia_r#7777", "wallet_address": "0x777788889999aaaa"},
            {"email": "kevin.bacon@example.com", "username": "kevin_b", "discord_id": "kevin_b#8888", "wallet_address": "0x88889999aaaabbbb"},
            {"email": "lisa.simpson@example.com", "username": "lisa_s", "discord_id": "lisa_s#9999", "wallet_address": "0x9999aaaabbbbcccc"},
            {"email": "michael.jordan@example.com", "username": "michael_j", "discord_id": "michael_j#0000", "wallet_address": "0x0000bbbbccccdddd"}
        ]
        
        users = []
        for user_data in users_data:
            user = User(
                id=str(uuid.uuid4()),
                email=user_data["email"],
                username=user_data["username"],
                discord_id=user_data["discord_id"],
                wallet_address=user_data["wallet_address"],
                created_at=datetime.now(timezone.utc)
            )
            users.append(user)
        
        session.add_all(users)
        session.flush()  # Get the IDs
        
        # Create profiles for all users
        profiles_data = [
            {"bio": "Professional gamer and content creator", "region": "North America", "roles": ["DPS", "Support"], "badges": ["Top 500", "Season Champion"], "hours_played": 1200, "rank": "Diamond", "mechanical": 85, "game_sense": 90, "communication": 75, "teamwork": 80, "adaptability": 85},
            {"bio": "Esports enthusiast and team player", "region": "Europe", "roles": ["Tank", "Flex"], "badges": ["Team Captain", "MVP"], "hours_played": 800, "rank": "Platinum", "mechanical": 75, "game_sense": 85, "communication": 90, "teamwork": 95, "adaptability": 80},
            {"bio": "Rising star in competitive gaming", "region": "Asia", "roles": ["DPS", "Tank"], "badges": ["Rookie of the Year"], "hours_played": 600, "rank": "Gold", "mechanical": 90, "game_sense": 70, "communication": 65, "teamwork": 75, "adaptability": 85},
            {"bio": "Strategic mastermind and shot caller", "region": "North America", "roles": ["Support", "Flex"], "badges": ["Shot Caller", "Analyst"], "hours_played": 1500, "rank": "Masters", "mechanical": 70, "game_sense": 95, "communication": 90, "teamwork": 85, "adaptability": 80},
            {"bio": "Aggressive playstyle specialist", "region": "Europe", "roles": ["DPS", "Duelist"], "badges": ["Aggressive Player", "Clutch Master"], "hours_played": 900, "rank": "Diamond", "mechanical": 95, "game_sense": 75, "communication": 60, "teamwork": 70, "adaptability": 90},
            {"bio": "Support main with healing expertise", "region": "Asia", "roles": ["Support", "Healer"], "badges": ["Healing Master", "Team Player"], "hours_played": 1100, "rank": "Platinum", "mechanical": 65, "game_sense": 80, "communication": 85, "teamwork": 90, "adaptability": 75},
            {"bio": "Tank specialist and team leader", "region": "North America", "roles": ["Tank", "Flex"], "badges": ["Tank Master", "Leader"], "hours_played": 1300, "rank": "Masters", "mechanical": 80, "game_sense": 85, "communication": 90, "teamwork": 95, "adaptability": 75},
            {"bio": "Flex player with diverse skillset", "region": "Europe", "roles": ["Flex", "Support"], "badges": ["Flex Master", "Adaptable"], "hours_played": 1000, "rank": "Diamond", "mechanical": 75, "game_sense": 80, "communication": 85, "teamwork": 80, "adaptability": 95},
            {"bio": "DPS main with precision aim", "region": "Asia", "roles": ["DPS", "Sniper"], "badges": ["Aim Master", "Precision"], "hours_played": 800, "rank": "Platinum", "mechanical": 90, "game_sense": 70, "communication": 65, "teamwork": 75, "adaptability": 80},
            {"bio": "Strategic support and analyst", "region": "North America", "roles": ["Support", "Analyst"], "badges": ["Analyst", "Strategic"], "hours_played": 1200, "rank": "Diamond", "mechanical": 70, "game_sense": 90, "communication": 85, "teamwork": 85, "adaptability": 80},
            {"bio": "Aggressive tank player", "region": "Europe", "roles": ["Tank", "DPS"], "badges": ["Aggressive", "Tank"], "hours_played": 950, "rank": "Platinum", "mechanical": 85, "game_sense": 75, "communication": 70, "teamwork": 80, "adaptability": 85},
            {"bio": "Flexible player and team coordinator", "region": "Asia", "roles": ["Flex", "Coordinator"], "badges": ["Coordinator", "Flex"], "hours_played": 1100, "rank": "Diamond", "mechanical": 75, "game_sense": 85, "communication": 90, "teamwork": 85, "adaptability": 90},
            {"bio": "Support specialist and mentor", "region": "North America", "roles": ["Support", "Mentor"], "badges": ["Mentor", "Support"], "hours_played": 1400, "rank": "Masters", "mechanical": 65, "game_sense": 85, "communication": 90, "teamwork": 90, "adaptability": 75},
            {"bio": "DPS main with tactical approach", "region": "Europe", "roles": ["DPS", "Tactical"], "badges": ["Tactical", "DPS"], "hours_played": 900, "rank": "Platinum", "mechanical": 85, "game_sense": 80, "communication": 75, "teamwork": 80, "adaptability": 85},
            {"bio": "Versatile player and team captain", "region": "Asia", "roles": ["Captain", "Flex"], "badges": ["Captain", "Versatile"], "hours_played": 1300, "rank": "Masters", "mechanical": 80, "game_sense": 90, "communication": 95, "teamwork": 95, "adaptability": 85}
        ]
        
        profiles = []
        for i, profile_data in enumerate(profiles_data):
            profile = Profile(
                user_id=users[i].id,
                bio=profile_data["bio"],
                region=profile_data["region"],
                roles=json.dumps(profile_data["roles"]),
                badges=json.dumps(profile_data["badges"]),
                grind_data={"hours_played": profile_data["hours_played"], "rank": profile_data["rank"]},
                pentagon_data={"mechanical": profile_data["mechanical"], "game_sense": profile_data["game_sense"], "communication": profile_data["communication"], "teamwork": profile_data["teamwork"], "adaptability": profile_data["adaptability"]}
            )
            profiles.append(profile)
        
        session.add_all(profiles)
        
        # Create games for all users
        games_data = [
            {"game_name": "Overwatch 2", "rank": "Diamond", "winrate": 0.65, "top_roles": ["DPS", "Support"]},
            {"game_name": "Valorant", "rank": "Platinum", "winrate": 0.58, "top_roles": ["Controller", "Duelist"]},
            {"game_name": "League of Legends", "rank": "Gold", "winrate": 0.52, "top_roles": ["ADC", "Top"]},
            {"game_name": "CS:GO", "rank": "Masters", "winrate": 0.72, "top_roles": ["Rifler", "AWP"]},
            {"game_name": "Dota 2", "rank": "Diamond", "winrate": 0.61, "top_roles": ["Carry", "Support"]},
            {"game_name": "Rainbow Six Siege", "rank": "Platinum", "winrate": 0.55, "top_roles": ["Attacker", "Defender"]},
            {"game_name": "Apex Legends", "rank": "Diamond", "winrate": 0.68, "top_roles": ["Fragger", "Support"]},
            {"game_name": "Fortnite", "rank": "Champion", "winrate": 0.45, "top_roles": ["Builder", "Editor"]},
            {"game_name": "Rocket League", "rank": "Champion", "winrate": 0.58, "top_roles": ["Striker", "Defender"]},
            {"game_name": "PUBG", "rank": "Diamond", "winrate": 0.62, "top_roles": ["Sniper", "Support"]},
            {"game_name": "Call of Duty: Warzone", "rank": "Platinum", "winrate": 0.54, "top_roles": ["Sniper", "Rusher"]},
            {"game_name": "Hearthstone", "rank": "Legend", "winrate": 0.65, "top_roles": ["Aggro", "Control"]},
            {"game_name": "Teamfight Tactics", "rank": "Diamond", "winrate": 0.59, "top_roles": ["Flex", "Aggro"]},
            {"game_name": "FIFA 24", "rank": "Elite", "winrate": 0.71, "top_roles": ["Attacker", "Midfielder"]},
            {"game_name": "Street Fighter 6", "rank": "Master", "winrate": 0.63, "top_roles": ["Rushdown", "Zoner"]}
        ]
        
        games = []
        for i, game_data in enumerate(games_data):
            game = Game(
                id=str(uuid.uuid4()),
                user_id=users[i].id,
                game_name=game_data["game_name"],
                rank=game_data["rank"],
                winrate=game_data["winrate"],
                top_roles=json.dumps(game_data["top_roles"]),
                updated_at=datetime.now(timezone.utc)
            )
            games.append(game)
        
        session.add_all(games)
        
        # Create highlights
        highlights_data = [
            {"title": "Epic 6K with Genji", "clip_url": "https://youtube.com/watch?v=abc123", "tags": ["genji", "6k", "play_of_the_game"]},
            {"title": "Perfect Ace with Sova", "clip_url": "https://youtube.com/watch?v=def456", "tags": ["sova", "ace", "clutch"]},
            {"title": "Insane 1v5 Clutch", "clip_url": "https://youtube.com/watch?v=ghi789", "tags": ["clutch", "1v5", "epic"]},
            {"title": "Perfect Headshot Sequence", "clip_url": "https://youtube.com/watch?v=jkl012", "tags": ["headshot", "precision", "aim"]},
            {"title": "Team Wipe with Ultimate", "clip_url": "https://youtube.com/watch?v=mno345", "tags": ["ultimate", "team_wipe", "combo"]},
            {"title": "Amazing Save with Shield", "clip_url": "https://youtube.com/watch?v=pqr678", "tags": ["save", "shield", "defense"]},
            {"title": "Perfect Rotation and Flank", "clip_url": "https://youtube.com/watch?v=stu901", "tags": ["rotation", "flank", "strategy"]},
            {"title": "Incredible Reflex Block", "clip_url": "https://youtube.com/watch?v=vwx234", "tags": ["reflex", "block", "reaction"]},
            {"title": "Perfect Team Coordination", "clip_url": "https://youtube.com/watch?v=yza567", "tags": ["coordination", "teamwork", "sync"]},
            {"title": "Epic Comeback Victory", "clip_url": "https://youtube.com/watch?v=bcd890", "tags": ["comeback", "victory", "epic"]},
            {"title": "Perfect Timing Ultimate", "clip_url": "https://youtube.com/watch?v=efg123", "tags": ["timing", "ultimate", "perfect"]},
            {"title": "Amazing Crosshair Placement", "clip_url": "https://youtube.com/watch?v=hij456", "tags": ["crosshair", "placement", "aim"]},
            {"title": "Perfect Economy Management", "clip_url": "https://youtube.com/watch?v=klm789", "tags": ["economy", "management", "strategy"]},
            {"title": "Incredible Game Sense", "clip_url": "https://youtube.com/watch?v=nop012", "tags": ["game_sense", "prediction", "intelligence"]},
            {"title": "Perfect Communication Call", "clip_url": "https://youtube.com/watch?v=qrs345", "tags": ["communication", "call", "leadership"]}
        ]
        
        highlights = []
        for i, highlight_data in enumerate(highlights_data):
            highlight = Highlight(
                id=str(uuid.uuid4()),
                user_id=users[i % len(users)].id,
                title=highlight_data["title"],
                clip_url=highlight_data["clip_url"],
                tags=json.dumps(highlight_data["tags"]),
                created_at=datetime.now(timezone.utc)
            )
            highlights.append(highlight)
        
        session.add_all(highlights)
        
        # Create sponsors
        sponsors_data = [
            {"name": "GamingGear Pro", "verified": True},
            {"name": "EnergyDrink Co", "verified": False},
            {"name": "Razer Gaming", "verified": True},
            {"name": "Logitech G", "verified": True},
            {"name": "SteelSeries", "verified": True},
            {"name": "Corsair Gaming", "verified": True},
            {"name": "HyperX", "verified": True},
            {"name": "Red Bull Gaming", "verified": True},
            {"name": "Monster Energy Gaming", "verified": True},
            {"name": "G Fuel", "verified": True},
            {"name": "NVIDIA", "verified": True},
            {"name": "AMD Gaming", "verified": True},
            {"name": "Intel Gaming", "verified": True},
            {"name": "ASUS ROG", "verified": True},
            {"name": "MSI Gaming", "verified": True}
        ]
        
        sponsors = []
        for sponsor_data in sponsors_data:
            sponsor = Sponsor(
                id=str(uuid.uuid4()),
                name=sponsor_data["name"],
                org_id=str(uuid.uuid4()),
                verified=sponsor_data["verified"]
            )
            sponsors.append(sponsor)
        
        session.add_all(sponsors)
        
        # Create gigs
        gigs_data = [
            {"title": "Content Creator for Gaming Channel", "description": "Looking for skilled gamers to create content for our YouTube channel", "budget": 5000.0, "method": "upi", "status": "open"},
            {"title": "Esports Team Coach", "description": "Experienced coach needed for amateur esports team", "budget": 3000.0, "method": "card", "status": "open"},
            {"title": "Game Streamer", "description": "Professional streamer needed for daily gaming content", "budget": 4000.0, "method": "upi", "status": "open"},
            {"title": "Tournament Organizer", "description": "Experienced organizer for online gaming tournaments", "budget": 2500.0, "method": "card", "status": "open"},
            {"title": "Gaming Analyst", "description": "Analyst needed for esports team performance review", "budget": 3500.0, "method": "upi", "status": "open"},
            {"title": "Social Media Manager", "description": "Manager for gaming brand social media accounts", "budget": 2000.0, "method": "card", "status": "open"},
            {"title": "Game Tester", "description": "Professional game tester for new releases", "budget": 1500.0, "method": "upi", "status": "open"},
            {"title": "Esports Commentator", "description": "Commentator for live gaming tournaments", "budget": 3000.0, "method": "card", "status": "open"},
            {"title": "Gaming Equipment Reviewer", "description": "Reviewer for gaming peripherals and equipment", "budget": 2500.0, "method": "upi", "status": "open"},
            {"title": "Team Manager", "description": "Manager for professional esports team", "budget": 4000.0, "method": "card", "status": "open"},
            {"title": "Game Developer", "description": "Developer for indie gaming studio", "budget": 6000.0, "method": "upi", "status": "open"},
            {"title": "Gaming Journalist", "description": "Journalist for gaming news website", "budget": 2000.0, "method": "card", "status": "open"},
            {"title": "Esports Photographer", "description": "Photographer for gaming events and tournaments", "budget": 1800.0, "method": "upi", "status": "open"},
            {"title": "Gaming Video Editor", "description": "Editor for gaming content and highlights", "budget": 2200.0, "method": "card", "status": "open"},
            {"title": "Community Manager", "description": "Manager for gaming community and forums", "budget": 2800.0, "method": "upi", "status": "open"}
        ]
        
        gigs = []
        for i, gig_data in enumerate(gigs_data):
            gig = Gig(
                id=str(uuid.uuid4()),
                title=gig_data["title"],
                description=gig_data["description"],
                org_id=sponsors[i % len(sponsors)].id,
                budget=gig_data["budget"],
                method=gig_data["method"],
                status=gig_data["status"]
            )
            gigs.append(gig)
        
        session.add_all(gigs)
        
        # Create applications
        applications_data = [
            {"resume_link": "https://drive.google.com/resume1", "message": "I have 5 years of content creation experience", "status": "pending"},
            {"resume_link": "https://drive.google.com/resume2", "message": "I specialize in competitive gaming content", "status": "accepted"},
            {"resume_link": "https://drive.google.com/resume3", "message": "I have coaching experience in multiple games", "status": "pending"},
            {"resume_link": "https://drive.google.com/resume4", "message": "Professional streamer with 10k+ followers", "status": "accepted"},
            {"resume_link": "https://drive.google.com/resume5", "message": "Experienced tournament organizer", "status": "pending"},
            {"resume_link": "https://drive.google.com/resume6", "message": "Former pro player turned analyst", "status": "accepted"},
            {"resume_link": "https://drive.google.com/resume7", "message": "Social media expert in gaming industry", "status": "pending"},
            {"resume_link": "https://drive.google.com/resume8", "message": "QA tester with 3 years experience", "status": "accepted"},
            {"resume_link": "https://drive.google.com/resume9", "message": "Professional commentator for 5 years", "status": "pending"},
            {"resume_link": "https://drive.google.com/resume10", "message": "Equipment reviewer with technical background", "status": "accepted"},
            {"resume_link": "https://drive.google.com/resume11", "message": "Former team manager for top esports org", "status": "pending"},
            {"resume_link": "https://drive.google.com/resume12", "message": "Game developer with Unity experience", "status": "accepted"},
            {"resume_link": "https://drive.google.com/resume13", "message": "Gaming journalist with 7 years experience", "status": "pending"},
            {"resume_link": "https://drive.google.com/resume14", "message": "Event photographer specializing in gaming", "status": "accepted"},
            {"resume_link": "https://drive.google.com/resume15", "message": "Video editor with gaming content focus", "status": "pending"},
            {"resume_link": "https://drive.google.com/resume16", "message": "Community manager for large gaming discord", "status": "accepted"},
            {"resume_link": "https://drive.google.com/resume17", "message": "Content creator with 50k+ subscribers", "status": "pending"},
            {"resume_link": "https://drive.google.com/resume18", "message": "Esports coach with championship experience", "status": "accepted"},
            {"resume_link": "https://drive.google.com/resume19", "message": "Professional gamer with tournament wins", "status": "pending"},
            {"resume_link": "https://drive.google.com/resume20", "message": "Gaming influencer with brand partnerships", "status": "accepted"}
        ]
        
        applications = []
        for i, app_data in enumerate(applications_data):
            application = Application(
                id=str(uuid.uuid4()),
                gig_id=gigs[i % len(gigs)].id,
                user_id=users[i % len(users)].id,
                resume_link=app_data["resume_link"],
                message=app_data["message"],
                status=app_data["status"]
            )
            applications.append(application)
        
        session.add_all(applications)
        
        # Create teams
        teams_data = [
            {"name": "Elite Warriors", "members": [0, 1, 2]},
            {"name": "Rising Stars", "members": [1, 2, 3]},
            {"name": "Phoenix Gaming", "members": [2, 3, 4]},
            {"name": "Shadow Hunters", "members": [3, 4, 5]},
            {"name": "Thunder Strike", "members": [4, 5, 6]},
            {"name": "Ice Dragons", "members": [5, 6, 7]},
            {"name": "Fire Falcons", "members": [6, 7, 8]},
            {"name": "Storm Riders", "members": [7, 8, 9]},
            {"name": "Golden Eagles", "members": [8, 9, 10]},
            {"name": "Silver Wolves", "members": [9, 10, 11]},
            {"name": "Crimson Knights", "members": [10, 11, 12]},
            {"name": "Azure Dragons", "members": [11, 12, 13]},
            {"name": "Emerald Phoenix", "members": [12, 13, 14]},
            {"name": "Sapphire Serpents", "members": [13, 14, 0]},
            {"name": "Ruby Raptors", "members": [14, 0, 1]}
        ]
        
        teams = []
        for i, team_data in enumerate(teams_data):
            member_ids = [users[idx].id for idx in team_data["members"]]
            team = Team(
                id=str(uuid.uuid4()),
                name=team_data["name"],
                owner_id=users[team_data["members"][0]].id,
                members=json.dumps(member_ids)
            )
            teams.append(team)
        
        session.add_all(teams)
        
        # Add 15 new dummy users with games and bios
        new_users = []
        new_profiles = []
        new_games = []
        for i in range(1, 16):
            uname = f"dummy_user_{i}"
            email = f"dummy{i}@example.com"
            discord = f"dummy_user_{i}#10{i:02d}"
            wallet = f"0xdummy{i:04x}"
            user_id = str(uuid.uuid4())
            new_user = User(
                id=user_id,
                email=email,
                username=uname,
                discord_id=discord,
                wallet_address=wallet,
                created_at=datetime.now(timezone.utc)
            )
            new_users.append(new_user)
            # Profile
            bio = f"This is the bio for {uname}, a passionate gamer."
            region = ["North America", "Europe", "Asia"][i % 3]
            roles = json.dumps(["DPS", "Support"] if i % 2 == 0 else ["Tank", "Flex"])
            badges = json.dumps(["Newbie", "Challenger"] if i % 2 == 0 else ["Veteran", "Strategist"])
            grind_data = {"hours_played": 100 + i * 10, "rank": ["Bronze", "Silver", "Gold", "Platinum"][i % 4]}
            pentagon_data = {"mechanical": 50 + i, "game_sense": 55 + i, "communication": 60 + i, "teamwork": 65 + i, "adaptability": 70 + i}
            new_profile = Profile(
                user_id=user_id,
                bio=bio,
                region=region,
                roles=roles,
                badges=badges,
                grind_data=grind_data,
                pentagon_data=pentagon_data
            )
            new_profiles.append(new_profile)
            # Game
            game_name = ["Minecraft", "Fortnite", "Valorant", "Apex Legends", "Rocket League"][i % 5]
            rank = ["Bronze", "Silver", "Gold", "Platinum"][i % 4]
            winrate = 0.4 + (i % 5) * 0.1
            top_roles = json.dumps(["Builder", "Shooter"] if i % 2 == 0 else ["Strategist", "Sniper"])
            new_game = Game(
                id=str(uuid.uuid4()),
                user_id=user_id,
                game_name=game_name,
                rank=rank,
                winrate=winrate,
                top_roles=top_roles,
                updated_at=datetime.now(timezone.utc)
            )
            new_games.append(new_game)
        session.add_all(new_users)
        session.add_all(new_profiles)
        session.add_all(new_games)
        
        session.commit()
        print("✅ Enhanced seed data created successfully!")
        print(f"Created: {len(users)} users, {len(profiles)} profiles, {len(games)} games, {len(highlights)} highlights, {len(sponsors)} sponsors, {len(gigs)} gigs, {len(applications)} applications, {len(teams)} teams")
    finally:
        session.close()

if __name__ == '__main__':
    seed_data()
