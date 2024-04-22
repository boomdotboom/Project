import mysql.connector
import sys


mydb = mysql.connector.connect(
  host="localhost",
  user="aemorton",
  password="eT5wisee",
  database= "aemorton"
) 
cursor = mydb.cursor()

par1 = sys.args[1]
par2 = sys.args[2]
par3 = sys.args[3]
par4 = sys.args[4]
par5 = sys.args[5]

def create_tables():
        cursor.execute('''CREATE TABLE Team (
                                    TeamId INTEGER PRIMARY KEY,
                                    Location TEXT,
                                    Nickname TEXT,
                                    Conference TEXT,
                                    Division TEXT
                                )''')
        cursor.execute('''CREATE TABLE Game (
                                    GameId INTEGER PRIMARY KEY,
                                    TeamId1 INTEGER,
                                    TeamId2 INTEGER,
                                    Score1 INTEGER,
                                    Score2 INTEGER,
                                    Date DATE,
                                    FOREIGN KEY (TeamId1) REFERENCES Team(TeamId),
                                    FOREIGN KEY (TeamId2) REFERENCES Team(TeamId)
                                )''')
        cursor.execute('''CREATE TABLE Player (
                                    PlayerId INTEGER PRIMARY KEY,
                                    TeamId INTEGER,
                                    Name TEXT,
                                    Position TEXT,
                                    FOREIGN KEY (TeamId) REFERENCES Team(TeamId)
                                )''')
        cursor.execute('''INSERT INTO Team (TeamID,Location, Nickname, Conference, Division) VALUES 
                       (1, 'Arizona', 'Cardinals', 'NFC', 'West'),
                       (2, 'Alanta','Falcons','NFC', 'South'), (3, 'Carolina','Panthers','NFC','South'),
                       (4, 'Chicago','Bears','NFC','North'), (5,'Dallas','Cowboys','NFC','East'),
                       (6,'Detriot','Lions','NFC','North'), (7,'Green Bay','Packers','NFC','North'), 
                       (8,'Los Angeles','Rams','NFC','West'), (9,'Minnesota','Vikings','NFC', 'North'),
                       (10,'New Orleans','Saints','NFC','South'), (11,'New York','Giants','NFC','East'),
                       (12,'Philadelphia','Eagles','NFC','East'), (13,'San Francisco','49ers','NFC','West'),
                       (14,'Seattle','Seahawks','NFC','West'), (15, 'Tampa Bay','Buccaneers','NFC','South'),
                       (16, 'Washington','Commanders','NFC','East'), (17, 'Baltimore','Ravens','AFC','North'),
                       (18,'Buffalo','Bills','AFC','East'), (19,'Cincinnati','Bengals','AFC','North'),
                       (20,'Cleveland','Browns','AFC','North'), (21,'Denver','Broncos','AFC','South'),
                       (22,'Houston','Texans','AFC','South'), (23,'Indianapolis','Colts','AFC','South'),
                       (24,'Jacksonville','Jaguars','AFC','South'), (25,'Kansas City','Chiefs','AFC','West'),
                       (26,'Las Vegas','Raiders','AFC','West'), (27,'Los Angeles','Chargers','AFC','West'),
                       (28,'Miami','Dolphins','AFC','East'), (29,'New England','Patriots','AFC','East'),
                       (30,'New York','Jets','AFC','East'), (31,'Pittsburgh','Steelers','AFC','North'),
                       (32,'Tennessee','Titans','AFC','South')''')
def add_game(game_id, team1_id, team2_id, score1, score2, date):
        cursor.execute(f"INSERT INTO Game (GameId ,TeamId1, TeamId2, Score1, Score2, Date) VALUES ({game_id},{team1_id},{team2_id},{score1},{score2},'{date}')")

def add_player(player_id,team_id, name, position):
        cursor.execute(f"INSERT INTO Player (PlayerID ,TeamId, Name, Position) VALUES ({player_id},{team_id},'{name}', '{position}')")

def view_players_on_team(team_id):
        cursor.execute(f"SELECT Nickname, PlayerId, Name, Position FROM Team,Player WHERE Player.TeamId = {team_id} AND Team.TeamID= {team_id}")
        return cursor.fetchall()

def view_players_by_position(position):
        cursor.execute(f"SELECT * FROM Player WHERE Position = '{position}'")
        return cursor.fetchall()

def view_teams_by_conference():
        cursor.execute("SELECT * FROM Team ORDER BY Conference, Nickname ASC")
        return cursor.fetchall()

def view_games_by_team(team_id): # The Problem CHILDREN
        cursor.execute(f'''SELECT g.Date, t1.Location, t1.Nickname, g.Score1, t2.Location, t2.Nickname, g.Score2, 
                       IF(g.Score1>g.Score2, Concat(t1.Nickname,' Won'),Concat(t1.Nickname,' Lost')) AS Result 
                       FROM Game g 
                            JOIN Team t1 on t1.TeamId= g.TeamId1 
                            JOIN Team t2 on t2.TeamId= g.TeamId2 
                                WHERE g.TeamId1= {team_id} 
                                    OR g.teamId2= {team_id}''')
        return cursor.fetchall()

def view_results_by_date(date):# The Problem CHILDREN
        cursor.execute('''SELECT g.Date, t1.Location, t1.Nickname, g.Score1, t2.Location, t2.Nickname, g.Score2, 
            IF(g.Score1>g.Score2, Concat(t1.Nickname," Won"),Concat(t1.Nickname," Lost")) AS Result 
                FROM Game g 
                    JOIN Team t1 on t1.TeamId= g.TeamId1 
                    JOIN Team t2 on t2.TeamId= g.TeamId2 
                        WHERE g.date= '{date}' ''')
        return cursor.fetchall()

def __del__():
        cursor.close()

    # Add a game
create_tables()
add_game(1, 2, 29, 21, 17,'2024-04-15')

    # Add a player
#add_player(1,29,'Tom Brady','Quarterback')

    # View players on a team
#print(view_players_on_team(29))

    # View players by position
#print(view_players_by_position('Quarterback'))

    # View teams by conference
#print(view_teams_by_conference())

    # View games by team
print(view_games_by_team(2))
print("in progress")

    # View results by date
print(view_results_by_date('2024-04-15'))
print("in progress")