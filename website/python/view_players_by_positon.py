import mysql.connector
import sys


mydb = mysql.connector.connect(
  host="localhost",
  user="aemorton",
  password="eT5wisee",
  database= "aemorton"
) 
cursor = mydb.cursor()

position = sys.args[1]
def view_players_by_position(position):
        cursor.execute(f"SELECT PlayerId,Name, Position, Location, Nickname FROM Player, Team WHERE Position = '{position}' AND Player.TeamId= Team.TeamId")
        return cursor.fetchall()
s= view_players_by_position(position)
if(s==[]):
  print("Could Not Find Position")
else:
  print("Player#".ljust(6)+"Name".ljust(30)+"Positon".ljust(20)+"Location".ljust(25)+"Nickname".ljust(20))
  for l in s:
    print(str(l[0]).ljust(6)+str(l[1]).ljust(30)+str(l[2]).ljust(20)+str(l[3]).ljust(25)+str(l[4]).ljust(20))