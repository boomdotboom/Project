import sqlite3

class NFLDatabase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Team (
                                    TeamId INTEGER PRIMARY KEY,
                                    Location TEXT,
                                    Nickname TEXT,
                                    Conference TEXT,
                                    Division TEXT
                                )''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Game (
                                    GameId INTEGER PRIMARY KEY,
                                    TeamId1 INTEGER,
                                    TeamId2 INTEGER,
                                    Score1 INTEGER,
                                    Score2 INTEGER,
                                    Date DATE,
                                    FOREIGN KEY (TeamId1) REFERENCES Team(TeamId),
                                    FOREIGN KEY (TeamId2) REFERENCES Team(TeamId)
                                )''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Player (
                                    PlayerId INTEGER PRIMARY KEY,
                                    TeamId INTEGER,
                                    Name TEXT,
                                    Position TEXT,
                                    FOREIGN KEY (TeamId) REFERENCES Team(TeamId)
                                )''')
        self.conn.commit()

    def add_game(self, team1_id, team2_id, score1, score2, date):
        self.cursor.execute('''INSERT INTO Game (TeamId1, TeamId2, Score1, Score2, Date)
                                VALUES (?, ?, ?, ?, ?)''', (team1_id, team2_id, score1, score2, date))
        self.conn.commit()

    def add_player(self, team_id, name, position):
        self.cursor.execute('''INSERT INTO Player (TeamId, Name, Position)
                                VALUES (?, ?, ?)''', (team_id, name, position))
        self.conn.commit()

    def view_players_on_team(self, team_id):
        self.cursor.execute('''SELECT * FROM Player WHERE TeamId = ?''', (team_id,))
        return self.cursor.fetchall()

    def view_players_by_position(self, position):
        self.cursor.execute('''SELECT * FROM Player WHERE Position = ?''', (position,))
        return self.cursor.fetchall()

    def view_teams_by_conference(self):
        self.cursor.execute('''SELECT * FROM Team ORDER BY Conference ASC, Wins DESC''')
        return self.cursor.fetchall()

    def view_games_by_team(self, team_id):
        self.cursor.execute('''SELECT G.*, T1.Location, T1.Nickname AS Team1_Nickname, T2.Location, T2.Nickname AS Team2_Nickname
                                FROM Game G
                                JOIN Team T1 ON G.TeamId1 = T1.TeamId
                                JOIN Team T2 ON G.TeamId2 = T2.TeamId
                                WHERE G.TeamId1 = ? OR G.TeamId2 = ?''', (team_id, team_id))
        return self.cursor.fetchall()

    def view_results_by_date(self, date):
        self.cursor.execute('''SELECT T.Location, T.Nickname, G.Score1, G.Score2, 
                                        CASE 
                                            WHEN G.Score1 > G.Score2 THEN T.Location || ' ' || T.Nickname
                                            WHEN G.Score2 > G.Score1 THEN T1.Location || ' ' || T1.Nickname
                                            ELSE 'Draw'
                                        END AS Winner
                                FROM Game G
                                JOIN Team T ON G.TeamId1 = T.TeamId
                                JOIN Team T1 ON G.TeamId2 = T1.TeamId
                                WHERE G.Date = ?''', (date,))
        return self.cursor.fetchall()

    def __del__(self):
        self.conn.close()

# Example Usage:
if __name__ == "__main__":
    db = NFLDatabase('nfl_database.db')

    # Add a game
    db.add_game(1, 2, 21, 17, '2024-04-15')

    # Add a player
    db.add_player(1, 'Tom Brady', 'Quarterback')

    # View players on a team
    print(db.view_players_on_team(1))

    # View players by position
    print(db.view_players_by_position('Quarterback'))

    # View teams by conference
    print(db.view_teams_by_conference())

    # View games by team
    print(db.view_games_by_team(1))

    # View results by date
    print(db.view_results_by_date('2024-04-15'))