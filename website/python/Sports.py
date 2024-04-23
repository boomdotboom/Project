import mysql.connector
import sys


mydb = mysql.connector.connect(
  host="localhost",
  user="aemorton",
  password="eT5wisee",
  database= "aemorton"
) 
cursor = mydb.cursor()

#par1 = sys.args[1]
#par2 = sys.args[2]
#par3 = sys.args[3]
#par4 = sys.args[4]
#par5 = sys.args[5]

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
                                    PlayerId INTEGER,
                                    TeamId INTEGER,
                                    Name TEXT,
                                    Position TEXT,
                                    CONSTRAINT  PK_Player PRIMARY KEY(PlayerId, TeamId),
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
        cursor.execute('''INSERT INTO Player(PlayerId, TeamId, Name, Position) VALUES 
                       (9,1,'Desmond Ridder','Quarterback'),(22,1,'Michael Carter','Running back'),(34,1,'Jalen Thompson','Safety'),
                       (18,2,'Kirk Cousins','Quarterback'),(28,2,'Carlos Washington Jr.','Running back'),(27,2,'Richie Grant','Safety'),
                       (14,3,'Andy Dalton','Quarterback'),(41,3,'Spencer Brown','Running back'),(42,3,'Sam Franklin Jr.','Safety'),
                       (17,4,'Tyson Bagent','Quarterback'),(24,4,'Khalil Herbert','Running back'),(25,4,'Adrian Colbert','Safety'),
                       (15,5,'Trey Lance','Quarterback'),(34,5,'Malik Davis','Running Back'),(28,5,'Markquese Bell','Safety'),
                       (16,6,'Jared Golf','Quarterback'),(26,6,'Jake Funk','Running back'),(32,6,'Brian Branch','Safety'),
                       (8,7,'Sean Clifford','Quarterback'),(23,7,'AJ Dillon','Running back'),(37,7,'Carrington Valentine','Safety'),
                       (13,8,'Stetson Bennett','Quarterback'),(20,8,'Zach Evans','Running back'),(34,8,'Tanner Ingle','Safety'),
                       (12,9,'Nick Mullens','Quarterback'),(33,9,'Aaron Jones','Running back'),(6,9,'Lewis Cine','Safety'),
                       (4,10,'Derek Carr','Quarterback'),(41,10,'Alvin Kamara','Running back'),(31,10,'Jordan Howden','Safety'),
                       (8,11,'Daniel Jones','Quarterback'),(20,11,'Eric Gray','Running back'),(39,11,'Gervarrius Owens','Safety'),
                       (19,12,'Tanner McKee','Quarterback'),(14,12,'Kenneth Gainwell','Running back'),(21,12,'Sydney Brown','Safety'),
                       (17,13,'Brandon Allen','Quarterback'),(23,13,'Christian McCaffrey','Running back'),(29,13,'Talanoa Hufanga','Safety'),
                       (7,14,'Geno Smith','Quarterback'),(1,14,'Dee Eskridge','Running back'),(2,14,'Rayshawn Jenkins','Safety'),
                       (6,15,'Bakere Mayfield','Quarterback'),(44,15,'Sean Tucker','Running back'),(31,15,'Antoine Winfield Jr.','Safety'),
                       (11,16,'Jake Fromm','Quarterback'),(23,16,'Chris Rodriguez Jr.','Running back'),(39,16,'Jeremy Reaves','Safety'),
                       (12,17,'Malik Cunningham','Quarterback'),(43,17,'Justice Hill','Running back'),(29,17,'ArDarius Washington','Safety'),
                       (17,18,'Josh Allen','Quarterback'),(4,18,'James Cook','Running back'),(3,18,'Damar Hamlin','Safety'),
                       (9,19,'Joe Burrow','Quarterback'),(30,19,'Chase Brown','Running back'),(23,19,'Dax Hill','Safety'),
                       (12,20,'Jeff Driskel','Quarterback'),(4,20,'Deshaun Watson','Running back'),(1,20,'Juan Thornhill','Safety'),
                       (11,21,'Ben DiNucci','Quarterback'),(36,21,'Tyler Badie','Running back'),(34,21,'JL Skinner','Safety'),
                       (8,22,'Tim Boyle','Quarterback'),(28,22,'Gerrid Doaks','Running back'),(5,22,'Jalen Pitre','Safety'),
                       (4,23,'Sam Ehlinger','Quarterback'),(26,23,'Evan Hull','Running back'),(42,23,'Tevor Denbow','Safety'),
                       (3,24,'C.J. Beathard','Quarterback'),(4,24,'Tank Bigsby','Running back'),(5,24,'Andre Cisco','Safety'),
                       (15,25,'Patrick Mahomes','Quarterback'),(30,25,'Keaontay Ingram','Running back'),(26,25,'Deon Bush','Safety'),
                       (4,26,'Aidan OConnell','Quarterback'),(38,26,'Brittain Brown','Running back'),(40,26,'Jaydon Grant','Safety'),
                       (8,27,'Max Duggan','Quarterback'),(42,27,'Elijah Dotson','Running back'),(24,27,'AJ Finley','Safety'),
                       (1,28,'Tua Tagovailoa','Quarterback'),(26,28,'Salvon Ahmed','Running back'),(8,28,'Jevon Holland','Safety'),
                       (4,29,'Bailey Zappe','Quarterback'),(39,29,'JaMycal Hasty','Running back'),(5,29,'Jabrill Peppers','Safety'),
                       (8,30,'Aaron Rodgers','Quarterback'),(20,30,'Breece Hall','Running back'),(4,30,'D.J. Reed','Safety'),
                       (4,31,'Kyle Allen','Quarterback'),(22,31,'Najee Harris','Running back'),(33,31,'Nathan Meadors','Safety'),
                       (8,32,'Will Levis','Quarterback'),(36,32,'Julius Chestnut','Running back'),(44,32,'Mike Brown','Safety')
                       ''')
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

def view_teams_by_conference(conference):
        cursor.execute(f"SELECT * FROM Team WHERE Conference='{conference}' ORDER BY Nickname ASC")
        return cursor.fetchall()

def view_games_by_team(team_id): # The Problem CHILDREN
        cursor.execute(f"SELECT g.Date, t1.Location, t1.Nickname, g.Score1, t2.Location, t2.Nickname, g.Score2, IF(g.Score1>g.Score2, Concat(t1.Nickname,' Won'),Concat(t1.Nickname,' Lost')) AS Result FROM Game g JOIN Team t1 on t1.TeamId= g.TeamId1 JOIN Team t2 on t2.TeamId= g.TeamId2 WHERE g.TeamId1= {team_id} OR g.teamId2= {team_id}")
        return cursor.fetchall()

def view_results_by_date(date):# The Problem CHILDREN
        cursor.execute(f"SELECT g.Date, t1.Location, t1.Nickname, g.Score1, t2.Location, t2.Nickname, g.Score2, IF(g.Score1>g.Score2, Concat(t1.Nickname,' Won'),Concat(t2.Nickname,' Won')) AS Result FROM Game g JOIN Team t1 on t1.TeamId= g.TeamId1 JOIN Team t2 on t2.TeamId= g.TeamId2 WHERE g.date= '{date}' ")
        return cursor.fetchall()

def __del__():
        cursor.close()
def bonus(team_id):
  cursor.execute(f"SELECT g.Date, t1.Location, t1.Nickname, p1.Name, p1.Position, g.Score1, t2.Location, t2.Nickname,p2.Name, p2.position, g.Score2, IF(g.Score1>g.Score2, Concat(t1.Nickname,' Won'),Concat(t1.Nickname,' Lost')) AS Result FROM Game g JOIN Team t1 on t1.TeamId= g.TeamId1 JOIN Team t2 on t2.TeamId= g.TeamId2 JOIN Player p1 on p1.TeamId= t1.TeamId JOIN Player p2 on p2.TeamId= t2.TeamId WHERE g.TeamId1= {team_id} OR g.teamId2= {team_id} ")
  return cursor.fetchall()

    # Add a game
create_tables()
add_game(1, 2, 29, 21, 17,'2024-04-15')

    # Add a player
add_player(1,29,'Tom Brady','Quarterback')
    # View players on a team

print(view_players_on_team(29))
print()
    # View players by position
print(view_players_by_position('Quarterback'))
print()
    # View teams by conference
print(view_teams_by_conference('AFC'))
print()
    # View games by team
print(view_games_by_team(2))
print()
    # View results by date
print(view_results_by_date('2024-04-15'))
print()



#print(bonus(2))