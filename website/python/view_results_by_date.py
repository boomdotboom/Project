import mysql.connector
import sys


mydb = mysql.connector.connect(
  host="localhost",
  user="aemorton",
  password="eT5wisee",
  database= "aemorton"
) 
cursor = mydb.cursor()

date = sys.args[1]
def view_results_by_date(date):# The Problem CHILDREN
        cursor.execute('''SELECT g.Date, t1.Location, t1.Nickname, g.Score1, t2.Location, t2.Nickname, g.Score2, 
            IF(g.Score1>g.Score2, Concat(t1.Nickname," Won"),Concat(t1.Nickname," Lost")) AS Result 
                FROM Game g 
                    JOIN Team t1 on t1.TeamId= g.TeamId1 
                    JOIN Team t2 on t2.TeamId= g.TeamId2 
                        WHERE g.date= '{date}' ''')
        return cursor.fetchall()
view_results_by_date(date)
