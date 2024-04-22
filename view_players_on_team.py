import mysql.connector
import sys


mydb = mysql.connector.connect(
  host="localhost",
  user="aemorton",
  password="eT5wisee",
  database= "aemorton"
) 
cursor = mydb.cursor()

team_id = sys.args[1]
def view_players_on_team(team_id):
        cursor.execute(f"SELECT Nickname, PlayerId, Name, Position FROM Team,Player WHERE Player.TeamId = {team_id} AND Team.TeamID= {team_id}")
        return cursor.fetchall()
view_players_on_team(team_id)