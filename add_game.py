import mysql.connector
import sys

mydb = mysql.connector.connect(
  host="localhost",
  user="aemorton",
  password="eT5wisee",
  database= "aemorton"
)
cursor = mydb.cursor()
game_id = sys.args[1]
team1_id = sys.args[2]
team2_id = sys.args[3]
score1= sys.args[4]
score2 = sys.args[5]
date= sys.args[6]
def add_game(game_id, team1_id, team2_id, score1, score2, date):
        cursor.execute(f"INSERT INTO Game (GameId ,TeamId1, TeamId2, Score1, Score2, Date) VALUES ({game_id},{team1_id},{team2_id},{score1},{score2},'{date}')")
add_game(game_id,team1_id,team2_id,score1,score2,date)