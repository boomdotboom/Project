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
        cursor.execute(f"SELECT * FROM Player WHERE Position = '{position}'")
        return cursor.fetchall()
view_players_by_position(position)