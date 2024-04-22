import mysql.connector
import sys


mydb = mysql.connector.connect(
  host="localhost",
  user="aemorton",
  password="eT5wisee",
  database= "aemorton"
) 
cursor = mydb.cursor()
conference = sys.args[1]
def view_teams_by_conference(conference):
        cursor.execute(f"SELECT * FROM Team WHERE Conference='{conference}' ORDER BY Nickname ASC")
        return cursor.fetchall()
view_teams_by_conference(conference)