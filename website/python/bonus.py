import mysql.connector
import sys


mydb = mysql.connector.connect(
  host="localhost",
  user="aemorton",
  password="eT5wisee",
  database= "aemorton"
) 
cursor = mydb.cursor()
date= sys.argv[1]

def bonus(date):
  cursor.execute('''SELECT g.Date, t1.Location, t1.Nickname, p1.Name, p1.Position, g.Score1, 
                 t2.Location, t2.Nickname,p1.Name, p1.position g.Score2, 
            IF(g.Score1>g.Score2, Concat(t1.Nickname," Won"),Concat(t1.Nickname," Lost")) AS Result 
                FROM Game g 
                    JOIN Team t1 on t1.TeamId= g.TeamId1 
                    JOIN Team t2 on t2.TeamId= g.TeamId2
                    JOIN Player p1 on p.TeamId= t1.TeamId
                    JOIN Player p2 on p.TeamId= t2.TeamId
                        WHERE g.date= '{date}' ''')
  return cursor.fetchall()