import mysql.connector
import sys
import Sports
import sys
import traceback
import logging

Sports.open_database()

game_id = sys.args[1]
team1_id = sys.args[2]
team2_id = sys.args[3]
score1= sys.args[4]
score2 = sys.args[5]
date= sys.args[6]

Sports.add_game(game_id,team1_id,team2_id,score1,score2,date)

res=Sports.executeSelect('Select * From Game')
res = res.split('\n')  # split the header and data for printing
print("<br/>" + "<br/>")
print("<br/>" + "Table Game after:"+"<br/>" +
          res[0] + "<br/>"+res[1] + "<br/>")
for i in range(len(res)-2):
    print(res[i+2]+"<br/>")