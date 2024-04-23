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
s=view_players_on_team(team_id)
if(s==[]):
  print("Could Not Find Team")
else:
  print("Nickname".ljust(20)+"Player#".ljust(6)+"Name".ljust(30)+"Position".ljust(20))
  for l in s:
    print(str(l[0]).ljust(20)+str(l[1]).ljust(6)+str(l[2]).ljust(30)+str(l[3]).ljust(20))