import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="aemorton",
  password="eT5wisee",
  database= "aemorton"
) 
cursor = mydb.cursor()

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
def add_game( team1_id, team2_id, score1, score2, date):
        cursor.execute(f"INSERT INTO Game (TeamId1, TeamId2, Score1, Score2, Date) VALUES ({team1_id},'{team2_id}','{score1}','{score2}')")

def add_player( team_id, name, position):
        cursor.execute(f"INSERT INTO Player (TeamId, Name, Position)
                                VALUES ('{team_id}','{name}', '{position}')")

def view_players_on_team(team_id):
        cursor.execute(f"SELECT Nickname, PlayerId, Name, Postion  FROM Team,Player WHERE Team.TeamID= Player.TeamID AND TeamId = '{team_id}'")
        return cursor.fetchall()

def view_players_by_position(position):
        cursor.execute(f"SELECT * FROM Player WHERE Position = '{position}'")
        return cursor.fetchall()

def view_teams_by_conference():
        cursor.execute("SELECT * FROM Team ORDER BY Conference ASC")
        return cursor.fetchall()

def view_games_by_team( team_id):
        cursor.execute("SELECT G.*, T1.Location, T1.Nickname AS Team1_Nickname, T2.Location, T2.Nickname AS Team2_Nickname")
        return cursor.fetchall()

def view_results_by_date(date):
        cursor.execute("SELECT T.Location, T.Nickname, G.Score1, G.Score2,")
        return cursor.fetchall()

def __del__():
        cursor.close()

    # Add a game
add_game(1, 2, 21, 17, '2024-04-15')

    # Add a player
add_player(1, 'Tom Brady', 'Quarterback')

    # View players on a team
print(view_players_on_team(1))

    # View players by position
print(view_players_by_position('Quarterback'))

    # View teams by conference
print(view_teams_by_conference())

    # View games by team
print(view_games_by_team(1))

    # View results by date
print(view_results_by_date('2024-04-15'))