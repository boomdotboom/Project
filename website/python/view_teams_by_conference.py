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
s=view_teams_by_conference(conference)
if(s==[]):
  print("Could Not Find Conference")
else:
  print("TeamId".ljust(6)+"Location".ljust(20)+"Nickname".ljust(20)+"Conference".ljust(10)+"Division".ljust(8))
  for l in s:
    print(str(l[0]).ljust(6)+str(l[1]).ljust(20)+str(l[2]).ljust(20)+str(l[3]).ljust(10)+str(l[4].ljust(8)))