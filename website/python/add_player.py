import mysql.connector
import sys


mydb = mysql.connector.connect(
  host="localhost",
  user="aemorton",
  password="eT5wisee",
  database= "aemorton"
) 
cursor = mydb.cursor()

player_id = sys.args[1]
team_id = sys.args[2]
name = sys.args[3]
position = sys.args[4]
def add_player(player_id,team_id, name, position):
        cursor.execute(f"INSERT INTO Player (PlayerID ,TeamId, Name, Position) VALUES ({player_id},{team_id},'{name}', '{position}')")
add_player(player_id,team_id,name,position)